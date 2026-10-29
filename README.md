# llm-desulfurization-eval

A reproducible benchmark that tests whether large language models understand the mechanistic chemistry of sorbent-based sulfur removal from liquid fuels (metal-exchanged zeolites, activated carbons), or whether they rely on surface-level associations between metals, materials, and sulfur compounds. The aim is a useful resource for materials scientists and practitioners deciding whether to trust LLM output on domain-specific reasoning.

## Why this matters

LLMs are increasingly used as research assistants for literature review, hypothesis generation, and data interpretation. General chemistry and materials science benchmarks such as ChemBench [1] and MatSciBench [2] measure broad knowledge and reasoning across many topics. To our knowledge, no benchmark focuses on adsorptive desulfurization, where correct answers often depend on reasoning about adsorption mechanisms, cation siting, porosity, and characterization limits rather than on recalling facts. This project maps where models are reliable in this area and where they give confident but incorrect answers.

## Contents

- `question_bank.md`: 24 benchmark questions in four tiers of increasing difficulty, each with a scoring rubric and source, plus one retired question.
- `pilot_results.md`: results of a hand-run pilot on two chat models, used to check question wording, rubrics, and difficulty.

## Status

- **Question bank:** complete (24 questions, one retired after the first run), reviewed by a domain expert.
- **Pilot:** complete. Both models tested (ChatGPT and Gemini) answered most fundamentals questions correctly and performed worst on Tiers 3 and 4. They failed in different ways: one tended to list several explanations without committing, the other committed confidently to plausible but incorrect conclusions. See `pilot_results.md`.
- **Automated evaluation harness:** in progress. It will submit each question independently to several models through their APIs, record model versions, and grade answers against the rubrics.

## License

- Questions, rubrics, and documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Code is licensed under the MIT License (see `LICENSE`).

## References

1. Mirza, A. et al. A framework for evaluating the chemical knowledge and reasoning abilities of large language models against the expertise of chemists. *Nat. Chem.* **2025**, 17. https://doi.org/10.1038/s41557-025-01815-x
2. Zhang, J. et al. MatSciBench: Benchmarking the Reasoning Ability of Large Language Models in Materials Science. arXiv:2510.12171 (2025).
