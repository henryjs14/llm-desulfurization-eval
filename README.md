# llm-desulfurization-eval

A reproducible benchmark that tests whether large language models understand the mechanistic chemistry of sorbent-based sulfur removal from liquid fuels (metal-exchanged zeolites, activated carbons), or whether they rely on surface-level associations between metals, materials, and sulfur compounds. The aim is a useful resource for materials scientists and practitioners deciding whether to trust LLM output on domain-specific reasoning.

## Why this matters

LLMs are increasingly used as research assistants for literature review, hypothesis generation, and data interpretation. General chemistry and materials science benchmarks such as ChemBench [1] and MatSciBench [2] measure broad knowledge and reasoning across many topics. To our knowledge, no benchmark focuses on adsorptive desulfurization, where correct answers often depend on reasoning about adsorption mechanisms, cation siting, porosity, and characterization limits rather than on recalling facts. This project maps where models are reliable in this area and where they give confident but incorrect answers.

## Contents

- `question_bank.md`: 24 benchmark questions in four tiers of increasing difficulty, each with a scoring rubric and source, plus one retired question.
- `harness/`: Python code that sends each question to each model, grades the answers against the rubrics with an LLM grader, and compares graders.
- `results/run1/`: answers, grades, and summaries from the first full run.
- `pilot_results.md`: results of a hand-run pilot on two chat models, used to check question wording, rubrics, and difficulty.

## Method

Each question was sent to each model as an independent API call, with no conversation history or web search, followed by the instruction "Answer in 400 words or fewer." Five models were tested in October 2026: gpt-6-astra, gpt-6.1-sol, and gpt-6-luna (OpenAI), gemini-4-argon (Google), and claude-fable-5-1 (Anthropic). No answers were cut off at the token limit.

Answers were graded as Full, Partial, or Incorrect against the rubrics in `question_bank.md` by two LLM graders from different providers: claude-opus-5-5 (Anthropic) and gpt-6.1-sol (OpenAI). Scores below use Full = 1, Partial = 0.5, and Incorrect = 0. A domain expert then graded a sample of answers blind to check the graders (see [Grader validation](#grader-validation)).

To reproduce the run, copy `.env.example` to `.env`, add API keys, and run from the repository root:

```bash
pip install -r requirements.txt
python harness/run_eval.py --run-id run1
python harness/grade.py results/run1 --grader claude-opus-5-5
python harness/grade.py results/run1 --grader gpt-6.1-sol
python harness/compare_grades.py results/run1 claude-opus-5-5 gpt-6.1-sol
```

## Results

### Scores by model

Average score over 24 questions (maximum 1.00).

| Model | claude-opus-5-5 grader | gpt-6.1-sol grader | Average answer length (words) |
|---|---|---|---|
| gemini-4-argon | 0.79 | 0.65 | 361 |
| claude-fable-5-1 | 0.77 | 0.65 | 373 |
| gpt-6-astra | 0.73 | 0.73 | 253 |
| gpt-6.1-sol | 0.69 | 0.67 | 248 |
| gpt-6-luna | 0.62 | 0.58 | 158 |

The ranking in the middle of the field depends on the grader. Two results hold under both: gpt-6-luna scores lowest, and gpt-6-astra receives the same score from both graders. The differences between the top four models are small relative to the difference between graders, so this run does not establish a clear leader.

### Scores by tier

| Tier | Focus | claude-opus-5-5 grader | gpt-6.1-sol grader |
|---|---|---|---|
| 1 | Mechanism and materials fundamentals | 0.90 | 0.75 |
| 2 | Comparative reasoning | 0.65 | 0.57 |
| 3 | Counterfactual and edge cases | 0.68 | 0.74 |
| 4 | Diagnostic and anomaly explanation | 0.56 | 0.52 |

Under both graders, Tier 1 is the easiest and Tier 4 the hardest. Tier 3 scored higher than Tier 2 under both graders, although it was designed to be harder; the gap is small under claude-opus-5-5 (0.03) and larger under gpt-6.1-sol (0.17).

### Where models fail

Most answers that lost credit were graded Partial: correct in direction but missing a required point or not committing to a conclusion. Answers that both graders marked Incorrect show the failure the benchmark is designed to detect, a confident conclusion that is plausible but wrong. Each rubric and its sources are given in `question_bank.md`.

- **Q9:** claude-fable-5-1 predicted that CeY binds benzothiophene more strongly than CuY, contrary to DFT adsorption enthalpies (−149 kJ/mol on CuY versus −126 kJ/mol on CeY) [3], and drew a general conclusion about rare-earth cations from it.
- **Q19:** claude-fable-5-1 concluded that Ce cannot contribute directly to DBT adsorption because a Rietveld refinement assigned it mainly to inaccessible sites, treating a site preference as strict exclusion [4, 5].
- **Q21:** gpt-6-luna argued that metallic Cu<sup>0</sup> clusters add sulfur adsorption sites, rather than recognizing that Cu reduced to Cu<sup>0</sup> is no longer available as Cu<sup>+</sup> for π-complexation [5].
- **Q23:** claude-fable-5-1 and gemini-4-argon concluded that because severe regeneration was needed, 4,6-DMDBT must be strongly adsorbed. In the source study, the sorbent recovered nearly all of its capacity after two cycles of calcination in air and reduction in H<sub>2</sub> [6]. Calcination combusts the adsorbed sulfur compounds and changes the oxidation state of the exchanged metals [7], and reduction restores the active sites, so the result gives no information about adsorption strength.

## Grader validation

### Agreement between graders

The two graders gave the same grade to 96 of 120 answers (80%), Cohen's kappa 0.65. They never disagreed by more than one grade (Full versus Incorrect). gpt-6.1-sol was the stricter grader: in 17 of the 24 disagreements, claude-opus-5-5 gave Full where gpt-6.1-sol gave Partial.

The graders disagreed most on the two models with the longest answers, gemini-4-argon and claude-fable-5-1, with score differences of 0.15 and 0.12. For the three OpenAI models the differences were 0.04 or less. Longer answers contain more supporting detail, and the scoring rules give Partial for a factual error in supporting detail, so a stricter grader finds more to mark down. Neither grader favored models from its own provider: gpt-6.1-sol graded its own answers 0.02 lower than claude-opus-5-5 did, and claude-opus-5-5 scored claude-fable-5-1 below gemini-4-argon.

### Agreement with expert grading

A domain expert (the author of the question bank, whose PhD research on sorbent-based desulfurization underlies many of the questions) graded 32 answers blind to model and grader: all 22 answers on which the graders disagreed after the answer key was revised, and 10 answers chosen at random (seed 2026) from those on which they agreed. Two answers were left ungraded because the expert judged the questions (Q20, Q22) too open-ended to grade those answers. Expert grades are in `results/run1/expert_grades.csv`.

| Grader | Same grade as expert (of 30) | Stricter than expert | More lenient than expert |
|---|---|---|---|
| claude-opus-5-5 | 23 (77%) | 7 | 0 |
| gpt-6.1-sol | 9 (30%) | 21 | 0 |

Both graders were stricter than the expert and never more lenient. claude-opus-5-5 was never more than one grade from the expert, so its scores, reported first above, are a conservative estimate of expert grading. gpt-6.1-sol differed from the expert by two grades (Incorrect versus Full) on three answers.

## Limitations

- **Expert sample.** One expert graded 30 answers, 22 of which were selected because the graders disagreed, so the sample overrepresents borderline answers. The rubrics for Q12, Q17, and Q19 were revised using these same answers, so the 77% agreement figure is likely optimistic. The expert graded 26 of the 30 answers as Full, which suggests that some questions are not difficult enough to separate current models.
- **Answer keys.** The rubrics were written by a single expert from selected publications and the expert's dissertation, and follow the interpretations given there. Where the literature is not settled, other researchers may accept answers the rubrics mark down. The rubrics were also revised during this run: requirements that the questions do not ask for were removed, and wording that led graders to penalize correct answers (Q12) or to rely on results not given in the question (Q17) was corrected. Grades under the earlier key are retained for comparison. Grader strictness depends closely on rubric wording, so further revisions could change scores.
- **Question specification.** The expert judged several questions open-ended enough that answers departing from the rubric were still defensible. Rubric requirements that a question does not ask for were removed before grading, but some questions would benefit from tighter wording.
- **One run.** Each model answered each question once. Model outputs vary between runs, and differences of a few hundredths in average score are within that variation.
- **Retired question.** Q18 was retired after run1 because its data cannot identify a single answer, so it tested whether a model declines to answer rather than its reasoning. Its answers and grades are kept in `results/run1/` but excluded from all scores (see `question_bank.md`).
- **Earlier grades.** `results/run1/grades_old_key.jsonl` and `summary_old_key.md` are grades from an earlier version of the answer key, kept for reference. `results/test` and `results/test2` are trial runs used to check the harness.

## License

- Questions, rubrics, and documentation are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
- Code is licensed under the MIT License (see `LICENSE`).

## References

1. Mirza, A. et al. A framework for evaluating the chemical knowledge and reasoning abilities of large language models against the expertise of chemists. *Nat. Chem.* **2025**, 17. https://doi.org/10.1038/s41557-025-01815-x
2. Zhang, J. et al. MatSciBench: Benchmarking the Reasoning Ability of Large Language Models in Materials Science. arXiv:2510.12171 (2025).
3. Sokol, H. J.; Lee, K. X.; Valla, J. A. The Mechanism of Adsorptive Desulfurization on Cu and Ce Exchanged Y Zeolite Using Density Functional Theory. *Comput. Mater. Sci.* **2024**, 235, 112813.
4. Lee, K. X.; Crowl, T. B.; Sokol, H. J.; Morales-Acosta, M. D.; Valla, J. A. Understanding the Role of Rare Earths in Zeolite Y on the Removal of Sulfur from Hydrocarbon Fuels. *J. Phys. Chem. C* **2021**, 125, 9107–9118.
5. Sokol, H. J.; Ebrahim, A. M.; Caratzoulas, S.; Frenkel, A. I.; Valla, J. A. In Situ XAFS, XRD, and DFT Characterization of the Sulfur Adsorption Sites on Cu and Ce Exchanged Y Zeolites. *J. Phys. Chem. C* **2022**, 126, 1496–1512.
6. Lee, K. X.; Wang, H.; Karakalos, S.; Tsilomelekis, G.; Valla, J. A. Adsorptive Desulfurization of 4,6-Dimethyldibenzothiophene on Bimetallic Mesoporous Y Zeolites: Effects of Cu and Ce Composition and Configuration. *Ind. Eng. Chem. Res.* **2019**, 58, 18301–18312.
7. Lee, K. X.; Valla, J. A. Adsorptive Desulfurization of Liquid Hydrocarbons Using Zeolite-Based Sorbents: A Comprehensive Review. *React. Chem. Eng.* **2019**, 4, 1357–1386.
