"""Compare the grades two graders gave to the same answers.

Usage (from the repository root):
    python harness/compare_grades.py results/run1 claude-opus-5-5 gpt-6.1-sol

Reads grades_<grader>.jsonl for each grader and writes
comparison_<grader1>_vs_<grader2>.md with:
    - how often the two graders gave the same grade, and Cohen's kappa
      (agreement corrected for chance: 1 is perfect, 0 is no better than chance)
    - a table of grade pairs (grader 1 grade vs. grader 2 grade)
    - each model's average score under each grader (Full = 1, Partial = 0.5,
      Incorrect = 0), to check whether either grader favors particular models
    - every disagreement, with both graders' justifications
"""

import argparse
import json
import os
from collections import Counter

from config import QUESTION_BANK
from questions import load_questions

GRADES = ("Full", "Partial", "Incorrect")
SCORE = {"Full": 1.0, "Partial": 0.5, "Incorrect": 0.0}


def load(run_dir, grader):
    path = os.path.join(run_dir, f"grades_{grader}.jsonl")
    with open(path, encoding="utf-8") as f:
        records = [json.loads(line) for line in f if line.strip()]
    return {(g["label"], g["question_id"]): g for g in records}


def cohens_kappa(pairs):
    """Agreement between two graders, corrected for agreement expected by chance."""
    n = len(pairs)
    observed = sum(a == b for a, b in pairs) / n
    count_a = Counter(a for a, _ in pairs)
    count_b = Counter(b for _, b in pairs)
    expected = sum(count_a[g] * count_b[g] for g in GRADES) / n ** 2
    return (observed - expected) / (1 - expected) if expected < 1 else 1.0


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("run_dir", help="results folder, e.g. results/run1")
    parser.add_argument("grader1", help="first grader label")
    parser.add_argument("grader2", help="second grader label")
    args = parser.parse_args()

    g1, g2 = load(args.run_dir, args.grader1), load(args.run_dir, args.grader2)
    keys = sorted(set(g1) & set(g2), key=lambda k: (k[0], int(k[1][1:])))
    current = {q["id"] for q in load_questions(QUESTION_BANK)}  # excludes retired questions
    keys = [k for k in keys if k[1] in current
            and g1[k]["grade"] in GRADES and g2[k]["grade"] in GRADES]
    if not keys:
        raise SystemExit("No answers graded by both graders.")
    pairs = [(g1[k]["grade"], g2[k]["grade"]) for k in keys]

    agree = sum(a == b for a, b in pairs)
    extreme = sum({a, b} in ({"Full", "Incorrect"},) for a, b in pairs)
    lines = [f"# Grader comparison: {args.grader1} vs. {args.grader2}", "",
             f"Answers graded by both: {len(pairs)}", "",
             f"- Same grade: {agree} ({agree / len(pairs):.0%})",
             f"- Cohen's kappa: {cohens_kappa(pairs):.2f}",
             f"- Full vs. Incorrect (largest disagreements): {extreme}", "",
             "## Grade pairs", "",
             f"Rows: {args.grader1}. Columns: {args.grader2}.", "",
             "| | " + " | ".join(GRADES) + " |", "|---|" + "---|" * len(GRADES)]
    pair_counts = Counter(pairs)
    for a in GRADES:
        lines.append(f"| {a} | " + " | ".join(str(pair_counts[(a, b)]) for b in GRADES) + " |")

    lines += ["", "## Average score by model", "",
              "Full = 1, Partial = 0.5, Incorrect = 0.", "",
              f"| Model | {args.grader1} | {args.grader2} | Difference |", "|---|---|---|---|"]
    for label in sorted({k[0] for k in keys}):
        ks = [k for k in keys if k[0] == label]
        s1 = sum(SCORE[g1[k]["grade"]] for k in ks) / len(ks)
        s2 = sum(SCORE[g2[k]["grade"]] for k in ks) / len(ks)
        lines.append(f"| {label} | {s1:.2f} | {s2:.2f} | {s1 - s2:+.2f} |")

    lines += ["", "## Disagreements", ""]
    for k in keys:
        a, b = g1[k]["grade"], g2[k]["grade"]
        if a != b:
            lines += [f"### {k[1]}, {k[0]}: {a} vs. {b}", "",
                      f"**{args.grader1}:** {g1[k]['justification']}", "",
                      f"**{args.grader2}:** {g2[k]['justification']}", ""]

    out_path = os.path.join(args.run_dir, f"comparison_{args.grader1}_vs_{args.grader2}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines[:8]))
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
