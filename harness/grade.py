"""Grade saved answers against the rubrics and summarize the results.

Usage (from the repository root):
    python harness/grade.py results/2026-10-23

Reads responses.jsonl in the given folder, asks the grader model (set in
config.py) to grade each answer as Full, Partial, or Incorrect, and writes:
    grades.jsonl   one line per graded answer, with the grader's justification
    summary.md     grade counts by model and tier, and a per-question table
Answers that were already graded are skipped, so the script can be re-run safely.
"""

import argparse
import json
import os
import re
from collections import Counter, defaultdict

from dotenv import load_dotenv

from clients import ask
from config import GRADER, QUESTION_BANK
from questions import load_questions, load_scoring_definitions

GRADES = ("Full", "Partial", "Incorrect")

GRADER_PROMPT = """You are grading an answer to a chemistry question against an expert rubric.

Scoring definitions:
{scoring}

Question:
{question}

Rubric:
{rubric}

Answer to grade:
{answer}

Grade the answer strictly according to the rubric and scoring definitions. Points
introduced with "Strong answers" are not required for full credit. Do not reward
length or confident tone, and do not penalize correct points that the rubric does
not mention unless they are wrong.

Reply with only a JSON object in this form:
{{"grade": "Full" | "Partial" | "Incorrect", "justification": "<one to three sentences>"}}"""


def parse_grade(text):
    """Extract the grade and justification from the grader's reply."""
    match = re.search(r"\{.*\}", text, re.S)
    if match:
        try:
            data = json.loads(match.group(0))
            if data.get("grade") in GRADES:
                return data["grade"], data.get("justification", "")
        except json.JSONDecodeError:
            pass
    return "Unparsed", text.strip()


def read_jsonl(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def write_summary(grades, path):
    """Write grade counts by model and tier, plus a per-question table."""
    providers = sorted({g["provider"] for g in grades})
    tiers = sorted({g["tier"] for g in grades})
    counts = defaultdict(Counter)
    by_question = defaultdict(dict)
    for g in grades:
        counts[(g["provider"], g["tier"])][g["grade"]] += 1
        counts[(g["provider"], "Total")][g["grade"]] += 1
        by_question[g["question_id"]][g["provider"]] = g["grade"]

    lines = ["# Results summary", "",
             f"Grader: {GRADER[1]}. Counts are Full / Partial / Incorrect.", "",
             "| Tier | " + " | ".join(providers) + " |",
             "|---|" + "---|" * len(providers)]
    for tier in tiers + ["Total"]:
        cells = []
        for p in providers:
            c = counts[(p, tier)]
            cells.append(f"{c['Full']} / {c['Partial']} / {c['Incorrect']}")
        label = f"**{tier}**" if tier == "Total" else str(tier)
        lines.append(f"| {label} | " + " | ".join(cells) + " |")

    lines += ["", "## By question", "",
              "| Question | " + " | ".join(providers) + " |",
              "|---|" + "---|" * len(providers)]
    for qid in sorted(by_question, key=lambda q: int(q[1:])):
        lines.append(f"| {qid} | " + " | ".join(by_question[qid].get(p, "") for p in providers) + " |")

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", help="results folder, e.g. results/2026-10-23")
    args = parser.parse_args()

    load_dotenv()
    questions = {q["id"]: q for q in load_questions(QUESTION_BANK)}
    scoring = load_scoring_definitions(QUESTION_BANK)

    responses = read_jsonl(os.path.join(args.run_dir, "responses.jsonl"))
    grades_path = os.path.join(args.run_dir, "grades.jsonl")
    grades = read_jsonl(grades_path)
    done = {(g["provider"], g["question_id"]) for g in grades}

    grader_provider, grader_model = GRADER
    with open(grades_path, "a", encoding="utf-8") as out:
        for r in responses:
            key = (r["provider"], r["question_id"])
            if key in done:
                continue
            q = questions[r["question_id"]]
            prompt = GRADER_PROMPT.format(scoring=scoring, question=q["prompt"],
                                          rubric=q["rubric"], answer=r["text"])
            print(f"Grading {r['provider']} {r['question_id']}...")
            try:
                reply = ask(grader_provider, grader_model, prompt)
            except Exception as error:
                print(f"  FAILED ({error}); re-run to retry")
                continue
            grade, justification = parse_grade(reply["text"])
            record = {"question_id": r["question_id"], "tier": r["tier"],
                      "provider": r["provider"], "model_version": r["model_version"],
                      "grade": grade, "justification": justification,
                      "grader": reply["model_version"]}
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            out.flush()
            grades.append(record)

    write_summary(grades, os.path.join(args.run_dir, "summary.md"))
    print(f"\nWrote {grades_path} and summary.md")
    unparsed = [g for g in grades if g["grade"] == "Unparsed"]
    if unparsed:
        print(f"Warning: {len(unparsed)} grades could not be parsed; check grades.jsonl.")


if __name__ == "__main__":
    main()
