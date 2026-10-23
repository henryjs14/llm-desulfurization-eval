"""Read questions, rubrics, and scoring definitions from question_bank.md.

The question bank is the single source of truth: the harness parses it each time
it runs, so edits to the questions take effect without a separate data file.
"""

import re

SUP_FROM, SUP_TO = "0123456789+-−*", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻*"
SUB_FROM, SUB_TO = "0123456789", "₀₁₂₃₄₅₆₇₈₉"


def _convert_tag(text, tag, chars_from, chars_to, fallback):
    """Replace <sup>/<sub> tags with Unicode characters, or ^x / _x if none exist."""
    table = str.maketrans(chars_from, chars_to)

    def replace(match):
        inner = match.group(1).replace("\\*", "*")
        if all(c in chars_from for c in inner):
            return inner.translate(table)
        return f"{fallback}{inner}" if len(inner) == 1 else f"{fallback}({inner})"

    return re.sub(rf"<{tag}>(.*?)</{tag}>", replace, text)


def to_plain_text(text):
    """Convert the Markdown/HTML used in the question bank to readable plain text."""
    text = _convert_tag(text, "sup", SUP_FROM, SUP_TO, "^")
    text = _convert_tag(text, "sub", SUB_FROM, SUB_TO, "_")
    text = text.replace("\\*", "*")
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # bold
    text = re.sub(r"(?<![\w*])\*(\w[^*]*?)\*(?![\w*])", r"\1", text)  # italics
    return text.strip()


def load_questions(path):
    """Return a list of questions, each a dict with id, tier, prompt, rubric, source."""
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()

    questions = []
    tier = None
    current = None

    for line in lines:
        tier_match = re.match(r"## Tier (\d+)", line)
        if tier_match:
            tier = int(tier_match.group(1))
            continue
        if line.startswith("## "):  # any other section ends the questions
            tier = None
            continue
        if tier is None:
            continue

        q_match = re.match(r"\*\*Q(\d+)\.\*\*\s*(.*)", line)
        if q_match:
            current = {"id": f"Q{q_match.group(1)}", "tier": tier,
                       "prompt_lines": [q_match.group(2)], "rubric": "", "source": ""}
            questions.append(current)
        elif current is None:
            continue
        elif line.startswith("- **Rubric:**"):
            current["rubric"] = line.removeprefix("- **Rubric:**").strip()
        elif line.startswith("- **Source:**"):
            current["source"] = line.removeprefix("- **Source:**").strip()
            current = None
        else:
            current["prompt_lines"].append(line)

    for q in questions:
        q["prompt"] = to_plain_text("\n".join(q.pop("prompt_lines")))
        q["rubric"] = to_plain_text(q["rubric"])
    return questions


def load_scoring_definitions(path):
    """Return the text of the 'Scoring' section, used in the grader prompt."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    match = re.search(r"## Scoring\n(.*?)\n## ", text, re.S)
    if not match:
        raise ValueError("No '## Scoring' section found in the question bank.")
    return to_plain_text(match.group(1))
