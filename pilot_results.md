# Pilot Results

## Purpose

Before building an automated evaluation pipeline, the question bank was tested by hand on two chat models to check that the questions are clearly worded, that the rubrics can be applied consistently, and that difficulty increases across the four tiers.

## Method

- **Date:** October 21, 2026.
- **Models:** ChatGPT and Gemini, each using the default model in its consumer chat interface. Exact model versions were not recorded.
- **Setup:** Questions were submitted without rubrics or sources. ChatGPT was run in a temporary, unpersonalized chat so that saved memories and custom instructions did not influence answers. Web search was intended to be disabled; an initial ChatGPT answer to Q17 that used web search was excluded.
- **Sessions:** All questions for each model were asked in a single chat session. Because earlier prompts can provide context for later questions (for example, Q8 and Q14 state that the food waste carbon contains inorganic species, which bears on Q17), Q17 was intended to be asked first. ChatGPT answered the Tier 4 questions in a separate session after those questions were revised.
- **Grading:** Each answer was graded Full, Partial, or Incorrect according to the scoring definitions in `question_bank.md`. Draft grades were prepared with LLM assistance and reviewed by the author.

## Results by question

| Q | Tier | ChatGPT | Gemini | Notes |
|---|---|---|---|---|
| 1 | 1 | Partial | Full | ChatGPT described Cu<sup>+</sup> as having a partially filled valence shell (it is 3d<sup>10</sup>). |
| 2 | 1 | Full | Full | |
| 3 | 1 | Full | Full | |
| 4 | 1 | Partial | Full | ChatGPT did not explain why Cu<sup>2+</sup> (3d<sup>9</sup>) is a poor π back-donor. |
| 5 | 1 | Full | Full | |
| 6 | 1 | Full | Full | |
| 7 | 1 | Full | Full | |
| 8 | 1 | Full | Partial | Gemini stated that the elements are present only as particles and that they enhance capacity, without support. |
| 9 | 2 | Partial | Full | ChatGPT did not state that Ce preferentially occupies inaccessible interior sites. |
| 10 | 2 | Partial | Partial | ChatGPT listed cation siting among several possibilities; Gemini asserted an unestablished Ce redox mechanism. |
| 11 | 2 | Full | Full | |
| 12 | 2 | Partial | Partial | Neither model attributed the slope difference specifically to the metal sites or separated curve shape from capacity. |
| 13 | 2 | Full | Full | Both noted the concentration difference between aromatics and sulfur compounds without prompting. |
| 14 | 2 | Full | Partial | Gemini claimed that naphthalene does not compete for adsorption on activated carbon. |
| 15 | 3 | Full | Incorrect | Gemini inferred specific oxidation-state changes, and the absence of Cu<sup>0</sup>, from XRD data alone. |
| 16 | 3 | Incorrect | Full | ChatGPT extrapolated the activation trend and predicted an initial increase. |
| 17 | 3 | Full | Incorrect | Gemini predicted negligible inorganic content after washing. |
| 18 | 3 | Partial | Incorrect | Both favored mesopore volume; Gemini identified it as the cause with confidence. |
| 19 | 3 | Incorrect | Incorrect | Both treated the Rietveld site assignment as excluding a direct Ce contribution. |
| 20 | 3 | Partial | Full | ChatGPT treated graphitization as favorable for adsorption. |
| 21 | 4 | Partial | Full | ChatGPT suggested Cu<sup>0</sup> clusters may add binding sites and did not commit to an effect. |
| 22 | 4 | Partial | Partial | Neither noted that measured Cu decreased as Ce loading increased. |
| 23 | 4 | Partial | Incorrect | Gemini concluded that adsorption is reversible; ChatGPT used the same term but noted that strength is not established. |
| 24 | 4 | Partial | Partial | Neither concluded from the chromatogram that early breakthrough reflects mass transfer limitations. |
| 25 | 4 | Full | Full | |

## Summary

| Tier | ChatGPT (Full / Partial / Incorrect) | Gemini (Full / Partial / Incorrect) |
|---|---|---|
| 1 | 6 / 2 / 0 | 7 / 1 / 0 |
| 2 | 3 / 3 / 0 | 3 / 3 / 0 |
| 3 | 2 / 2 / 2 | 2 / 0 / 4 |
| 4 | 1 / 4 / 0 | 2 / 2 / 1 |
| **Total** | **12 / 11 / 2** | **14 / 6 / 5** |

## Findings

1. **Difficulty increases with tier.** Both models answered most Tier 1 questions fully and performed worst on Tiers 3 and 4.
2. **The models fail in different ways.** ChatGPT tended to list several possible explanations without committing to one, producing mostly partial credit. Gemini tended to commit to a single answer, which produced outright errors on questions designed to invite a plausible but incorrect conclusion.
3. **Tier 3 questions discriminate well.** Q19 was failed by both models, and Q17 was failed by Gemini even though earlier questions in the same session had stated the relevant facts.
4. **Revising Tier 4 increased difficulty.** On an earlier version of the Tier 4 questions, which stated the anomaly or signaled the expected conclusion, ChatGPT received full credit on four of five questions. After revision, it received full credit on one of five.

## Revisions made during the pilot

- Added scoring definitions, including partial credit for answers that list the correct explanation among several without identifying it as the most likely.
- Revised Tier 4 prompts to remove statements of the anomaly and leading framing.
- Replaced Q25 with a question that presents a clearer anomaly.
- Expanded the Q15 rubric to mark any oxidation-state conclusion drawn from XRD as incorrect.

## Limitations

- Each model was tested once, in a single session, so results may vary between runs.
- Questions were not submitted independently, and model versions were not recorded.
- Grading was performed by a single reviewer with LLM assistance.

These limitations will be addressed by the automated evaluation, which will submit each question independently through model APIs with recorded model versions.
