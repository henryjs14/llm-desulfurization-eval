# LLM Reasoning Benchmark: Question Bank

*Adsorptive Desulfurization — Zeolites, Activated Carbon, Ion-Exchanged Sorbents*

## Overview

This question bank tests whether large language models genuinely reason through the mechanistic chemistry of sorbent-based sulfur removal, or are pattern-matching on surface-level associations between metals, materials, and sulfur compounds. Questions progress across four tiers of increasing difficulty, from basic mechanism identification to diagnostic reasoning about counterintuitive experimental findings.

Each question includes a scoring rubric (the specific points a correct answer must address) and a source (the paper/chapter the ground truth is drawn from). Ground truth for Tiers 1–3 is drawn primarily from dissertation research on adsorptive desulfurization; Tier 4 questions should be cross-checked against the broader literature before finalizing, since they hinge on findings that are more easily contested.

**Status note:** Tier 1 and Tier 2 questions below are first-pass candidates — review, edit, and add to these directly, since they draw on mechanistic understanding you know firsthand. Tier 3 and Tier 4 questions have been drafted/expanded from specific dissertation findings (with real citations) as a starting point for your review.

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
- **Source:** Dissertation, Ch. 3 (CuY/CeY/CuCeY XAFS/DFT structural study)

**Q2.** NaY zeolite shows much weaker sulfur adsorption than CuY for the same feed. Explain the mechanistic difference.
- **Rubric:** Identifies NaY as relying on weaker electrostatic / van der Waals interactions vs. CuY's specific π-complexation via Cu⁺.
- **Source:** Dissertation, Ch. 3

**Q3.** Fresh (as-prepared) CuY zeolite begins with Cu in the +2 oxidation state. Describe what happens to the Cu oxidation state during the reduction process used to activate the sorbent, and why this matters for sulfur adsorption.
- **Rubric:** Correctly identifies Cu²⁺ → Cu⁺ (and potentially Cu⁰) transition during reduction; notes that Cu⁺ is the active π-complexation site, so under-reduced or over-reduced samples adsorb sulfur less effectively.
- **Source:** Dissertation, Ch. 3, §4.3.6 (Cu K-edge XANES reduction data)

**Q4.** Why is the Ce³⁺ oxidation state relevant to the adsorption behavior of CeY zeolite, and how does this differ mechanistically from Cu-based adsorption?
- **Rubric:** Distinguishes Ce's redox/Lewis-acid behavior from Cu's π-complexation pathway; notes Ce migrates from Ce⁴⁺ toward Ce³⁺ during reduction; does not conflate the two mechanisms.
- **Source:** Dissertation, Ch. 3, §4.3.5–4.3.6

*[Add remaining Tier 1 questions here — target 12–15 total]*

---

## Tier 2 — Comparative Reasoning

Goal: test whether the model can predict relative performance between two sorbents and justify it using the correct structure-property relationship, not just a general sense of which metal "sounds" more reactive.

**Q5.** Would you expect CuY or CeY to bind 4,6-dimethyldibenzothiophene (DMDBT) more strongly? Justify your answer using the underlying adsorption mechanism, not just the empirical trend.
- **Rubric:** Correctly favors CuY; justification is grounded in relative π-complexation strength, not a generic "metals bind sulfur" claim.
- **Source:** Dissertation, Ch. 2–3 (comparative binding data)

**Q6.** A CuCeY mixed zeolite outperforms both CuY and CeY individually for DMDBT adsorption. Propose a mechanistic explanation for this synergy.
- **Rubric:** Proposes a genuine synergy mechanism (e.g. combined/complementary active sites) rather than simply averaging the two known individual mechanisms.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (CuCeY synergy finding)

**Q7.** Rank NaY, CuY, and FWAC (food-waste-derived activated carbon) by expected DBT adsorption capacity. Briefly justify the ranking.
- **Rubric:** Produces a ranking consistent with mechanism (chemical selectivity vs. physical surface area) and gives distinct justification for each material, not just a repeated template.
- **Source:** Dissertation, Ch. 6, §6.4 (cross-material comparison, Figure 49)

**Q8.** DFT calculations show the average Ce–T (Ce-to-framework) distance in Y zeolite is longer (~3.3 Å) than the corresponding Cu–T distance, with Ce positioned slightly elevated out of the plane of the six-membered ring. What does this structural difference suggest about the relative steric accessibility of Ce versus Cu active sites for adsorption?
- **Rubric:** Correctly connects the elevated, longer-distance Ce position to reduced steric hindrance / greater accessibility for incoming sulfur molecules, relative to Cu.
- **Source:** Dissertation, Ch. 3, §3.2 (DFT structural comparison)

*[Add remaining Tier 2 questions here — target 12–15 total]*

---

## Tier 3 — Counterfactual / Edge Cases

Goal: catch superficial pattern-matching. These questions test whether the model wrongly generalizes a trend from an adjacent or superficially similar process, rather than reasoning from the actual mechanism at hand.

**Q9.** In hydrodesulfurization (HDS), 4,6-DMDBT is notoriously difficult to remove due to steric hindrance from its methyl groups blocking catalytic sites. Would you expect the same steric difficulty to apply to adsorptive desulfurization on CuY zeolite? Why or why not?
- **Rubric:** Correctly identifies that π-complexation adsorption is less sterically sensitive than HDS's catalytic site geometry; does not simply transfer the HDS trend uncritically.
- **Source:** Dissertation, Ch. 2 (ADS vs. HDS mechanism comparison)

**Q10.** A colleague claims that increasing Cu loading in CuY zeolite will always increase sulfur adsorption capacity. Is this claim correct? What factors could cause it to break down at high loading?
- **Rubric:** Identifies at least one real limiting factor: pore blockage, loss of accessible active sites, or Cu clustering/aggregation at high loading. Does not simply affirm "more active sites = more capacity" without qualification.
- **Source:** Dissertation, Ch. 3–4; Zu et al., *Chem. Eng. J.* 2020, 380, 122319 (Cu/Al ratio effects)

**Q11.** Higher total BET surface area is often assumed to predict better sulfur adsorption capacity. Using the comparison between FWAC and commercial activated carbon (CAC) as an example, explain a case where this assumption fails.
- **Rubric:** Correctly notes that FWAC and CAC have comparable total surface areas, yet FWAC substantially outperforms CAC — meaning surface area alone is not predictive; should invoke pore size distribution, micropore volume, or chemisorption from inorganic impurities as the actual differentiator.
- **Source:** Dissertation, Ch. 6, §6.4, Figure 49; *ACS Omega* 2025, 10, 42725–42734

**Q12.** Would you expect naphthalene (a competing aromatic present in real fuels) to adsorb onto activated carbon via the same mechanism proposed for sulfur compounds like DBT (π–π stacking with the graphite face)? What problem does this raise for AC-based desulfurization selectivity?
- **Rubric:** Recognizes that if π–π stacking were the dominant mechanism, naphthalene would compete for the same sites, reducing sulfur selectivity — correctly identifies this as a real limitation noted in the literature, motivating alternative explanations (e.g., inorganic impurity chemisorption) for AC's sulfur selectivity.
- **Source:** Dissertation, Ch. 6, §6.4; *ACS Omega* 2025, 10, 42725–42734 (π–π stacking selectivity discussion)

*[Add remaining Tier 3 questions here — target 10–12 total]*

---

## Tier 4 — Diagnostic / Anomaly Explanation

Goal: the hardest tier. Present a real, validated experimental finding that runs counter to naive expectation, and ask the model to explain it. There is no shortcut answer — the model must reason from mechanism to explain the anomaly. Cross-check each of these against the wider literature before finalizing, since contested science makes for a bad ground truth.

**Q13.** A food-waste-derived activated carbon (FWAC25) with no specific metal active sites outperformed ion-exchanged Y zeolites (including CuY and CeY) in DMDBT adsorption capacity, despite the zeolites having mechanistically "smarter" sulfur-selective sites. Propose an explanation.
- **Rubric:** Invokes pore volume / micropore accessibility as a competing factor to selective chemical interaction; recognizes physical adsorption capacity can outweigh chemical selectivity for this contaminant; proposes an actual mechanism rather than restating the question.
- **Source:** Dissertation, Ch. 6, §6.4, Figure 49

**Q14.** FWAC25 and commercial activated carbon (CAC) have similar total surface areas (896 vs. 918 m²/g), yet FWAC25's sulfur capacity is dramatically higher than CAC's for both DBT and DMDBT. What specific structural and compositional differences between FWAC25 and CAC explain this gap?
- **Rubric:** Should identify (a) FWAC25 has substantially higher micropore volume relative to its mesopore volume than CAC (which is largely mesoporous), and micropores below ~10 Å are especially important since they match the ~9 Å molecular diameter of DBT/DMDBT; (b) FWAC25 contains Na, Ca, K, and P inorganic impurities largely absent or minimal in CAC, which are proposed to act as chemisorption sites for sulfur.
- **Source:** Dissertation, Ch. 6, §6.3.3, §6.4, Table 20; *ACS Omega* 2025, 10, 42725–42734

**Q15.** Within the FWAC series, sulfur adsorption capacity increased linearly with micropore volume — but total surface area alone did not predict capacity as cleanly. Explain why micropore volume specifically, rather than total surface area, is the better predictor for this system.
- **Rubric:** Connects the ~9 Å molecular diameter of DBT/DMDBT to the need for micropores smaller than ~10 Å; explains that mesopores or macropores contributing to "total surface area" don't provide the same size-matched confinement for physisorption.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50

**Q16.** Explain why in-situ XAFS measurements were necessary to determine Cu and Ce oxidation states in CuY/CeY zeolites under operating (reduced) conditions, rather than relying on ex-situ characterization of the as-prepared material alone.
- **Rubric:** Notes that oxidation state changes under reducing conditions (Cu²⁺→Cu⁺, Ce⁴⁺→Ce³⁺), so characterizing only the fresh, unreduced material would not reflect the true active-state structure responsible for sulfur adsorption.
- **Source:** Dissertation, Ch. 3, §3.4–4.3.6

**Q17.** In situ XRD of CuY, CeY, and CuCeY showed no significant peaks attributable to crystalline Cu or Ce metal/oxide phases, even though XANES confirmed clear oxidation-state changes were occurring in these same materials. How can both of these observations be true simultaneously?
- **Rubric:** Recognizes that XRD is sensitive to long-range crystalline order and would miss well-dispersed, highly disordered, or sub-nanometer metal species; XANES is a local, element-specific probe sensitive to oxidation state regardless of crystallinity — so the absence of XRD peaks indicates the metals are atomically/well-dispersed rather than forming bulk crystalline clusters, not that no chemical change occurred.
- **Source:** Dissertation, Ch. 3, §3.3–3.4

*[Add remaining Tier 4 questions here — target 8–12 total]*

---

## Next Steps

- Fill in remaining Tier 1 and Tier 2 questions — these draw on mechanistic understanding you know firsthand and are worth drafting/reviewing closely yourself.
- Review and revise the Tier 3/4 candidates above — treat them as a rough first pass to correct and sharpen, not a final answer to approve as-is.
- For Tier 4 in particular, do a targeted literature check to confirm each "anomaly" is settled science, not a contested finding.
- Once questions are finalized, hand-test 10–15 in a chat interface before building the automated harness.
