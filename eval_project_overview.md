# Project Overview: LLM Reasoning Benchmark for Adsorptive Desulfurization

## Aim

Build a rigorous, reproducible benchmark that tests whether large language models genuinely understand the mechanistic chemistry of sorbent-based sulfur removal (zeolites, activated carbons, ion-exchanged materials) or are just pattern-matching on surface-level associations. The goal is a genuinely useful resource for materials scientists and practitioners deciding whether to trust LLM output on domain-specific reasoning, backed by a reproducible methodology.

## Why this matters (the real question being answered)

LLMs are increasingly used as research assistants for literature review, hypothesis generation, and data interpretation. Nobody has rigorously mapped out *where* they're reliable versus *where* they confidently give wrong answers in adsorptive desulfurization / porous materials chemistry specifically. This project answers that question with evidence, not a vibe.

## What success looks like

- A test set of 40-60 well-posed questions, tiered by difficulty, each with a defensible rubric-based ground truth you can stand behind.
- An automated, reliable pipeline that runs the full test set against one or more models without manual babysitting, logs everything, and can be rerun cleanly.
- A validated scoring approach — you've checked that automated grading agrees with your own expert judgment closely enough to trust it.
- A clear, evidence-backed finding: e.g., "models reliably identify named mechanisms (Tier 1) but fail to reason about counterintuitive structure-performance anomalies (Tier 4), especially X and Y failure modes."
- A public GitHub repo with the questions, code, results, and a short written report, clean enough that another chemist or an eval engineer could both independently judge it as rigorous.

## Non-goals (to keep scope sane)

- Training or fine-tuning a model.
- Improving any company's model directly — this evaluates existing public models via API.
- A huge dataset (40-60 excellent questions beats 500 mediocre ones).
- A polished product — a clean script and a readable report are enough.

---

## Project Phases

### Phase 1 — Question design & ground truth (Weeks 1-2)
**Goal:** 40-60 questions across 4 tiers (mechanism ID → comparative reasoning → counterfactual → diagnostic anomaly), each with a written rubric.
**Output:** A spreadsheet or structured file: question text, tier, rubric points, source (which paper/finding it's grounded in).
**Check yourself:** For each question, could a reasonable expert (you, six months from now) disagree with your own rubric? If yes, revise until the correct answer is unambiguous.

### Phase 2 — Manual pilot (Week 2-3)
**Goal:** Hand-test 10-15 questions directly in a chat interface before writing any automation. Confirms questions are well-posed and gives you a feel for what model answers actually look like.
**Output:** A short note on any questions you rewrote or dropped, and why.

### Phase 3 — Build the automated harness (Weeks 3-5)
**Goal:** A script that sends each question to a model via API, saves the raw response, and stores it in a structured format (e.g., a CSV or small database) — question, answer, timestamp, model name, run ID.
**Reliability requirements:** handles API failures with retries, logs progress so you can see what happened on a run, can be safely re-run without duplicating or losing data.
**Output:** Working script + a results file from a full run across your test set.

### Phase 4 — Scoring & validation (Weeks 5-7)
**Goal:** Score model answers against your rubrics. Start by grading a subset yourself by hand. Then build or test an automated grader (e.g., a second LLM call scoring against your rubric) and check how often it agrees with your manual scores.
**Output:** A scored results file, plus a short validation note: "automated grader agreed with my manual scoring on X% of a 15-question sample."

### Phase 5 — Analysis (Weeks 7-9)
**Goal:** Look for patterns across tiers, question types, and failure modes. Where does the model do well? Where does it confidently fail? Is there a consistent kind of mistake (e.g., ignoring steric/mechanistic nuance in favor of a generic trend)?
**Output:** A findings summary — this is the actual "result" of the project.

### Phase 6 — Dashboard / visualization (Weeks 9-10)
**Goal:** A simple visual summary — score by tier, common failure categories, maybe a comparison across two different models if you have time/API budget.
**Output:** A chart or small Streamlit app / static HTML report.

### Phase 7 — Writeup & publish (Weeks 10-12)
**Goal:** Clean GitHub repo (questions, code, results, README) plus a short report (blog-post length is fine) explaining what you tested, what you found, and why it matters.
**Output:** A public, linkable portfolio piece.

---

## Example question (to anchor the abstraction)

**Question (Tier 4 — diagnostic):** A food-waste-derived activated carbon with no specific metal active sites outperformed ion-exchanged Y zeolites (including CuY and CeY) in DMDBT adsorption capacity, despite the zeolites having mechanistically "smarter" sulfur-selective sites. Propose an explanation.

**Rubric:**
- Mentions surface area / pore volume as a competing factor to selective chemical interaction
- Recognizes that physical adsorption capacity can outweigh chemical selectivity for this particular contaminant
- Does not simply restate the question without proposing a mechanism

**Why it's a good question:** There's no shortcut answer — a model has to either genuinely reason about competing adsorption mechanisms or guess, and the guess is usually distinguishable from real reasoning by what it omits.

## What "done" looks like at the end

A public, reproducible repo where the methodology, questions, and results are clear enough that another researcher could independently evaluate the findings, rerun the benchmark, or extend it to new materials systems. The core deliverable is a defensible, evidence-backed answer to the question: where do current LLMs reason reliably about sorbent-based desulfurization chemistry, and where do they fail?
