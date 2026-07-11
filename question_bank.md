# LLM Reasoning Benchmark: Question Bank

*Adsorptive Desulfurization — Zeolites, Activated Carbon, Ion-Exchanged Sorbents*

## Overview

This question bank tests whether large language models genuinely reason through the mechanistic chemistry of sorbent-based sulfur removal, or are pattern-matching on surface-level associations between metals, materials, and sulfur compounds. Questions progress across four tiers of increasing difficulty, from basic mechanism identification to diagnostic reasoning about counterintuitive experimental findings.

Each question includes a scoring rubric (the specific points a correct answer must address) and a source (the paper/chapter the ground truth is drawn from). Ground truth for Tiers 1–3 is drawn primarily from dissertation research on adsorptive desulfurization; Tier 4 questions should be cross-checked against the broader literature before finalizing, since they hinge on findings that are more easily contested.

## Target Question Counts by Tier

| Tier | Focus | Target # Questions |
|---|---|---|
| Tier 1 | Mechanism identification — name and justify the dominant adsorption mechanism for a given sorbent/contaminant pair | 12–15 |
| Tier 2 | Comparative reasoning — predict and justify relative performance between two sorbents | 12–15 |
| Tier 3 | Counterfactual / edge cases — test whether trends from adjacent processes (e.g. HDS) are wrongly over-generalized | 10–12 |
| Tier 4 | Diagnostic / anomaly explanation — explain a real, counterintuitive experimental result | 8–12 |

*Total target: 40–60 questions. Prioritize question quality and unambiguous ground truth over hitting the top of each range — a smaller set of airtight questions is more valuable than a larger set with contestable answers.*

---

## Tier 1 — Mechanism Identification

Goal: establish a baseline. Can the model correctly name and explain the primary adsorption mechanism at play, including the correct oxidation state / electronic explanation, not just the correct material name?

**Q1.** CuY zeolite is exposed to dibenzothiophene (DBT). What is the primary adsorption mechanism, and why does Cu specifically enable it?
- **Rubric:** Mentions π-complexation; identifies Cu⁺ (not Cu²⁺ or Cu⁰) as the active oxidation state; mentions back-donation into the thiophene ring.
- **Source:** Dissertation Ch. [X] — CuY mechanism study

**Q2.** NaY zeolite shows much weaker sulfur adsorption than CuY for the same feed. Explain the mechanistic difference.
- **Rubric:** Identifies NaY as relying on weaker electrostatic / van der Waals interactions vs. CuY's specific π-complexation via Cu⁺.
- **Source:** Dissertation Ch. [X] — comparative ion-exchange study

**Q3.** Why is the Ce³⁺ oxidation state relevant to the adsorption behavior of CeY zeolite, and how does this differ mechanistically from Cu-based adsorption?
- **Rubric:** Distinguishes Ce's redox / Lewis-acid behavior from Cu's π-complexation pathway; does not conflate the two mechanisms.
- **Source:** Publication [Y] — CeY characterization

*[Add remaining Tier 1 questions here — target 12–15 total]*

---

## Tier 2 — Comparative Reasoning

Goal: test whether the model can predict relative performance between two sorbents and justify it using the correct structure-property relationship, not just a general sense of which metal "sounds" more reactive.

**Q4.** Would you expect CuY or CeY to bind 4,6-dimethyldibenzothiophene (DMDBT) more strongly? Justify your answer using the underlying adsorption mechanism, not just the empirical trend.
- **Rubric:** Correctly favors CuY; justification is grounded in relative π-complexation strength, not a generic "metals bind sulfur" claim.
- **Source:** Dissertation Ch. [X] — DMDBT comparative binding data

**Q5.** A CuCeY mixed zeolite outperforms both CuY and CeY individually for DMDBT adsorption. Propose a mechanistic explanation for this synergy.
- **Rubric:** Proposes a genuine synergy mechanism (e.g. combined/complementary active sites) rather than simply averaging the two known individual mechanisms.
- **Source:** Publication [Y] — CuCeY synergy finding (−249 kJ/mol result)

**Q6.** Rank NaY, CuY, and FWAC (food-waste-derived activated carbon) by expected DBT adsorption capacity. Briefly justify the ranking.
- **Rubric:** Produces a ranking consistent with mechanism (chemical selectivity vs. physical surface area) and gives distinct justification for each material, not just a repeated template.
- **Source:** Dissertation Ch. [X] — cross-material comparison

*[Add remaining Tier 2 questions here — target 12–15 total]*

---

## Tier 3 — Counterfactual / Edge Cases

Goal: catch superficial pattern-matching. These questions test whether the model wrongly generalizes a trend from an adjacent or superficially similar process, rather than reasoning from the actual mechanism at hand.

**Q7.** In hydrodesulfurization (HDS), 4,6-DMDBT is notoriously difficult to remove due to steric hindrance from its methyl groups blocking catalytic sites. Would you expect the same steric difficulty to apply to adsorptive desulfurization on CuY zeolite? Why or why not?
- **Rubric:** Correctly identifies that π-complexation adsorption is less sterically sensitive than HDS's catalytic site geometry; does not simply transfer the HDS trend uncritically.
- **Source:** Dissertation Ch. [X] — DMDBT adsorption vs. HDS literature comparison

**Q8.** A colleague claims that increasing Cu loading in CuY zeolite will always increase sulfur adsorption capacity. Is this claim correct? What factors could cause it to break down at high loading?
- **Rubric:** Identifies at least one real limiting factor: pore blockage, loss of accessible active sites, or Cu clustering/aggregation at high loading. Does not simply affirm "more active sites = more capacity" without qualification.
- **Source:** Dissertation Ch. [X] — Cu loading study

**Q9.** Higher total BET surface area is often assumed to predict better sulfur adsorption. Give a scenario from ion-exchanged zeolite chemistry where this assumption fails.
- **Rubric:** Provides a case where accessible/micropore surface area, pore size compatibility with the target molecule, or active-site chemistry outweighs raw total surface area.
- **Source:** Dissertation Ch. [X] — pore structure vs. capacity discussion

*[Add remaining Tier 3 questions here — target 10–12 total]*

---

## Tier 4 — Diagnostic / Anomaly Explanation

Goal: the hardest tier. Present a real, validated experimental finding that runs counter to naive expectation, and ask the model to explain it. There is no shortcut answer — the model must reason from mechanism to explain the anomaly. Cross-check each of these against the wider literature before finalizing, since contested science makes for a bad ground truth.

**Q10.** A food-waste-derived activated carbon (FWAC) with no specific metal active sites outperformed ion-exchanged Y zeolites (including CuY and CeY) in DMDBT adsorption capacity, despite the zeolites having mechanistically "smarter" sulfur-selective sites. Propose an explanation.
- **Rubric:** Invokes surface area / pore volume as a competing factor to selective chemical interaction; recognizes physical adsorption capacity can outweigh chemical selectivity for this contaminant; proposes an actual mechanism rather than restating the question.
- **Source:** Publication [Y] — FWAC vs. zeolite comparative finding

**Q11.** Two sorbents have identical BET surface area, but one has significantly higher micropore volume. Which would you predict performs better for DMDBT adsorption specifically, and why does pore size — not just total surface area — matter for this particular sulfur compound?
- **Rubric:** Connects DMDBT's molecular size to the need for appropriately sized micropores; distinguishes accessible surface area from total surface area.
- **Source:** Dissertation Ch. [X] — pore size / molecular size discussion

**Q12.** Explain why in-situ XAFS measurements were necessary to determine Cu oxidation state in CuY zeolite under operating conditions, rather than relying on ex-situ characterization alone.
- **Rubric:** Notes that oxidation state can change under reaction conditions (redox-active Cu⁺/Cu⁰), so ex-situ measurement risks capturing an artifact rather than the true operating-state structure.
- **Source:** Publication [Y] — in-situ XAFS methodology

*[Add remaining Tier 4 questions here — target 8–12 total]*

---

## Next Steps

- Fill in remaining questions per tier using specific results from the dissertation and related publications.
- For Tier 4 in particular, do a targeted literature check to confirm each "anomaly" is settled science, not a contested finding.
- Once questions are drafted, hand-test 10–15 in a chat interface before building the automated harness.
- Replace bracketed [X] / [Y] source placeholders with specific chapter/paper citations.
