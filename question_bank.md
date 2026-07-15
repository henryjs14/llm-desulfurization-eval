# LLM Reasoning Benchmark: Question Bank

*Adsorptive Desulfurization — Zeolites, Activated Carbon, Ion-Exchanged Sorbents*

## Overview

This question bank tests whether large language models genuinely reason through the mechanistic chemistry of sorbent-based sulfur removal, or are pattern-matching on surface-level associations between metals, materials, and sulfur compounds. Questions progress across four tiers of increasing difficulty, from basic mechanism identification to diagnostic reasoning about counterintuitive experimental findings.

Each question includes a scoring rubric (the specific points a correct answer must address) and a source. **This full draft was generated from the dissertation and related papers for review — treat every question, rubric, and citation as a first pass to verify, correct, and rewrite, not a final answer to approve as-is.** Page/section/table references should be checked against your own copies before finalizing, and Tier 4 findings in particular should be cross-checked against the wider literature.

## Question Counts by Tier

| Tier | Focus | Count in this draft |
|---|---|---|
| Tier 1 | Mechanism identification | 12 |
| Tier 2 | Comparative reasoning | 12 |
| Tier 3 | Counterfactual / edge cases | 10 |
| Tier 4 | Diagnostic / anomaly explanation | 8 |

**Total: 42 questions.** Trim, merge, or cut any that feel redundant or insufficiently rigorous once you review them — a smaller set of airtight questions beats a larger set with weak spots.

---

## Tier 1 — Mechanism Identification

Goal: establish a baseline. Can the model correctly name and explain the primary adsorption mechanism at play, including the correct oxidation state / electronic explanation, not just the correct material name?

**Q1.** CuY zeolite is exposed to dibenzothiophene (DBT). What is the primary adsorption mechanism, and why does Cu specifically enable it?
- **Rubric:** Mentions π-complexation; identifies Cu⁺ as the active oxidation state; mentions back-donation into the aromatic/thiophene ring.
- **Source:** Dissertation, Ch. 5 (DFT adsorption mechanism study)

**Q2.** NaY zeolite shows much weaker sulfur adsorption than CuY for the same feed. Explain the mechanistic difference.
- **Rubric:** Identifies NaY as relying on weaker electrostatic / van der Waals interactions vs. CuY's specific π-complexation via Cu⁺.
- **Source:** Dissertation, Ch. 5, Table 11 (NaY ΔHads ~ -72 to -92 kJ/mol vs. CuY ~ -141 to -149 kJ/mol)

**Q3.** Fresh (as-prepared) CuY zeolite begins with Cu in the +2 oxidation state. Describe what happens to the Cu oxidation state during the reduction process used to activate the sorbent, and why this matters for sulfur adsorption.
- **Rubric:** Identifies Cu²⁺ → Cu⁺ transition during reduction; notes Cu⁺ is the active π-complexation site, so incomplete reduction limits adsorption performance.
- **Source:** Dissertation, Ch. 3, §4.3.6 (Cu K-edge XANES reduction data)

**Q4.** Why is the Ce³⁺ oxidation state relevant to the adsorption behavior of CeY zeolite, and how does this differ mechanistically from Cu-based adsorption?
- **Rubric:** Distinguishes Ce's behavior from Cu's π-complexation pathway; notes Ce migrates from Ce⁴⁺ toward Ce³⁺ during reduction.
- **Source:** Dissertation, Ch. 3, §4.3.5–4.3.6

**Q5.** CeY has been shown to preferentially adsorb benzothiophene (BT) through η⁶ coordination, with the aromatic ring centered over the Ce³⁺ cation, rather than the η² π-complexation mode seen with Cu⁺. Explain the electronic difference between these two coordination modes.
- **Rubric:** Distinguishes η² Cu⁺ π-complexation (two π-bonded carbons, back-donation from filled Cu d-orbitals into the aromatic π* system) from η⁶ Ce³⁺ coordination (whole-ring interaction, more consistent with σ-donation/electrostatic-dominated bonding from Ce's f/d character).
- **Source:** Dissertation, Ch. 5, §5.3 (adsorption geometries, Figure 30–32)

**Q6.** What role does the negative framework charge of the Y zeolite (arising from Al substitution for Si in the aluminosilicate lattice) play in enabling ion exchange with Cu²⁺, Ce³⁺, or Na⁺ cations in the first place?
- **Rubric:** Explains that framework Al introduces a net negative charge requiring charge-balancing extra-framework cations, which is the structural basis that allows metal cations to be exchanged into the zeolite and subsequently act as adsorption sites.
- **Source:** Dissertation, Ch. 1–2 (zeolite structure background)

**Q7.** Distinguish physisorption from chemisorption as they apply to sulfur removal, using microporous activated carbon and CuY zeolite as contrasting examples.
- **Rubric:** Correctly characterizes AC's dominant mechanism as physical adsorption (van der Waals/pore confinement, non-specific) vs. CuY's chemisorption (specific orbital interaction via π-complexation with Cu⁺); recognizes real materials can show both to varying degrees (e.g., FWAC's inorganic impurities contributing chemisorption).
- **Source:** Dissertation, Ch. 6 (FWAC discussion); Ch. 5 (CuY mechanism)

**Q8.** Introducing mesoporosity into Y zeolite (producing "SAY," surfactant-templated mesoporous Y) significantly increases sulfur adsorption capacity for bulky molecules like DBT and 4,6-DMDBT compared to purely microporous parent Y. What mechanism explains this improvement, and is it a chemical or physical effect?
- **Rubric:** Identifies this as primarily a diffusion/mass-transport effect — mesopores reduce diffusion limitations, allowing bulky molecules better access to internal active sites — rather than a change in the intrinsic chemical adsorption mechanism itself.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (SAY mesoporous Y study)

**Q9.** After sulfur adsorption, CuY and CuCeY sorbents can be regenerated (largely restoring sulfur capacity) using a high-temperature treatment combined with a solvent of similar polarity to the adsorbate. What does the effectiveness of this regeneration method suggest about the nature of the Cu–sulfur bonding interaction?
- **Rubric:** Notes that successful regeneration under moderate thermal/solvent treatment (rather than requiring destructive/irreversible conditions) is consistent with a strong-but-reversible chemisorption interaction (π-complexation), not a permanent covalent bond or purely physical trapping.
- **Source:** Dissertation, Ch. 4, §4.1 (regeneration discussion)

**Q10.** Explain what "back-donation" means in the context of Cu⁺–thiophene π-complexation, and why the +1 (not +2 or 0) oxidation state of Cu is specifically favorable for this interaction.
- **Rubric:** Describes back-donation as electron density flowing from filled Cu d-orbitals into the empty π* antibonding orbitals of the aromatic/thiophene ring; explains Cu⁺'s d10 configuration provides favorable orbital energy/occupancy for this donation, which Cu²⁺ (fewer d-electrons available) and Cu⁰ (different bonding environment) do not replicate as effectively.
- **Source:** Dissertation, Ch. 5 (NBO analysis, §5.3–5.4)

**Q11.** For a bimetallic CuCeY sorbent, Natural Bond Orbital (NBO) analysis reveals direct electron-sharing interactions between the Cu and Ce cations themselves, even before any sulfur compound is adsorbed. What does this suggest about the relationship between the two metal sites, beyond each acting as an independent, separate adsorption site?
- **Rubric:** Recognizes this as evidence of direct electronic coupling/synergy between the two metal centers, not just two independent active sites coexisting in the same material — i.e., the metals influence each other's electronic structure.
- **Source:** Dissertation, Ch. 5, §5.4, Table 9 (Cu-Ce bonding NBOs)

**Q12.** Both FWAC (activated carbon) and CuY (ion-exchanged zeolite) can adsorb dibenzothiophene, but they rely on fundamentally different molecular-level mechanisms. Briefly contrast the two.
- **Rubric:** CuY: chemisorption via Cu⁺ π-complexation with the thiophene ring. FWAC: primarily physisorption into size-matched micropores, supplemented by chemisorption at inorganic impurity sites (Na, Ca, K, P), without a dedicated metal-cation coordination site.
- **Source:** Dissertation, Ch. 5 (CuY); Ch. 6 (FWAC)

---

## Tier 2 — Comparative Reasoning

Goal: test whether the model can predict relative performance between two sorbents and justify it using the correct structure-property relationship, not just a general sense of which metal "sounds" more reactive.

**Q13.** Would you expect CuY or CeY to bind 4,6-dimethyldibenzothiophene (DMDBT) more strongly? Justify your answer using the underlying adsorption mechanism, not just the empirical trend.
- **Rubric:** Correctly favors CuY (ΔHads -142 kJ/mol vs. CeY -133 kJ/mol per DFT); justification grounded in π-complexation strength, not a generic "metals bind sulfur" claim.
- **Source:** Dissertation, Ch. 5, Table 11

**Q14.** A CuCeY mixed zeolite outperforms both CuY and CeY individually for DMDBT adsorption. Propose a mechanistic explanation for this synergy.
- **Rubric:** Proposes a genuine synergy mechanism (e.g., direct Cu-Ce electronic interaction, or an increase in the number/strength of available adsorption sites) rather than simply averaging the two individual mechanisms. Bonus: cites the specific enthalpy jump (CuY -142, CeY -133, CuCeY -249 kJ/mol for DMDBT — a value well beyond a simple average).
- **Source:** Dissertation, Ch. 5, Table 11; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142

**Q15.** Rank NaY, CuY, and FWAC25 by expected DBT adsorption capacity based on their dominant mechanisms. Briefly justify the ranking.
- **Rubric:** Produces a ranking consistent with mechanism (weak electrostatic vs. strong chemisorption vs. high-capacity physisorption+impurity chemisorption) and gives distinct justification for each material, not a repeated template.
- **Source:** Dissertation, Ch. 5 (NaY, CuY); Ch. 6 (FWAC)

**Q16.** DFT calculations show the average Ce–framework distance in Y zeolite is longer than the corresponding Cu–framework distance, with Ce positioned slightly elevated out of the plane of the six-membered ring. What does this structural difference suggest about the relative steric accessibility of Ce versus Cu active sites?
- **Rubric:** Connects the elevated, longer-distance Ce position to reduced steric hindrance / greater accessibility for incoming sulfur molecules, relative to Cu.
- **Source:** Dissertation, Ch. 3, §3.2 (DFT structural comparison)

**Q17.** Based on DFT-calculated adsorption enthalpies, CuY, CeY, and CuCeY all show only modest selectivity for sulfur-containing compounds over pure aromatics like benzene and naphthalene (in some cases, aromatic ΔHads values are comparable to or exceed those of smaller sulfur compounds). Given this, is the superior desulfurization performance of these metal-exchanged zeolites better explained by enhanced sulfur *selectivity* or by something else? What?
- **Rubric:** Correctly identifies that the improved performance is attributed to greater overall adsorption *capacity*/number of available strong-binding sites introduced by metal exchange, rather than intrinsic chemical selectivity for sulfur over aromatics specifically.
- **Source:** Dissertation, Ch. 5, §5.4, Table 11 (discussion following enthalpy table)

**Q18.** On HY and NaY, adsorption strength depends noticeably on the size of the sulfur compound (e.g., on HY: DMDBT > DBT > BT > TP). On CuY, CeY, and CuCeY, this size dependence essentially disappears (variation of only ~10 kJ/mol across all four compounds). Compare and explain why metal exchange would eliminate a trend that exists in the parent/alkali-exchanged material.
- **Rubric:** Recognizes that in HY/NaY, adsorption is governed by weaker, more size-sensitive interactions (electron density on S scaling with molecule size); in metal-exchanged Y, the strong, specific metal-cation π-complexation interaction dominates regardless of the sulfur compound's size, overriding the size-dependent trend.
- **Source:** Dissertation, Ch. 5, Table 11 and surrounding discussion

**Q19.** In mesoporous Y zeolite ion-exchange, introducing Ce before Cu (Ce-then-Cu) produced substantially higher 4,6-DMDBT capacity than the reverse order (Cu-then-Ce), despite similar final elemental composition by ICP. Propose a reason why exchange order would matter even when the final metal loading is nearly the same.
- **Rubric:** Proposes that exchange order affects which cation sites are occupied by which metal (site selectivity/kinetics of exchange), meaning the same bulk composition can correspond to different active site distributions/accessibility — composition alone doesn't determine structure.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 3, Figure 10a)

**Q20.** Increasing Cu loading beyond an optimum in Cu-Ce mesoporous Y zeolite decreased 4,6-DMDBT capacity, while increasing Ce loading (with Cu fixed) increased capacity. Compare these two trends and propose why the same "more metal" strategy produces opposite results depending on which metal is varied.
- **Rubric:** Should reference plausible explanations such as Cu reaching maximum ion-exchange capacity/saturation with excess Cu not incorporating usefully (or restricting Ce accessibility), while additional Ce continues to find accessible sites without the same blocking effect. Full credit requires proposing a specific, non-hand-wavy mechanism, not simply restating that the trends differ.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10b–c)

**Q21.** Without competing aromatics, CeY and CuY produced BT breakthrough capacities of 35 and 65 mL/g respectively, but CeY's breakthrough curve showed a much steeper slope than CuY's more gradual one. What does the difference in curve shape (not just capacity) suggest about the adsorption kinetics of the two materials?
- **Rubric:** Recognizes the steep CeY slope suggests faster saturation/adsorption kinetics but lower total capacity (fewer accessible sites, e.g., Ce preferentially in sites less accessible to bulkier molecules), while CuY's gradual slope suggests slower kinetics but sustained, higher-capacity adsorption — capacity and kinetics are separate properties that don't have to track together.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142

**Q22.** Compare the expected effect of adding 1 wt% naphthalene to a model fuel on the DBT adsorption performance of parent Y zeolite versus CuCeY zeolite. Would you expect the relative (percentage) performance drop to be similar or different between the two materials, and why?
- **Rubric:** A reasonable answer should reason from mechanism: parent Y's weak, non-selective interactions make it more vulnerable to competitive displacement by aromatics, while CuCeY's greater number of strong binding sites/capacity may better withstand (though not eliminate) competitive adsorption — a full-credit answer should acknowledge some performance suppression occurs in both cases rather than claiming CuCeY is immune to aromatic competition.
- **Source:** Dissertation, Ch. 4 (aromatics competition discussion); Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10, naphthalene suppression)

---

## Tier 3 — Counterfactual / Edge Cases

Goal: catch superficial pattern-matching. These questions test whether the model wrongly generalizes a trend from an adjacent or superficially similar process, rather than reasoning from the actual mechanism at hand.

**Q23.** In hydrodesulfurization (HDS), 4,6-DMDBT is notoriously difficult to remove due to steric hindrance from its methyl groups blocking access to the CoMo/NiMo catalytic surface. On un-exchanged (HY/NaY) zeolite, would you expect the same steric-hindrance-driven difficulty for larger, bulkier thiophenic compounds during adsorptive desulfurization? Why or why not — and does your answer change if the zeolite is microporous versus mesoporous?
- **Rubric:** Should identify two distinct, separate effects rather than a single "yes/no": (1) electronically, larger thiophenic compounds (DBT, DMDBT) actually show *higher* electron density on the sulfur atom and can bind *more* strongly than smaller compounds on HY/NaY — the opposite trend from HDS steric blocking; (2) separately, microporous parent Y suffers a genuine diffusion/accessibility limitation for bulky molecules (resolved by introducing mesoporosity), which is a different phenomenon from HDS active-site steric blocking. Full credit requires distinguishing these two threads, not conflating them.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 4, electron density/kinetic diameter discussion); Dissertation Ch. 2 (mesoporosity/diffusion discussion)

**Q24.** A colleague claims that increasing Cu loading in CuY zeolite will always increase sulfur adsorption capacity. Is this claim correct? What factors could cause it to break down at high loading?
- **Rubric:** Identifies at least one real limiting factor: approaching maximum ion-exchange capacity/saturation, pore blockage, or restricted accessibility to other active sites at high loading. Does not simply affirm "more active sites = more capacity" without qualification.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10b, Cu loading study)

**Q25.** By the same logic as the previous question, would you expect increasing Ce loading in a Cu-Ce mesoporous Y zeolite to also show a capacity decline at high loading? What does the actual experimental trend show, and how would you explain any difference from the Cu case?
- **Rubric:** Correctly notes that (per the data) increasing Ce loading continued to increase 4,6-DMDBT capacity up to the highest loading tested, unlike Cu — a strong answer proposes why Ce might not saturate/block sites the same way Cu does (e.g., different ion-exchange capacity, different site preferences), rather than assuming the trends must be identical because both are "metal loading."
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10c)

**Q26.** Higher total BET surface area is often assumed to predict better sulfur adsorption capacity. Using the comparison between FWAC and commercial activated carbon (CAC) as an example, explain a case where this assumption fails.
- **Rubric:** Correctly notes that FWAC and CAC have comparable total surface areas (896 vs. 918 m²/g), yet FWAC substantially outperforms CAC — meaning surface area alone is not predictive; should invoke micropore volume/pore size distribution or inorganic-impurity chemisorption as the actual differentiator.
- **Source:** Dissertation, Ch. 6, §6.4, Figure 49; *ACS Omega* 2025, 10, 42725–42734

**Q27.** Would you expect naphthalene (a competing aromatic present in real fuels) to adsorb onto activated carbon via the same π–π stacking mechanism proposed for sulfur compounds like DBT? What problem does this raise for AC-based desulfurization selectivity?
- **Rubric:** Recognizes that if π–π stacking with the graphite face were the dominant mechanism, naphthalene would compete for the same sites, reducing sulfur selectivity — correctly identifies this as a genuine limitation, motivating alternative explanations (e.g., inorganic-impurity chemisorption) for AC's observed sulfur selectivity.
- **Source:** Dissertation, Ch. 6, §6.4; *ACS Omega* 2025, 10, 42725–42734

**Q28.** DFT enthalpy calculations suggest CuY and CeY show only modest selectivity for sulfur compounds over aromatics (benzene, naphthalene). Would you therefore expect these zeolites to perform poorly for desulfurization of a fuel with a high aromatic content? What does experimental breakthrough data (with benzene present) actually show?
- **Rubric:** A naive extrapolation from the DFT selectivity finding might predict poor real-world performance; a correct answer should note that aromatics do measurably suppress performance experimentally (e.g., BT breakthrough on CuY dropping from 65 mL/g to well below 15 mL/g with benzene present) — so both things are true simultaneously: limited intrinsic selectivity by DFT, and a real, substantial (but not total) performance penalty from aromatic competition experimentally.
- **Source:** Dissertation, Ch. 5, Table 11 (DFT selectivity); Ch. 4 / Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (benzene competition data)

**Q29.** In situ XRD showed no crystalline Cu or Ce metal/oxide peaks in CuY, CeY, or CuCeY. Would this lead you to conclude that no meaningful change occurred in the Cu/Ce species during the reduction treatment? Why or why not?
- **Rubric:** Correctly rejects this conclusion — XRD is only sensitive to long-range crystalline order and would miss well-dispersed, sub-nanometer, or highly disordered species; the absence of XRD peaks does not mean no oxidation-state change occurred (which XANES independently confirmed).
- **Source:** Dissertation, Ch. 3, §3.3–3.4

**Q30.** A material with a very high total pore volume but predominantly mesoporous (rather than microporous) character is proposed as a sulfur sorbent for DBT/DMDBT removal. Based on the FWAC findings, would you expect this material to perform comparably to a similarly high-pore-volume but predominantly microporous material? Why or why not?
- **Rubric:** Should correctly predict weaker performance from the mesopore-dominated material, since DBT/DMDBT (kinetic diameter ~9 Å) require micropores smaller than ~10 Å for effective physisorptive confinement — mesopores contribute to total pore volume without providing the same size-matched adsorption environment.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50 (micropore volume correlation)

**Q31.** Would you expect a zeolite with a higher Si/Al ratio (fewer framework Al sites, and therefore fewer possible cation-exchange positions) to support higher or lower maximum metal loading, and how might this affect its ultimate sulfur adsorption capacity ceiling compared to a lower Si/Al ratio material?
- **Rubric:** Correctly reasons that higher Si/Al ratio means fewer exchangeable cation sites, generally limiting maximum metal loading and therefore capping the number of available strong-binding metal-cation adsorption sites — a plausible answer should connect this to a lower capacity ceiling, while noting this is a generalizable structure-property relationship rather than a specific reported dissertation finding (flag if your sources don't directly test this).
- **Source:** General zeolite ion-exchange chemistry — verify against dissertation background/introduction before finalizing; not a directly tested finding in the DFT/XAFS chapters.

**Q32.** A sorbent shows excellent sulfur breakthrough capacity in laboratory testing using a simple model fuel (e.g., sulfur compound + octane only). Would you expect this capacity to transfer directly to a real diesel or gasoline fuel matrix? What specific complicating factor from this research would you flag as a likely reason for reduced real-world performance?
- **Rubric:** Should flag competitive adsorption from aromatic compounds (benzene, naphthalene, methylnaphthalene) naturally present in real fuels as a concrete, evidence-backed reason for expecting reduced real-world capacity relative to idealized model-fuel testing.
- **Source:** Dissertation, Ch. 4; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (aromatics competition studies)

---

## Tier 4 — Diagnostic / Anomaly Explanation

Goal: the hardest tier. Present a real, validated experimental finding that runs counter to naive expectation, and ask the model to explain it. There is no shortcut answer — the model must reason from mechanism to explain the anomaly. Cross-check each of these against the wider literature before finalizing, since contested science makes for a bad ground truth.

**Q33.** A food-waste-derived activated carbon (FWAC25) with no specific metal active sites outperformed ion-exchanged Y zeolites (including CuY and CeY) in DMDBT adsorption capacity, despite the zeolites having mechanistically "smarter" sulfur-selective sites. Propose an explanation.
- **Rubric:** Invokes pore volume/micropore accessibility as a competing factor to selective chemical interaction; recognizes physical adsorption capacity can outweigh chemical selectivity for this contaminant; proposes an actual mechanism rather than restating the question.
- **Source:** Dissertation, Ch. 6, §6.4, Figure 49

**Q34.** FWAC25 and commercial activated carbon (CAC) have similar total surface areas (896 vs. 918 m²/g), yet FWAC25's sulfur capacity is dramatically higher than CAC's for both DBT and DMDBT. What specific structural and compositional differences explain this gap?
- **Rubric:** Should identify (a) FWAC25 has substantially higher micropore volume relative to CAC (which is largely mesoporous), and micropores below ~10 Å are especially important given the ~9 Å molecular diameter of DBT/DMDBT; (b) FWAC25 contains Na, Ca, K, and P inorganic impurities largely absent in CAC, proposed as chemisorption sites for sulfur.
- **Source:** Dissertation, Ch. 6, §6.3.3, §6.4, Table 20; *ACS Omega* 2025, 10, 42725–42734

**Q35.** Within the FWAC series, sulfur adsorption capacity increased linearly with micropore volume — but total surface area alone did not predict capacity as cleanly. Explain why micropore volume specifically, rather than total surface area, is the better predictor for this system.
- **Rubric:** Connects the ~9 Å molecular diameter of DBT/DMDBT to the need for micropores smaller than ~10 Å; explains that mesopore/macropore contributions to "total surface area" don't provide the same size-matched confinement for physisorption.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50

**Q36.** DFT calculations show that on CuY, CeY, and CuCeY, adsorption enthalpy is essentially independent of sulfur compound size (varying by only ~10 kJ/mol between the smallest, TP, and largest, DMDBT). Yet on the un-exchanged HY and NaY, size clearly matters (adsorption strength scales with molecule size). Explain how introducing a strong, specific binding site could *eliminate* an otherwise-present size-dependence rather than simply adding to it.
- **Rubric:** A strong answer recognizes that in the metal-exchanged materials, the dominant interaction becomes the metal-cation–sulfur orbital interaction (which depends on local electronic structure, not overall molecular size), effectively overriding/masking the weaker, size-sensitive electrostatic contribution that governs the parent material — the specific interaction doesn't scale with molecular size the way diffuse/electrostatic interactions do.
- **Source:** Dissertation, Ch. 5, Table 11 and surrounding discussion

**Q37.** Explain why in-situ XAFS measurements were necessary to determine Cu and Ce oxidation states in CuY/CeY zeolites under operating (reduced) conditions, rather than relying on ex-situ characterization of the as-prepared material alone.
- **Rubric:** Notes that oxidation state changes under reducing conditions (Cu²⁺→Cu⁺, Ce⁴⁺→Ce³⁺), so characterizing only the fresh, unreduced material would not reflect the true active-state structure responsible for sulfur adsorption.
- **Source:** Dissertation, Ch. 3, §3.4–4.3.6

**Q38.** In situ XRD of CuY, CeY, and CuCeY showed no significant peaks attributable to crystalline Cu or Ce metal/oxide phases, even though XANES confirmed clear oxidation-state changes were occurring in these same materials. How can both of these observations be true simultaneously?
- **Rubric:** Recognizes that XRD is sensitive to long-range crystalline order and would miss well-dispersed, highly disordered, or sub-nanometer metal species; XANES is a local, element-specific probe sensitive to oxidation state regardless of crystallinity — the absence of XRD peaks indicates well-dispersed (not crystalline-clustered) metal species, not that no chemical change occurred.
- **Source:** Dissertation, Ch. 3, §3.3–3.4

**Q39.** Introducing Ce before Cu during ion exchange (versus the reverse order) produced 4,6-DMDBT capacity of 35 mL/g versus only 20 mL/g, respectively — despite the two materials having nearly identical Cu and Ce content by ICP elemental analysis. Explain how two materials with essentially the same bulk elemental composition could show such a large performance difference.
- **Rubric:** Should propose that exchange order determines which cation sites within the zeolite framework are preferentially occupied by which metal (a kinetic/site-selectivity effect during the sequential exchange process), meaning bulk composition alone does not determine active-site structure or accessibility — two "identical" materials by ICP can have meaningfully different real structures.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 3, Figure 10a)

**Q40.** DFT-calculated adsorption enthalpies indicate CuY and CeY show only modest chemical selectivity for sulfur compounds over aromatics like benzene and naphthalene. Yet these same materials are widely reported and marketed specifically as *desulfurization* sorbents, and do measurably outperform parent Y and NaY at removing sulfur from real fuels. Reconcile these two facts.
- **Rubric:** A strong answer separates "selectivity" from "capacity": the metals' main benefit is a large increase in the number of strong-binding adsorption sites (higher overall capacity) rather than a chemical preference for sulfur specifically over aromatics — so a material can be a good desulfurization sorbent in practice (high capacity, works in real fuel matrices where sulfur is a minority component) while showing limited computed selectivity at the molecular level.
- **Source:** Dissertation, Ch. 5, §5.4, Table 11

*(Optional additions to reach the top of the 8–12 target range: consider a question built around the biodiesel desulfurization chapter, or the regeneration/reusability data, if you want to broaden beyond the CuY/CeY/CuCeY and FWAC systems.)*

---

## Next Steps

- Review every question, rubric, and citation — this is a first-pass draft, not a final answer key. Correct anything that misrepresents your data or overstates certainty.
- Verify page/section/table references against your own copies of the dissertation and papers.
- For Tier 4 especially, confirm each "anomaly" reflects settled findings rather than a still-open question in the field.
- Trim to your preferred final count per tier — fewer airtight questions are better than more contestable ones.
- Once finalized, hand-test 10–15 in a chat interface before building the automated harness.
