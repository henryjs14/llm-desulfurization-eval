# LLM Reasoning Benchmark: Question Bank

*Adsorptive Desulfurization — Zeolites, Activated Carbon, Ion-Exchanged Sorbents*

## Overview

This question bank tests whether large language models genuinely reason through the mechanistic chemistry of sorbent-based sulfur removal, or are pattern-matching on surface-level associations between metals, materials, and sulfur compounds. Questions progress across four tiers of increasing difficulty, from basic mechanism identification to diagnostic reasoning about counterintuitive experimental findings.

Each question includes a scoring rubric (the specific points a correct answer must address) and a source. **This full draft was generated from the dissertation and related papers for review — treat every question, rubric, and citation as a first pass to verify, correct, and rewrite, not a final answer to approve as-is.** Page/section/table references should be checked against your own copies before finalizing, and Tier 4 findings in particular should be cross-checked against the wider literature.

**Design note — self-contained questions:** When these questions are actually run against a model via API, the model will NOT have your dissertation as context — it only sees the question text itself. Any dissertation-specific label or acronym (FWAC, SAY, CAC, etc.) needs to be briefly defined inline within the question, or the model is just guessing at what the term means. Check every question for this before finalizing, not just the ones flagged below.

**Terminology reference (for your use while editing — fold relevant definitions into question text itself):**
- **FWAC** — food waste-derived activated carbon (as opposed to conventional coal- or wood-derived activated carbon).
- **CAC** — commercial (conventional, non-food-waste-derived) activated carbon, used as a comparison baseline.
- **SAY** — Surfactant-Assisted Y, mesoporous Y zeolite prepared via a surfactant-assisted synthesis method (as opposed to conventional purely microporous Y).

## Question Counts by Tier

| Tier | Focus | Count in this draft |
|---|---|---|
| Tier 1 | Mechanism identification | 12 |
| Tier 2 | Comparative reasoning | 12 |
| Tier 3 | Counterfactual / edge cases | 9 (Q25 removed, needs replacement) |
| Tier 4 | Diagnostic / anomaly explanation | 4 solid (Q33–35, 38) + 2 flagged for rework (Q26, Q37) — needs substantial redrafting, per your note that you'll work on this tier directly |

**Total: 42 questions.** Trim, merge, or cut any that feel redundant or insufficiently rigorous once you review them — a smaller set of airtight questions beats a larger set with weak spots.

---

## Tier 1 — Mechanism Identification

Goal: establish a baseline. Can the model correctly name and explain the primary adsorption mechanism at play, including the correct oxidation state / electronic explanation, not just the correct material name?

**Q1.** CuY zeolite is exposed to dibenzothiophene (DBT). What is the primary adsorption mechanism, and why does Cu specifically enable it?
- **Rubric:** Mentions π-complexation; identifies Cu⁺ (d¹⁰ configuration, [Ar]3d¹⁰) as the active oxidation state; explains that occupied 3d orbitals enable back-donation into the adsorbate's π* orbital, while the available 4s orbital accepts σ-donation from the aromatic ring.
- **Source:** Dissertation, Ch. 5 (DFT adsorption mechanism study); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (natural electron configuration data)

**Q2.** NaY zeolite shows much weaker sulfur adsorption than CuY for the same feed. Explain the mechanistic difference — specifically, could Na⁺ support a direct sulfur-metal (S-M) chemisorption interaction similar to what's seen with Ce, or is a different explanation needed?
- **Rubric:** Identifies NaY as relying on weak interactions rather than either π-complexation or S-M chemisorption. Should note that both π-complexation and S-M interaction modes are specifically tied to transition metal/lanthanide cations with accessible d-orbitals (as with Cu and Ce); Na⁺, an alkali metal with no accessible d-orbitals, lacks the orbital character needed for either specific coordination mode. Strong answers additionally note that NaY also lacks Brønsted acid sites (Na⁺ occupies the charge-balancing role instead of H⁺), which independently limits adsorption — the protonated (HY) form, by contrast, forms hydrogen bonds between its acidic hydroxyl groups and the sulfur/aromatic system, giving HY substantially higher capacity than NaY despite neither having a metal-cation site.
- **Source:** Dissertation, Ch. 5, Table 11 (NaY ΔHads ~ -72 to -92 kJ/mol vs. CuY ~ -141 to -149 kJ/mol); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (π-complexation/S-M mode discussion); Lee, K. X.; Valla, J. A. et al. review (Brønsted acid site H-bonding, HY vs. NaY)

**Q3.** Fresh (as-prepared) CuY zeolite begins with Cu in the +2 oxidation state. Describe what happens to the Cu oxidation state during the reduction process used to activate the sorbent, and why this matters for sulfur adsorption.
- **Rubric:** Identifies Cu²⁺ → Cu⁺ transition during reduction; notes Cu⁺ is the active π-complexation site, so incomplete reduction limits adsorption performance. Strong answers note that Cu²⁺'s d⁹ configuration lacks the fully occupied d-shell needed for effective back-donation, explaining specifically why reduction to Cu⁺ (not just "some reduced state") is required.
- **Source:** Dissertation, Ch. 3, §4.3.6 (Cu K-edge XANES reduction data); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Cu⁺ d¹⁰ requirement for π-complexation)

**Q4.** During the reduction treatment used to activate CuCeY, Cu²⁺ is reduced to Cu⁺. Does Ce in the same material undergo a similarly complete reduction to a single well-defined oxidation state? Describe what actually happens to Ce during this process.
- **Rubric:** Should NOT assume Ce reduces cleanly and completely the way Cu does. Correct answer notes Ce is unstable in a +2 state, and that experimental work (XPS) has found Ce present in a mixture of +3 and +4 states after ion-exchange and calcination, with in-situ XAS showing only partial reduction of Ce⁴⁺ toward Ce³⁺ under H₂ — i.e., Ce's reduction behavior is more partial/mixed than Cu's clean +2→+1 transition, and a model that assumes complete, uniform Ce³⁺ reduction by analogy with Cu should be marked down.
- **Source:** Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Ce oxidation state discussion, XPS/in-situ XAS references)

**Q5.** *[PENDING REVIEW — Henry to verify the η⁶/η² coordination framing against the source figures before finalizing]*
CeY has been shown to preferentially adsorb benzothiophene (BT) through η⁶ coordination, with the aromatic ring centered over the Ce³⁺ cation, rather than the η² π-complexation mode seen with Cu⁺. Explain the electronic difference between these two coordination modes.
- **Rubric:** Distinguishes η² Cu⁺ π-complexation (two π-bonded carbons, back-donation from filled Cu d-orbitals into the aromatic π* system) from η⁶ Ce³⁺ coordination (whole-ring interaction, more consistent with σ-donation/electrostatic-dominated bonding from Ce's f/d character).
- **Source:** Dissertation, Ch. 5, §5.3 (adsorption geometries, Figure 30–32)

**Q6.** What is the role of framework Al in zeolite ion-exchange?
- **Rubric:** Explains that Al substitution for Si in the aluminosilicate framework introduces a net negative charge, requiring charge-balancing extra-framework cations — this is the structural basis that allows metal cations (Na⁺, Cu²⁺, Ce³⁺, etc.) to be exchanged into the zeolite and subsequently act as adsorption sites.
- **Source:** Dissertation, Ch. 1–2 (zeolite structure background)

**Q7.** Distinguish physisorption from chemisorption as they apply to sulfur removal, using microporous activated carbon and CuY zeolite as contrasting examples.
- **Rubric:** Correctly characterizes AC's dominant mechanism as physical adsorption (van der Waals/pore confinement, non-specific) vs. CuY's chemisorption (specific orbital interaction via π-complexation with Cu⁺). Full credit should also be given to answers that note real materials can show both modes simultaneously (e.g., FWAC combines micropore physisorption with inorganic-impurity chemisorption) — a model that complicates the clean binary this way is demonstrating deeper understanding, not getting the question wrong.
- **Source:** Dissertation, Ch. 6 (FWAC discussion); Ch. 5 (CuY mechanism)

**Q8.** Introducing mesoporosity into Y zeolite (producing "SAY," Surfactant-Assisted Y — named for its synthesis method) significantly increases sulfur adsorption capacity for bulky molecules like DBT and 4,6-DMDBT compared to purely microporous parent Y. What mechanism explains this improvement, and is it a chemical or physical effect?
- **Rubric:** Identifies this as primarily a diffusion/mass-transport effect — mesopores reduce diffusion limitations, allowing bulky molecules better access to internal active sites — rather than a change in the intrinsic chemical adsorption mechanism itself.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (SAY mesoporous Y study)

**Q9.** *[PENDING REVIEW — not supported by Henry's own data; citation and rubric logic need rework before finalizing]*
After sulfur adsorption, CuY and CuCeY sorbents can be regenerated (largely restoring sulfur capacity) using a high-temperature treatment combined with a solvent of similar polarity to the adsorbate. What does the effectiveness of this regeneration method suggest about the nature of the Cu–sulfur bonding interaction?
- **Rubric:** [Needs rework — the "strong enthalpy implies reversibility" logic is flawed; binding strength and reversibility are separate properties. Needs a different, defensible framing before use.]
- **Source:** Findings cited in the dissertation introduction, attributed to external literature — not Henry's own generated data. Needs correct attribution before use.

**Q10.** Explain what "back-donation" means in the context of Cu⁺–thiophene π-complexation, and why the +1 (not +2 or 0) oxidation state of Cu is specifically favorable for this interaction.
- **Rubric:** Describes back-donation as electron density flowing from filled Cu d-orbitals into the empty π* antibonding orbitals of the aromatic/thiophene ring; explains Cu⁺'s d10 configuration provides favorable orbital energy/occupancy for this donation, which Cu²⁺ (fewer d-electrons available) and Cu⁰ (different bonding environment) do not replicate as effectively.
- **Source:** Dissertation, Ch. 5 (NBO analysis, §5.3–5.4)

**Q11.** For a bimetallic CuCeY sorbent, Natural Bond Orbital (NBO) analysis reveals direct electron-sharing interactions between the Cu and Ce cations themselves. What does this suggest about the relationship between the two metal sites, beyond each acting as an independent, separate adsorption site?
- **Rubric:** Recognizes this as evidence of direct electronic coupling/synergy between the two metal centers, not just two independent active sites coexisting in the same material — i.e., the metals influence each other's electronic structure.
- **Source:** Dissertation, Ch. 5, §5.4, Table 9 (Cu-Ce bonding NBOs)

**Q12.** Both activated carbon (AC) and CuY zeolite can adsorb dibenzothiophene, but they rely on fundamentally different molecular-level mechanisms. Briefly contrast the two.
- **Rubric:** CuY: chemisorption via Cu⁺ π-complexation with the thiophene ring. AC: physisorption into size-matched micropores, without a dedicated metal-cation coordination site (though some activated carbons can show supplementary chemisorption at trace inorganic impurity sites, depending on feedstock).
- **Source:** Dissertation, Ch. 5 (CuY); Ch. 6 (activated carbon discussion)

---

## Tier 2 — Comparative Reasoning

Goal: test whether the model can predict relative performance between two sorbents and justify it using the correct structure-property relationship, not just a general sense of which metal "sounds" more reactive.

**Q13.** Would you expect CuY or CeY to bind 4,6-dimethyldibenzothiophene (DMDBT) more strongly? Justify your answer using the underlying adsorption mechanism, not just the empirical trend.
- **Rubric:** Correctly favors CuY (ΔHads -142 kJ/mol vs. CeY -133 kJ/mol per DFT); justification grounded in π-complexation strength, not a generic "metals bind sulfur" claim.
- **Source:** Dissertation, Ch. 5, Table 11

**Q14.** A CuCeY mixed zeolite outperforms both CuY and CeY individually for DMDBT adsorption. Propose a mechanistic explanation for this synergy.
- **Rubric:** Proposes a genuine synergy mechanism (e.g., direct Cu-Ce electronic interaction, or an increase in the number/strength of available adsorption sites) rather than simply averaging the two individual mechanisms. Bonus: cites the specific enthalpy jump (CuY -142, CeY -133, CuCeY -249 kJ/mol for DMDBT — a value well beyond a simple average).
- **Source:** Dissertation, Ch. 5, Table 11; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142

**Q15.** Consider three sorbents: NaY zeolite, CuY zeolite, and FWAC (food waste-derived activated carbon). Rank these three by expected DBT (dibenzothiophene) adsorption capacity, and briefly justify the ranking based on their dominant mechanisms.
- **Rubric:** Correct ranking: FWAC > CuY > NaY (this ranking holds for both DBT and DMDBT). Justification should distinguish: NaY's weak interactions (lacking both accessible d-orbital metal chemistry and Brønsted acid sites, since Na⁺ occupies the charge-balancing role instead of H⁺); CuY's stronger but site-limited chemisorption via Cu⁺ π-complexation; and FWAC's combination of high micropore volume (size-matched to DBT/DMDBT's ~9 Å kinetic diameter) with supplementary chemisorption at inorganic impurity sites (residual Na, Ca, K, P from the food-waste feedstock) that CuY and NaY lack. A full-credit answer should invoke both the pore-size/surface-area distinction and the impurity-chemisorption point, not just one.
- **Source:** Dissertation, Ch. 5 (NaY, CuY); Ch. 6, §6.3.3, §6.4, Table 20 (FWAC pore structure and impurity data)

**Q16.** In Y zeolite, extra-framework cations occupy several distinct crystallographic positions: site I and I' are located deep within the hexagonal prism/sodalite cage regions, largely inaccessible to adsorbing molecules, while site II is located in the supercage, directly accessible to adsorbates. Cu tends to preferentially occupy site II, while Ce tends to preferentially occupy sites I/I'. What does this difference in site preference suggest about the relative *effective* (accessible) active site fraction between CuY and CeY, independent of each metal's intrinsic per-site binding strength?
- **Rubric:** Recognizes that even if Ce had comparable or favorable per-site electronic binding character, its strong preference for inaccessible interior sites (I/I') means a smaller fraction of total Ce is actually available to participate in adsorption, compared to Cu's preference for the directly accessible supercage site II — this site-accessibility effect is a separate limiting factor from per-site bonding strength, and can suppress CeY's real-world performance independent of its electronic mechanism.
- **Source:** Dissertation, Ch. 3, §3.2–3.4 (Cu/Ce site occupancy, supercage vs. interior sites)

**Q17.** Would you expect metal-exchanged Y zeolites like CuY and CeY to show strong chemical selectivity for sulfur-containing compounds specifically, over other aromatic compounds like benzene and naphthalene that are also present in real fuels? What property is primarily responsible for their improved desulfurization performance relative to unmodified Y or NaY?
- **Rubric:** A well-reasoned answer should not simply assume high sulfur-specific selectivity by default; the correct characterization is that metal exchange provides only modest chemical selectivity for sulfur over aromatics (computed binding strengths for aromatics can be comparable to smaller sulfur compounds), and the improved performance is better explained by a large increase in overall adsorption *capacity*/number of strong-binding sites introduced by metal exchange, rather than intrinsic sulfur-specific selectivity.
- **Source:** Dissertation, Ch. 5, §5.4, Table 11

**Q18.** *[Note: the "~10 kJ/mol variation" figure should be re-verified against Table 11 directly before use.]*
These adsorption enthalpies described here are DFT-computed values (single unit cell, no diffusion effects) rather than measured breakthrough capacities. On HY and NaY, computed adsorption strength depends noticeably on the size of the sulfur compound (larger compounds bind more strongly). On CuY, CeY, and CuCeY, this size dependence essentially disappears. Explain why metal exchange would eliminate a size-dependence trend that exists in the parent/alkali-exchanged material — and separately, explain why this computed thermodynamic trend does not necessarily predict the same ranking in real fixed-bed breakthrough experiments.
- **Rubric:** Two distinct points required for full credit: (1) mechanistic — on HY specifically, the size-dependent trend is attributed to hydrogen bonding between the sulfur/aromatic system and the zeolite's Brønsted acid sites (Si-OH-Al hydroxyl groups); larger, more electron-rich thiophenic compounds form stronger H-bond interactions. NaY, lacking Brønsted acid sites (Na⁺ occupies the charge-balancing role instead of H⁺), shows much weaker adsorption overall. In metal-exchanged Y, the strong, specific metal-cation π-complexation/S-M interaction dominates regardless of the sulfur compound's size, overriding this trend. (2) computational-vs-experimental — DFT enthalpies reflect a single, idealized unit cell with no diffusion limitation, while real fixed-bed breakthrough experiments on microporous materials can show the opposite size trend for bulky molecules (e.g., worse performance for larger compounds) due to diffusion limitations restricting access to internal active sites — so a thermodynamically favorable interaction does not guarantee good real-world performance if the molecule can't physically reach the site.
- **Source:** Dissertation, Ch. 5, Table 11 and surrounding discussion; Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (diffusion limitation in parent Y, Table 4)

**Q19.** In mesoporous Y zeolite, the extra-framework cation sites can be broadly grouped by location: rare earth cations (like Ce) show a strong affinity for sites I and I', located deep within the interior of the framework, while transition metal cations (like Cu) show a strong affinity for sites II and II', located nearer the accessible supercage surface. Given this, propose a reason why ion-exchanging Ce before Cu (Ce-then-Cu) produced substantially higher 4,6-DMDBT capacity (35 mL/g) than the reverse order, Cu-then-Ce (20 mL/g) — despite similar final elemental composition by ICP.
- **Rubric:** Should reason that when Ce is exchanged first, it preferentially occupies its favored interior sites (I/I'), leaving the accessible exterior sites (II/II') available for Cu introduced afterward — both metals end up reasonably well-placed. When Cu is exchanged first, it occupies the accessible exterior sites, and Ce introduced afterward is left with less access to its preferred interior sites (or ends up in suboptimal positions) — resulting in a less functionally effective distribution despite similar bulk composition.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 3, Figure 10a)

**Q20.** Beyond an optimal loading (~2 wt%), increasing Cu loading in Cu-Ce mesoporous Y zeolite (with Ce fixed) decreased 4,6-DMDBT capacity. In contrast, increasing Ce loading (with Cu fixed) increased capacity. Propose a mechanism for each trend that explains why they go in opposite directions.
- **Rubric:** For Cu: excess Cu beyond the ion-exchange capacity is not well-incorporated at true exchange sites and instead tends to end up in extra-framework positions, physically filling/blocking pores and impeding adsorption and/or diffusion — a pore-blocking effect, not a "restricting Ce's access" effect specifically. For Ce: additional Ce continues to fill the interior sites (I/I') effectively, and as those fill, it can push more Cu toward the accessible exterior sites (II/II'), which is favorable for adsorption; some Ce ending up in exterior sites is also functionally fine. Full credit requires these two distinct, correct mechanisms — not a symmetric "one blocks the other" explanation for both metals.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10b–c)

**Q21.** *[Note: mg/g would be a better capacity unit than mL/g, since mL/g is confounded by feed sulfur concentration — used here because it's what the source reports.]*
Without competing aromatics, CeY and CuY produced BT breakthrough capacities of 35 and 65 mL/g respectively, but CeY's breakthrough curve showed a much steeper slope than CuY's more gradual one. What does the difference in curve shape (not just capacity) suggest about the adsorption kinetics of the two materials?
- **Rubric:** Recognizes the steep CeY slope suggests faster saturation/adsorption kinetics but lower total capacity, while CuY's gradual slope suggests slower kinetics but sustained, higher-capacity adsorption. Capacity and kinetics are separate properties that don't have to track together.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142

**Q22.** *[NEW DRAFT — please review before finalizing]*
Without competing aromatics, CuY produced a BT breakthrough capacity of 65 mL/g. With 20 wt% benzene added to the feed, this dropped to about 12 mL/g. Would you expect this magnitude of performance loss (roughly 80%) to be primarily due to benzene physically blocking pore access, or due to a more specific chemical competition effect? Justify your reasoning.
- **Rubric:** Should reason toward chemical competition rather than simple pore blocking — benzene, like the sulfur compounds, can interact with the same Cu⁺ active sites (via π-complexation or related aromatic-metal interactions), directly competing for the limited number of specific chemisorption sites, rather than merely obstructing physical access to them.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Fig. 4a, BT breakthrough with 20 wt% benzene)

---

## Tier 3 — Counterfactual / Edge Cases

Goal: catch superficial pattern-matching. These questions test whether the model wrongly generalizes a trend from an adjacent or superficially similar process, rather than reasoning from the actual mechanism at hand.

**Q23.** In hydrodesulfurization (HDS), 4,6-DMDBT is notoriously difficult to remove due to steric hindrance from its methyl groups blocking access to the CoMo/NiMo catalytic surface. Would you expect the same steric-hindrance-driven difficulty for larger, bulkier thiophenic compounds during adsorptive desulfurization on a metal-free, mesoporous Y zeolite (i.e., a Y zeolite with no Cu, Ce, or other metal cation exchanged into it, but with mesopores introduced via a surfactant-assisted synthesis)? Why or why not?
- **Rubric:** Correctly identifies the opposite trend from HDS: larger thiophenic compounds (DBT, DMDBT) show *higher* breakthrough capacity than smaller ones (BT, TP) on this material. A strong answer attributes this to hydrogen bonding between the sulfur/aromatic system and the zeolite's Brønsted acid sites (Si-OH-Al hydroxyl groups), where larger, more electron-rich thiophenic compounds form stronger H-bond interactions — a distinct mechanism from HDS's active-site steric blocking, and distinct from generic "physisorption."
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 4); Lee, K. X.; Valla, J. A. et al. review (Brønsted acid site H-bonding mechanism, HY vs. NaY discussion)

**Q24.** A colleague claims that increasing Cu loading in CuY zeolite will always increase sulfur adsorption capacity. Is this claim correct? What factors could cause it to break down at high loading?
- **Rubric:** Identifies at least one real limiting factor: approaching maximum ion-exchange capacity/saturation, pore blockage, or restricted accessibility to other active sites at high loading. Does not simply affirm "more active sites = more capacity" without qualification.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10b, Cu loading study)

*[Q25 REMOVED — the original version leaked Q24's answer by structure, and overstated Ce loading behavior beyond what was actually tested (Ce loading increased capacity up to the highest tested level, but a decline at higher untested loadings is expected chemically, not something the data disproves). Needs a genuinely independent replacement if you want a Tier 3 question in this slot — happy to draft one on a different topic if useful.]*

**Q26.** *[FLAGGED FOR REWORK — this is really just asking "what properties determine adsorption capacity beyond surface area," and doesn't need specific materials/numbers attached. Consider generalizing to a plain conceptual question, or removing if redundant with Q34/Q35 once those are reworked.]*
A food-waste-derived activated carbon (FWAC) and a commercial activated carbon (CAC) sample were found to have comparable total BET surface areas. Given only this information, would you be able to confidently predict which sample has the higher sulfur adsorption capacity? What specific additional properties would you need to know?
- **Rubric:** Should recognize that total surface area alone is insufficient to predict relative capacity. A strong answer identifies pore size distribution/micropore volume and trace inorganic composition as the properties worth checking.
- **Source:** Dissertation, Ch. 6, §6.4; *ACS Omega* 2025, 10, 42725–42734

**Q27.** Would you expect naphthalene (a competing aromatic present in real fuels) to adsorb onto activated carbon via the same π–π stacking mechanism proposed for sulfur compounds like DBT? What problem does this raise for AC-based desulfurization selectivity?
- **Rubric:** Recognizes that if π–π stacking with the graphite face were the dominant mechanism, naphthalene would compete for the same sites, reducing sulfur selectivity — correctly identifies this as a genuine, experimentally demonstrated limitation (aromatics have been shown to compete with thiophenic compounds for AC adsorption sites), not just a theoretical concern.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (π–π stacking mechanism and aromatic competition discussion)

**Q28.** Enthalpy calculated by DFT suggests CuY and CeY show only modest selectivity for sulfur compounds over aromatics (benzene, naphthalene). What would you predict this means for desulfurization performance on a fuel with a high aromatic content, and what does experimental breakthrough data (with benzene present) actually show?
- **Rubric:** This question doesn't have a single "correct" verdict (what counts as "performs poorly" is a judgment call) — score on reasoning quality rather than a binary right/wrong. A strong answer should: (1) avoid assuming limited computed selectivity automatically means poor real-world performance; (2) cite that aromatics do measurably suppress performance experimentally (e.g., BT breakthrough on CuY dropping from 65 mL/g to ~12 mL/g with 20 wt% benzene present); (3) hold both facts at once — modest computed selectivity AND a real, substantial (not total) experimental performance penalty — rather than collapsing to an overly simple "it works great" or "it fails" verdict.
- **Source:** Dissertation, Ch. 5, Table 11 (DFT selectivity); Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (benzene competition data)

**Q29.** In situ XRD showed no crystalline Cu or Ce metal/oxide peaks in CuY, CeY, or CuCeY. Would this lead you to conclude that no meaningful change occurred in the Cu/Ce species during the reduction treatment? Why or why not?
- **Rubric:** Correctly rejects this conclusion — XRD is only sensitive to long-range crystalline order and would miss well-dispersed, sub-nanometer, or highly disordered species; the absence of XRD peaks does not mean no oxidation-state change occurred (which XANES independently confirmed).
- **Source:** Dissertation, Ch. 3, §3.3–3.4

**Q30.** Based on the relationship between micropore volume and sulfur capacity observed in activated carbon sorbents, what pore size range would you predict is most effective for physisorptive capture of DBT?
- **Rubric:** Should recall or reason toward DBT's kinetic diameter (~9 Å) and predict an ideal pore size just above this (i.e., micropores below ~10 Å) — close enough to provide strong confinement/multi-point van der Waals contact, but not so small that the molecule can't physically enter.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50 (micropore volume correlation); *ACS Omega* 2025, 10, 42725–42734

**Q31.** Would you expect a zeolite with a higher Si/Al ratio (fewer framework Al sites, and therefore fewer possible cation-exchange positions) to support higher or lower maximum metal loading, and how might this affect its ultimate sulfur adsorption capacity ceiling compared to a lower Si/Al ratio material?
- **Rubric:** Correctly reasons that higher Si/Al ratio means fewer exchangeable cation sites, generally limiting maximum metal loading and therefore capping the number of available strong-binding metal-cation adsorption sites — a plausible answer should connect this to a lower capacity ceiling, while noting this is a generalizable structure-property relationship rather than a specific reported dissertation finding (flag if your sources don't directly test this).
- **Source:** General zeolite ion-exchange chemistry — verify against dissertation background/introduction before finalizing; not a directly tested finding in the DFT/XAFS chapters.

**Q32.** A sorbent shows excellent sulfur breakthrough capacity in laboratory testing using a model fuel of thiophene in octane. Would you expect this capacity to transfer directly to a real diesel or gasoline fuel matrix? What specific complicating factor from this research would you flag as a likely reason for reduced real-world performance?
- **Rubric:** Should flag competitive adsorption from aromatic compounds (benzene, naphthalene, methylnaphthalene) naturally present in real fuels as a concrete, evidence-backed reason for expecting reduced real-world capacity relative to idealized model-fuel testing.
- **Source:** Dissertation, Ch. 4; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (aromatics competition studies)

---

## Tier 4 — Diagnostic / Anomaly Explanation

Goal: the hardest tier. Present a real, validated experimental finding that runs counter to naive expectation, and ask the model to explain it. There is no shortcut answer — the model must reason from mechanism to explain the anomaly. Cross-check each of these against the wider literature before finalizing, since contested science makes for a bad ground truth.

**Q33.** A food-waste-derived activated carbon (FWAC), which has no specific metal active sites, outperformed ion-exchanged Y zeolites in DMDBT adsorption capacity, despite the zeolites having specific, targeted metal-cation sites designed to chemically bind sulfur. Propose an explanation for how a material without such a targeted mechanism could still outperform one that has it.
- **Rubric:** Invokes pore volume/micropore accessibility as a competing factor to selective chemical interaction; recognizes physical adsorption capacity (a high density of size-matched micropores) can outweigh a smaller number of chemically-specific binding sites for this contaminant; proposes an actual mechanism rather than restating the question.
- **Source:** Dissertation, Ch. 6, §6.4

**Q34.** A food-waste-derived activated carbon (FWAC) and a mesoporous commercial activated carbon (CAC) have comparable total BET surface areas, yet FWAC's sulfur capacity is substantially higher than CAC's for both DBT and DMDBT. What specific structural and compositional differences would you propose to explain this gap?
- **Rubric:** Should identify (a) FWAC likely has a higher fraction of micropores relative to CAC's mesopore-dominated structure, and micropores sized close to the sulfur compounds' kinetic diameter (~9 Å) are especially effective for size-matched physisorption; (b) food-waste feedstocks typically carry residual inorganic content (e.g., alkali/alkaline earth metals, phosphorus from the biomass) largely absent in a purer commercial carbon source, which can provide supplementary chemisorption sites. This question is meant to be answerable through general materials chemistry reasoning about feedstock/porosity relationships, not recall of dissertation-specific figures.
- **Source:** Dissertation, Ch. 6, §6.3.3, §6.4, Table 20 (for grading/validation reference only)

**Q35.** For a series of porous carbon adsorbents being evaluated for DBT removal, would you expect micropore volume or total BET surface area to be a better predictor of relative sulfur adsorption capacity? Explain your reasoning.
- **Rubric:** Should favor micropore volume as the better predictor, reasoning from DBT's kinetic diameter (~9 Å) requiring size-matched micropores for effective physisorptive confinement, while total surface area conflates micropore, mesopore, and macropore contributions that aren't equally relevant to a specific-sized adsorbate.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50 (for grading/validation reference only)

*[Q36 REMOVED — redundant with Q18 (Tier 2) and Q23 (Tier 3), which already test the Brønsted-acid/metal-complexation size-dependence override from different angles.]*

**Q37.** *[FLAGGED — too obvious as written; in-situ vs. ex-situ characterization for redox-active species is fairly generic materials science knowledge, not a strong test of domain-specific reasoning. Consider removing or reworking to require a more specific, less guessable insight.]*
Explain why in-situ XAFS measurements were necessary to determine Cu and Ce oxidation states in CuY/CeY zeolites under operating (reduced) conditions, rather than relying on ex-situ characterization of the as-prepared material alone.

**Q38.** *[FLAGGED for rework per your review — needs more work before finalizing.]*
In situ XRD of CuY, CeY, and CuCeY showed no significant peaks attributable to crystalline Cu or Ce metal/oxide phases, even though XANES confirmed clear oxidation-state changes were occurring in these same materials. How can both of these observations be true simultaneously?

*[Q39 REMOVED — redundant with Q19 (Tier 2), same setup and numbers. Note: site I/I'/II/II' terminology is standard, decades-old zeolite crystallography vocabulary, not dissertation-specific — no issue with using it if this slot is refilled with a genuinely different question later.]*

*[Q40 REMOVED — redundant with Q17 (Tier 2) and Q28 (Tier 3), same selectivity-vs-capacity theme.]*

*(Optional additions to reach the top of the 8–12 target range: consider a question built around the biodiesel desulfurization chapter, or the regeneration/reusability data, if you want to broaden beyond the CuY/CeY/CuCeY and FWAC systems.)*

---

## Next Steps

- Review every question, rubric, and citation — this is a first-pass draft, not a final answer key. Correct anything that misrepresents your data or overstates certainty.
- Verify page/section/table references against your own copies of the dissertation and papers.
- For Tier 4 especially, confirm each "anomaly" reflects settled findings rather than a still-open question in the field.
- Trim to your preferred final count per tier — fewer airtight questions are better than more contestable ones.
- Once finalized, hand-test 10–15 in a chat interface before building the automated harness.
