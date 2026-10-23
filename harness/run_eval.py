"""Send every question to every model and save the raw answers.

Usage (from the repository root):
    python harness/run_eval.py                      # all models, all questions
    python harness/run_eval.py --models gpt-6-luna  # selected models (by label)
    python harness/run_eval.py --questions Q1 Q2    # selected questions
    python harness/run_eval.py --dry-run            # show what would be sent

Answers are written to results/<run-id>/responses.jsonl, one line per answer.
If a run is interrupted, running the same command again skips answers that were
already saved.
"""

import argparse
import json
import os
from datetime import datetime, timezone

from dotenv import load_dotenv

from clients import ask
from config import MODELS, QUESTION_BANK, RESULTS_DIR
from questions import load_questions


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--models", nargs="+",
                        help="model labels to test (default: all in config.py)")
    parser.add_argument("--questions", nargs="+", help="question IDs, e.g. Q1 Q17")
    parser.add_argument("--run-id", default=datetime.now().strftime("%Y-%m-%d"),
                        help="name of the results folder (default: today's date)")
    parser.add_argument("--dry-run", action="store_true",
                        help="print the prompts without calling any API")
    args = parser.parse_args()

    load_dotenv()
    models = MODELS
    if args.models:
        unknown = set(args.models) - {label for label, _, _ in MODELS}
        if unknown:
            parser.error(f"unknown model label(s): {', '.join(sorted(unknown))}")
        models = [m for m in MODELS if m[0] in args.models]
    questions = load_questions(QUESTION_BANK)
    if args.questions:
        wanted = {q.upper() for q in args.questions}
        questions = [q for q in questions if q["id"] in wanted]

    if args.dry_run:
        for q in questions:
            print(f"--- {q['id']} (Tier {q['tier']}) ---\n{q['prompt']}\n")
        print(f"{len(questions)} questions x {len(models)} models "
              f"= {len(questions) * len(models)} API calls")
        return

    run_dir = os.path.join(RESULTS_DIR, args.run_id)
    os.makedirs(run_dir, exist_ok=True)
    out_path = os.path.join(run_dir, "responses.jsonl")

    done = set()
    if os.path.exists(out_path):
        with open(out_path, encoding="utf-8") as f:
            for line in f:
                record = json.loads(line)
                done.add((record["label"], record["question_id"]))

    with open(out_path, "a", encoding="utf-8") as out:
        for label, provider, model in models:
            print(f"\n{label}")
            for q in questions:
                if (label, q["id"]) in done:
                    print(f"  {q['id']}: already saved, skipping")
                    continue
                print(f"  {q['id']}: asking...")
                try:
                    answer = ask(provider, model, q["prompt"])
                except Exception as error:
                    print(f"  {q['id']}: FAILED ({error})")
                    continue
                record = {
                    "question_id": q["id"],
                    "tier": q["tier"],
                    "label": label,
                    "provider": provider,
                    "model_requested": model,
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    **answer,
                }
                out.write(json.dumps(record, ensure_ascii=False) + "\n")
                out.flush()
                if answer["truncated"]:
                    print(f"  {q['id']}: WARNING answer was cut off at the token limit")

    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
