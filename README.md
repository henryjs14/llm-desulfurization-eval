# llm-desulfurization-eval

A rigorous, reproducible benchmark that tests whether large language models genuinely understand the mechanistic chemistry of sorbent-based sulfur removal (zeolites, activated carbons) or are just pattern-matching on surface-level associations. The goal is a genuinely useful resource for materials scientists and practitioners deciding whether to trust LLM output on domain-specific reasoning, backed by a reproducible methodology.

## Why this matters

LLMs are increasingly used as research assistants for literature review, hypothesis generation, and data interpretation. Nobody has rigorously mapped out *where* they're reliable versus *where* they confidently give wrong answers in adsorptive desulfurization / porous materials chemistry specifically. This project answers that question with evidence.

## Contents

- `question_bank.md`: benchmark questions in four tiers of increasing difficulty, each with a scoring rubric and source.
