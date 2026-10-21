# LLM Reasoning Benchmark: Question Bank

*Adsorptive Desulfurization: Zeolites, Activated Carbon, Ion-Exchanged Sorbents*

## Overview

This question bank tests whether large language models genuinely reason through the mechanistic chemistry of sorbent-based sulfur removal, or are pattern-matching on surface-level associations between metals, materials, and sulfur compounds. It covers metal-exchanged Y zeolites and activated carbons (porosity, inorganic content, and carbon structure), plus application to real fuels and biodiesel. Questions progress across four tiers of increasing difficulty.

Each question includes a scoring rubric (the points a correct answer must address) and a source. **Treat every question, rubric, and citation as a draft to verify, correct, and rewrite, not a final answer to approve as-is.** Questions marked NEW DRAFT have not yet been reviewed.

**Design note: self-contained questions.** When run against a model via API, the model will NOT have the dissertation as context. Any dissertation-specific label (FWAC, SAY, CAC, sample names) must be defined inline or replaced with a plain description.

**Terminology reference (for editing only):**
- **FWAC**: food waste-derived activated carbon.
- **CAC**: commercial activated carbon, used as a comparison baseline.
- **MisAC / WAC / CoAC**: activated carbons from miscanthus, walnut shell, and coconut shell.
- **SAY**: Surfactant-Assisted Y, mesoporous Y zeolite.

## Question Counts

| Tier | Focus | Questions | Zeolite | Activated carbon / biodiesel |
|---|---|---|---|---|
| Tier 1 | Mechanism and Materials Fundamentals | 10 | 5 | 5 |
| Tier 2 | Comparative Reasoning | 10 | 6 | 4 |
| Tier 3 | Counterfactual / Edge Cases | 10 | 5 | 5 |
| Tier 4 | Diagnostic / Anomaly Explanation | 10 | 5 | 5 |

**Total: 40 questions.** Original question numbers are kept so earlier review notes line up; renumber once the bank is final. Q7 and Q15 compare zeolites with carbons and are counted as activated carbon.

---

## Tier 1: Mechanism and Materials Fundamentals

Goal: establish a baseline. Can the model correctly explain the foundational chemistry and materials science the later tiers rely on: how sulfur compounds bind to metal sites and carbon surfaces, how sorbent structure and porosity are created and measured, what carbon disorder and inorganic content look like, and what common characterization techniques can tell you? Failures here make later-tier failures uninterpretable.

**Q1.** CuY zeolite is exposed to dibenzothiophene (DBT). What is the primary adsorption mechanism, and why does Cu specifically enable it?
- **Rubric:** Mentions π-complexation; identifies Cu⁺ (d¹⁰ configuration, [Ar]3d¹⁰) as the active oxidation state; explains that occupied 3d orbitals enable back-donation into the adsorbate's π* orbital, while the available 4s orbital accepts σ-donation from the aromatic ring.
- **Source:** Dissertation, Ch. 5 (DFT adsorption mechanism study); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (natural electron configuration data)

**Q2.** NaY zeolite shows much weaker sulfur adsorption than CuY for the same feed. Explain the mechanistic difference — specifically, could Na⁺ support a direct sulfur-metal (S-M) chemisorption interaction similar to what's seen with Ce, or is a different explanation needed?
- **Rubric:** Identifies NaY as relying on weak interactions rather than either π-complexation or S-M chemisorption. Should note that both π-complexation and S-M interaction modes are specifically tied to transition metal/lanthanide cations with accessible d-orbitals (as with Cu and Ce); Na⁺, an alkali metal with no accessible d-orbitals, lacks the orbital character needed for either specific coordination mode. Strong answers additionally note that NaY also lacks Brønsted acid sites (Na⁺ occupies the charge-balancing role instead of H⁺), which independently limits adsorption — the protonated (HY) form, by contrast, forms hydrogen bonds between its acidic hydroxyl groups and the sulfur/aromatic system, giving HY substantially higher capacity than NaY despite neither having a metal-cation site.
- **Source:** Dissertation, Ch. 5, Table 11 (NaY ΔHads ~ -72 to -92 kJ/mol vs. CuY ~ -141 to -149 kJ/mol); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (π-complexation/S-M mode discussion); Lee, K. X.; Valla, J. A. et al. review (Brønsted acid site H-bonding, HY vs. NaY)

**Q4.** During the reduction treatment used to activate CuCeY, Cu²⁺ is reduced to Cu⁺. Does Ce in the same material undergo a similarly complete reduction to a single well-defined oxidation state? Describe what actually happens to Ce during this process.
- **Rubric:** Should NOT assume Ce reduces cleanly and completely the way Cu does. Correct answer notes Ce is unstable in a +2 state, and that experimental work (XPS) has found Ce present in a mixture of +3 and +4 states after ion-exchange and calcination, with in-situ XAS showing only partial reduction of Ce⁴⁺ toward Ce³⁺ under H₂ — i.e., Ce's reduction behavior is more partial/mixed than Cu's clean +2→+1 transition, and a model that assumes complete, uniform Ce³⁺ reduction by analogy with Cu should be marked down.
- **Source:** Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Ce oxidation state discussion, XPS/in-situ XAS references)

**Q6.** What is the role of framework Al in zeolite ion-exchange?
- **Rubric:** Explains that Al substitution for Si in the aluminosilicate framework introduces a net negative charge, requiring charge-balancing extra-framework cations — this is the structural basis that allows metal cations (Na⁺, Cu²⁺, Ce³⁺, etc.) to be exchanged into the zeolite and subsequently act as adsorption sites.
- **Source:** Dissertation, Ch. 1–2 (zeolite structure background)

**Q7.** Distinguish physisorption from chemisorption as they apply to sulfur removal, using microporous activated carbon and CuY zeolite as contrasting examples.
- **Rubric:** Correctly characterizes AC's dominant mechanism as physical adsorption (van der Waals/pore confinement, non-specific) vs. CuY's chemisorption (specific orbital interaction via π-complexation with Cu⁺). Full credit should also be given to answers that note real materials can show both modes simultaneously (e.g., FWAC combines micropore physisorption with inorganic-impurity chemisorption) — a model that complicates the clean binary this way is demonstrating deeper understanding, not getting the question wrong.
- **Source:** Dissertation, Ch. 6 (FWAC discussion); Ch. 5 (CuY mechanism)

**Q8.** Introducing mesoporosity into Y zeolite (producing "SAY," Surfactant-Assisted Y — named for its synthesis method) significantly increases sulfur adsorption capacity for bulky molecules like DBT and 4,6-DMDBT compared to purely microporous parent Y. What mechanism explains this improvement, and is it a chemical or physical effect?
- **Rubric:** Identifies this as primarily a diffusion/mass-transport effect — mesopores reduce diffusion limitations, allowing bulky molecules better access to internal active sites — rather than a change in the intrinsic chemical adsorption mechanism itself.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (SAY mesoporous Y study)

**Q35.** For a series of porous carbon adsorbents being evaluated for DBT removal, would you expect micropore volume or total BET surface area to be a better predictor of relative sulfur adsorption capacity? Explain your reasoning.
- **Rubric:** Should favor micropore volume as the better predictor, reasoning from DBT's kinetic diameter (~9 Å) requiring size-matched micropores for effective physisorptive confinement, while total surface area conflates micropore, mesopore, and macropore contributions that aren't equally relevant to a specific-sized adsorbate.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50 (for grading/validation reference only)

**Q50.** *[NEW DRAFT: please review before finalizing]*
Activated carbon is often made by physical activation: biomass is first pyrolyzed to biochar under inert gas, then treated with steam at around 900 °C. Explain how the steam step creates porosity, and why longer or more intense activation typically raises BET surface area while lowering the mass yield of carbon.
- **Rubric:** Steam gasifies carbon from the char (H₂O + C → CO + H₂), so pores are created and widened by removing carbon atoms from the framework. More activation removes more carbon, lowering yield while increasing pore volume and surface area. Strong answers add that the trend does not continue indefinitely: excessive activation widens micropores into mesopores or macropores and can collapse or merge pore walls, eventually reducing micropore volume and surface area. Bonus for noting that steam widens pores earlier than CO₂, giving a broader pore size distribution with more mesoporosity.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Introduction on physical activation; §3.1 activation series); Dissertation, Ch. 6

**Q51.** *[NEW DRAFT: please review before finalizing]*
Two techniques are commonly used to assess the carbon structure of activated carbons. In Raman spectroscopy, carbons show a D band near 1350 cm⁻¹ and a G band near 1582 cm⁻¹. In X-ray diffraction, they may show broad features near 24° and 43° 2θ, a sharper peak near 47° 2θ, and sometimes additional sharp, narrow peaks between about 20° and 35° 2θ. Explain what each of these features indicates, and what a higher I_D/I_G ratio means.
- **Rubric:** Raman: G band arises from in-plane vibration of sp² graphitic carbon; D band is activated by defects and disorder; a higher I_D/I_G indicates a more disordered, defect-rich carbon (comparisons are most meaningful within a series measured the same way). XRD: broad peaks near 24° (002) and 43° (100) reflect amorphous or turbostratic carbon with little long-range order; a sharper peak near 47° indicates more crystalline graphite (101); additional sharp, narrow peaks that don't belong to carbon indicate crystalline inorganic phases (in biomass carbons, commonly calcium or potassium phosphates). Full credit requires correctly interpreting I_D/I_G direction and recognizing sharp non-carbon peaks as inorganic phases.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (§3.1–3.2, Fig. 2, Table 3); Dissertation, Ch. 6

**Q52.** *[NEW DRAFT: please review before finalizing]*
Activated carbons made from biomass feedstocks such as food waste can retain inorganic elements (for example Na, Ca, K, and P) after pyrolysis and activation. Which characterization techniques would you use to identify how much of these elements is present, what crystalline form they take, and where they sit on the carbon? How might such species contribute to the removal of thiophenic sulfur compounds from fuels?
- **Rubric:** Techniques: ICP-OES (or XRF) for bulk elemental composition; XRD for crystalline inorganic phases (sharp peaks, e.g., phosphates); SEM/STEM with EDS mapping for spatial distribution and particle size. Contribution: inorganic species can act as additional chemisorption sites for sulfur compounds (e.g., cation–sulfur interactions), complementing physisorption in pores; they may also alter surface chemistry and introduce disorder into the carbon structure. Strong answers flag that these roles are proposed based on correlation and literature for related systems, not directly proven for thiophenic sulfur on these carbons.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (§3.1–3.2, Table 2, Fig. 1, Discussion)

---

## Tier 2: Comparative Reasoning

Goal: test whether the model can predict relative performance between sorbents and justify it using the correct structure-property relationship, not just a general sense of which material "sounds" better.

**Q13.** Would you expect CuY or CeY to bind 4,6-dimethyldibenzothiophene (DMDBT) more strongly? Justify your answer using the underlying adsorption mechanism, not just the empirical trend.
- **Rubric:** Correctly favors CuY (ΔHads -142 kJ/mol vs. CeY -133 kJ/mol per DFT); justification grounded in π-complexation strength, not a generic "metals bind sulfur" claim.
- **Source:** Dissertation, Ch. 5, Table 11

**Q14.** A CuCeY mixed zeolite outperforms both CuY and CeY individually for DMDBT adsorption. Propose a mechanistic explanation for this synergy.
- **Rubric:** Proposes a genuine synergy mechanism (e.g., direct Cu-Ce electronic interaction, or an increase in the number/strength of available adsorption sites) rather than simply averaging the two individual mechanisms. Bonus: cites the specific enthalpy jump (CuY -142, CeY -133, CuCeY -249 kJ/mol for DMDBT — a value well beyond a simple average).
- **Source:** Dissertation, Ch. 5, Table 11; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142

**Q15.** Consider three sorbents: NaY zeolite, CuY zeolite, and FWAC (food waste-derived activated carbon). Rank these three by expected DBT (dibenzothiophene) adsorption capacity, and briefly justify the ranking based on their dominant mechanisms.
- **Rubric:** Correct ranking: FWAC > CuY > NaY (this ranking holds for both DBT and DMDBT). Justification should distinguish: NaY's weak interactions (lacking both accessible d-orbital metal chemistry and Brønsted acid sites, since Na⁺ occupies the charge-balancing role instead of H⁺); CuY's stronger but site-limited chemisorption via Cu⁺ π-complexation; and FWAC's combination of high micropore volume (size-matched to DBT/DMDBT's ~9 Å kinetic diameter) with supplementary chemisorption at inorganic impurity sites (residual Na, Ca, K, P from the food-waste feedstock) that CuY and NaY lack. A full-credit answer should invoke both the pore-size/surface-area distinction and the impurity-chemisorption point, not just one.
- **Source:** Dissertation, Ch. 5 (NaY, CuY); Ch. 6, §6.3.3, §6.4, Table 20 (FWAC pore structure and impurity data)

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

**Q34.** A food-waste-derived activated carbon (FWAC) and a mesoporous commercial activated carbon (CAC) have comparable total BET surface areas, yet FWAC's sulfur capacity is substantially higher than CAC's for both DBT and DMDBT. What specific structural and compositional differences would you propose to explain this gap?
- **Rubric:** Should identify (a) FWAC likely has a higher fraction of micropores relative to CAC's mesopore-dominated structure, and micropores sized close to the sulfur compounds' kinetic diameter (~9 Å) are especially effective for size-matched physisorption; (b) food-waste feedstocks typically carry residual inorganic content (e.g., alkali/alkaline earth metals, phosphorus from the biomass) largely absent in a purer commercial carbon source, which can provide supplementary chemisorption sites. This question is meant to be answerable through general materials chemistry reasoning about feedstock/porosity relationships, not recall of dissertation-specific figures.
- **Source:** Dissertation, Ch. 6, §6.3.3, §6.4, Table 20 (for grading/validation reference only)

**Q53.** *[NEW DRAFT: please review before finalizing]*
Consider two sorbents for removing dibenzothiophene (DBT) from a model fuel (octane with naphthalene): (A) a Cu- and Ce-exchanged mesoporous Y zeolite with a BET surface area around 650 m²/g, and (B) a commercial activated carbon with a BET surface area around 920 m²/g, of which about 350 m²/g is micropore area and about 570 m²/g is mesopore area. Which would you expect to have the higher sulfur capacity, and why?
- **Rubric:** Should favor the zeolite despite its lower surface area. Justification: the zeolite has specific metal-cation sites (Cu⁺ π-complexation, Ce interactions) that chemisorb sulfur compounds, plus micropores close to DBT's size; the commercial carbon's area is dominated by mesopores (2–50 nm), which are too wide for strong size-matched confinement of a ~9 Å molecule, and it lacks specific chemisorption sites. Key point: total surface area is not a reliable predictor of capacity across different sorbent classes. Note for grading: the zeolite and carbon data come from separate studies in the same group, so treat this as a qualitative comparison.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Table 1; Discussion comparing ion-exchanged Y zeolites with commercial AC, Fig. 6)

**Q54.** *[NEW DRAFT: please review before finalizing]*
Three activated carbons were made from different biomass feedstocks under identical pyrolysis and steam activation conditions, reaching similar mass yields and total surface areas (about 850–930 m²/g). Their properties:

| Sorbent | Micropore vol. (cm³/g) | Mesopore vol. (cm³/g) | P (wt%) | Ca (wt%) | K (wt%) | Na (wt%) |
|---|---|---|---|---|---|---|
| A | 0.259 | 0.304 | 1.0 | 1.0 | 3.5 | 0.2 |
| B | 0.293 | 0.208 | 0.1 | 0.8 | 1.7 | 0.0 |
| C | 0.283 | 0.199 | 0.3 | 0.1 | 2.0 | 0.3 |

Predict which will have the highest sulfur capacity for 4,6-dimethyldibenzothiophene, and justify your prediction.
- **Rubric:** Should predict A, even though it has the *lowest* micropore volume. Justification should cite A's higher inorganic content (notably P and Ca, plus K), consistent with additional chemisorption sites, and its higher mesopore volume, which can improve access to adsorption sites. A strong answer explicitly notes that micropore volume alone would predict the opposite ranking. Measured capacities: A 9.1, B 7.4, C 7.0 mg S/g; B and C are close, so do not require a specific order between them.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–2, §3.2; A = miscanthus, B = walnut shell, C = coconut shell AC)

---

## Tier 3: Counterfactual / Edge Cases

Goal: catch superficial pattern-matching. These questions test whether the model wrongly generalizes a trend from an adjacent or superficially similar situation, or draws a conclusion the data don't support, rather than reasoning from the actual mechanism.

**Q23.** In hydrodesulfurization (HDS), 4,6-DMDBT is notoriously difficult to remove due to steric hindrance from its methyl groups blocking access to the CoMo/NiMo catalytic surface. Would you expect the same steric-hindrance-driven difficulty for larger, bulkier thiophenic compounds during adsorptive desulfurization on a metal-free, mesoporous Y zeolite (i.e., a Y zeolite with no Cu, Ce, or other metal cation exchanged into it, but with mesopores introduced via a surfactant-assisted synthesis)? Why or why not?
- **Rubric:** Correctly identifies the opposite trend from HDS: larger thiophenic compounds (DBT, DMDBT) show *higher* breakthrough capacity than smaller ones (BT, TP) on this material. A strong answer attributes this to hydrogen bonding between the sulfur/aromatic system and the zeolite's Brønsted acid sites (Si-OH-Al hydroxyl groups), where larger, more electron-rich thiophenic compounds form stronger H-bond interactions — a distinct mechanism from HDS's active-site steric blocking, and distinct from generic "physisorption."
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 4); Lee, K. X.; Valla, J. A. et al. review (Brønsted acid site H-bonding mechanism, HY vs. NaY discussion)

**Q27.** Would you expect naphthalene (a competing aromatic present in real fuels) to adsorb onto activated carbon via the same π–π stacking mechanism proposed for sulfur compounds like DBT? What problem does this raise for AC-based desulfurization selectivity?
- **Rubric:** Recognizes that if π–π stacking with the graphite face were the dominant mechanism, naphthalene would compete for the same sites, reducing sulfur selectivity — correctly identifies this as a genuine, experimentally demonstrated limitation (aromatics have been shown to compete with thiophenic compounds for AC adsorption sites), not just a theoretical concern.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (π–π stacking mechanism and aromatic competition discussion)

**Q28.** Enthalpy calculated by DFT suggests CuY and CeY show only modest selectivity for sulfur compounds over aromatics (benzene, naphthalene). What would you predict this means for desulfurization performance on a fuel with a high aromatic content, and what does experimental breakthrough data (with benzene present) actually show?
- **Rubric:** This question doesn't have a single "correct" verdict (what counts as "performs poorly" is a judgment call) — score on reasoning quality rather than a binary right/wrong. A strong answer should: (1) avoid assuming limited computed selectivity automatically means poor real-world performance; (2) cite that aromatics do measurably suppress performance experimentally (e.g., BT breakthrough on CuY dropping from 65 mL/g to ~12 mL/g with 20 wt% benzene present); (3) hold both facts at once — modest computed selectivity AND a real, substantial (not total) experimental performance penalty — rather than collapsing to an overly simple "it works great" or "it fails" verdict.
- **Source:** Dissertation, Ch. 5, Table 11 (DFT selectivity); Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (benzene competition data)

**Q29.** In situ XRD showed no crystalline Cu or Ce metal/oxide peaks in CuY, CeY, or CuCeY. Would this lead you to conclude that no meaningful change occurred in the Cu/Ce species during the reduction treatment? Why or why not?
- **Rubric:** Correctly rejects this conclusion — XRD is only sensitive to long-range crystalline order and would miss well-dispersed, sub-nanometer, or highly disordered species; the absence of XRD peaks does not mean no oxidation-state change occurred (which XANES independently confirmed).
- **Source:** Dissertation, Ch. 3, §3.3–3.4

**Q48.** *[NEW DRAFT: please review before finalizing]*
A bimetallic Cu- and Ce-exchanged mesoporous Y zeolite was tested for dibenzothiophene (DBT) removal in two model fuels. In feed A (n-octane + 20 wt% benzene) it produced about 32 mL/g of DBT-free fuel. In feed B (n-octane + 1 wt% naphthalene) it produced about 45 mL/g. A colleague concludes that naphthalene is a weaker competitor for the sorbent's active sites than benzene. Is this conclusion justified by these data? What experiment would actually test it?
- **Rubric:** Should reject the conclusion as confounded: the two aromatics were present at very different concentrations (20 wt% vs. 1 wt%, roughly a 30x difference on a molar basis), so the comparison cannot separate concentration from intrinsic binding strength. Strong answers note that on a per-molecule basis naphthalene could plausibly be the *stronger* competitor (larger, more electron-rich π system, favorable for π-complexation), and propose a controlled comparison at equal molar aromatic concentration. Full credit requires spotting the concentration confound without being prompted; an answer that explains why naphthalene "binds more weakly" should be marked down.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (model fuel compositions in Methods; CuCeSAY DBT capacities in Conclusions)

**Q49.** *[NEW DRAFT: please review before finalizing]*
La, Sm, Nd, and Ce are all lanthanides that commonly exist as +3 cations with similar ionic radii, and when exchanged into Y zeolite all of them preferentially migrate into the sodalite cages. A researcher therefore assumes that pairing Cu with any of these four rare earths in Y zeolite should give roughly the same synergistic improvement in sulfur adsorption. Is this assumption reasonable? What property might distinguish one of these rare earths from the others?
- **Rubric:** Should not accept the assumption: similar charge, size, and siting do not guarantee the same functional behavior. Identifies Ce as the outlier because it can readily access a +4 oxidation state (Ce³⁺/Ce⁴⁺ redox), unlike La, Sm, and Nd, which are essentially fixed at +3; this redox flexibility is a plausible basis for stronger electronic interaction with Cu and with adsorbates. Experimentally, Ce gave the strongest synergy with Cu and the highest capacity of the rare earths tested. Because the source proposes oxidation state as a *possible* cause and calls for further work, score on reasoning: do not require a definitive mechanism, but do require the model to single out Ce's redox behavior rather than treating the lanthanides as interchangeable.
- **Source:** Lee, K. X. et al. *J. Phys. Chem. C* 2021 (doi:10.1021/acs.jpcc.1c01103), Rietveld siting results and Discussion of RE oxidation states

**Q55.** *[NEW DRAFT: please review before finalizing]*
In activated carbons made from food waste, sulfur capacity for dibenzothiophene increased linearly with micropore volume, and longer steam activation increases BET surface area. A colleague proposes activating the carbon as long as possible (down to about 15 wt% mass yield) to maximize sulfur capacity. Is this a sound plan? What would you expect to happen at very high degrees of activation?
- **Rubric:** Should reject the extrapolation. At very high activation, pore widening and merging of adjacent micropores convert micropores into mesopores and macropores, so micropore volume and surface area eventually *decrease* (observed at 15 wt% yield); a large fraction of the carbon framework is lost (carbon content fell by about half); and the carbon becomes more graphitic (I_D/I_G dropped). The optimum is at an intermediate activation level (25 wt% yield in this study), and the low yield also carries a cost. Full credit requires recognizing that the surface area trend reverses, not just citing yield cost.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (§3.1; Figs. S3, S8, S9; Tables S2, S3)

**Q56.** *[NEW DRAFT: please review before finalizing]*
Before pyrolysis, a food-waste feedstock was washed five times with deionized water to remove soluble minerals, then pyrolyzed and steam-activated to about 25 wt% mass yield. A colleague concludes that because the minerals were washed out, inorganic impurities cannot play a meaningful role in the resulting carbon's sulfur adsorption. Evaluate this reasoning.
- **Rubric:** Should reject it. Washing removes only *soluble* salts; insoluble mineral phases (e.g., calcium or potassium phosphates) remain. Because most of the carbon is lost during pyrolysis and activation while inorganics are largely retained, the inorganic fraction becomes *concentrated* in the final carbon. Should propose verifying with ICP-OES, XRD (sharp inorganic peaks), and EDS mapping. In this study, the washed food-waste carbon still contained several wt% each of P, Ca, K, and Na. Full credit requires both the solubility point and the concentration-by-mass-loss point.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Methods washing step; Table 2; Figs. 1–2)

**Q57.** *[NEW DRAFT: please review before finalizing]*
Two activated carbons were prepared under identical conditions from different biomass. Carbon X (food waste): micropore volume 0.246 cm³/g, mesopore volume 0.501 cm³/g, K 2.5 wt%, Na 2.6 wt%, Ca 2.1 wt%, P 3.0 wt%, dibenzothiophene capacity 6.3 mg S/g. Carbon Y (miscanthus): micropore volume 0.259 cm³/g, mesopore volume 0.304 cm³/g, K 3.5 wt%, Na 0.2 wt%, Ca 1.0 wt%, P 1.0 wt%, capacity 4.7 mg S/g. A researcher notes that both carbons are rich in K and concludes that K is the main active impurity responsible for X's superior performance. Is this conclusion supported?
- **Rubric:** Should reject it: Y contains *more* K than X yet has lower capacity, so K alone cannot explain X's advantage. The differences that track with performance are Na, Ca, and P (all much higher in X) and mesopore volume. Strong answers add that with only a few samples and several co-varying properties, the data cannot isolate any single element, and propose a controlled test (e.g., selectively adding or removing individual elements on one carbon).
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–2; §3.2)

**Q58.** *[NEW DRAFT: please review before finalizing]*
One proposed mechanism for thiophenic sulfur adsorption on activated carbon is π–π stacking between the aromatic rings of the sulfur compound and graphitic carbon planes. Consider three carbons with similar total surface area (850–930 m²/g): a commercial carbon with Raman I_D/I_G = 1.1 (most graphitic), micropore volume 0.157 cm³/g and about 37 wt% oxygen; nut-shell carbons with I_D/I_G ≈ 1.8–2.0 and micropore volume ≈ 0.28–0.29 cm³/g; and a food-waste carbon with I_D/I_G = 2.9 (most disordered), micropore volume 0.246 cm³/g, and several wt% of inorganic elements. If π–π stacking with graphitic planes were the dominant mechanism, what ranking would you predict? Would you trust that prediction?
- **Rubric:** Under the π–π hypothesis alone, the most graphitic commercial carbon should perform best. A strong answer should not trust this: the commercial carbon has by far the lowest micropore volume and a heavily oxidized surface, while the most disordered carbon has the most inorganic species, so pore structure and surface chemistry plausibly dominate over graphitic content. (Measured dibenzothiophene capacities ran opposite to graphitization: commercial 2.3, nut shells 4.2–5.1, food waste 6.3 mg S/g.) Bonus for noting that π–π stacking is non-selective, so aromatics like naphthalene would compete for the same sites. Marked down for confidently ranking by graphitization alone.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–3; §3.2; Discussion on π–π stacking)

---

## Tier 4: Diagnostic / Anomaly Explanation

Goal: the hardest tier. Present a real experimental finding that runs counter to naive expectation, and ask the model to explain it. There is no shortcut answer; the model must reason from mechanism to explain the anomaly. Cross-check each against the wider literature before finalizing, since contested science makes for a bad ground truth.

**Q33.** A food-waste-derived activated carbon (FWAC), which has no specific metal active sites, outperformed ion-exchanged Y zeolites in DMDBT adsorption capacity, despite the zeolites having specific, targeted metal-cation sites designed to chemically bind sulfur. Propose an explanation for how a material without such a targeted mechanism could still outperform one that has it.
- **Rubric:** Invokes pore volume/micropore accessibility as a competing factor to selective chemical interaction; recognizes physical adsorption capacity (a high density of size-matched micropores) can outweigh a smaller number of chemically-specific binding sites for this contaminant; proposes an actual mechanism rather than restating the question.
- **Source:** Dissertation, Ch. 6, §6.4

**Q41.** *[NEW DRAFT: please review before finalizing. Tension to resolve: the 2017 paper attributes Ce's selectivity to S–M σ-bonding, but Dissertation Ch. 5 DFT found no stable S–M geometry on reduced Ce³⁺ (σ-bonding reported on Ce(IV)Y).]*
Cu-exchanged and Ce-exchanged mesoporous Y zeolites were tested in fixed-bed breakthrough experiments. With dibenzothiophene (DBT) as the only sulfur compound in n-octane, the Cu material outperformed the Ce material (about 125 vs. 100 mL/g of DBT-free fuel). But in a model fuel containing thiophene, benzothiophene, and DBT together, the Ce material showed the highest total sulfur capacity. Propose a mechanistic explanation for why the ranking reverses when several sulfur compounds compete.
- **Rubric:** Should connect the reversal to a difference in *binding mode*, not just binding strength. Cu⁺ binds mainly through π-complexation with the aromatic ring, which is less discriminating between molecules; Ce binds mainly through direct S–M σ-bonding to the sulfur lone pair, which is more sulfur-specific and strongest for the most electron-rich compound (DBT). When only one adsorbate is present, Cu's larger number of accessible, strong sites wins; when adsorbates compete, Ce's more selective binding retains sulfur more effectively. Strong answers explicitly distinguish single-component capacity from multicomponent selectivity. Marked down if the answer simply asserts "Ce binds sulfur more strongly" without addressing why Cu wins in the single-component test.
- **Source:** Lee, K. X.; Valla, J. A. *Appl. Catal. B Environ.* 2017, 201, 359–369 (Conclusions; Fig. 7 mixed-sulfur breakthrough; Ce σ-bond discussion in §3.3)

**Q42.** *[NEW DRAFT: please review before finalizing]*
In-situ X-ray absorption spectroscopy of CuY zeolite during H₂ activation shows that Cu²⁺ is reduced to a mixture of isolated Cu⁺ cations in the framework's six-membered-ring sites *and* small metallic Cu⁰ clusters, which were absent before reduction. Should the Cu⁰ atoms be counted as active sites for thiophene π-complexation? What does this finding imply for (a) the relationship between total Cu loading and the number of active sites, and (b) how activation conditions should be chosen?
- **Rubric:** Should conclude that Cu⁰ is not equivalent to Cu⁺: metallic Cu is no longer an isolated, charge-balancing cation; it aggregates into clusters in which most atoms are not exposed; and it lacks the cationic Cu⁺ (3d¹⁰ with empty 4s) electronic character that supports π-complexation. (a) The number of active sites is therefore smaller than total Cu loading implies, so bulk composition overstates active-site density. (b) Activation is a trade-off: reduction must convert Cu²⁺ to Cu⁺ but over-reduction (harsher or longer treatment) converts useful Cu⁺ into less useful Cu⁰. Strong answers also note that when cationic Cu is reduced to Cu⁰, framework charge must be balanced by other means (e.g., H⁺, creating Brønsted acid sites). The optimal conditions themselves were not directly tested in the source, so score (b) on reasoning.
- **Source:** Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512 (XANES/EXAFS of CuY during reduction; Cu fcc scattering paths)

**Q43.** *[NEW DRAFT: please review before finalizing. Overlaps in theme with Q47 and Q19; keep the strongest one or two.]*
In Cu/rare-earth co-exchanged Y zeolites, X-ray diffraction refinement places the rare-earth cations (La, Ce, Sm, Nd) in the sodalite cages, which are too small for molecules like dibenzothiophene (~9 Å) to enter. Yet adding a rare earth to CuY increases its sulfur adsorption capacity. How can a cation that the sulfur molecule cannot physically reach still increase capacity?
- **Rubric:** Should propose at least one *indirect* mechanism and ideally two: (1) site displacement, where rare earths occupying interior sites (I, I′, II′) push Cu into the accessible supercage site II, increasing the fraction of Cu that adsorbates can reach (experimentally, greater site II occupancy by Cu when paired with Ce correlated with higher BT and DBT capacity); (2) electronic coupling, where the interior cation modifies the electronic structure of nearby Cu (consistent with computed Cu–Ce electron sharing). Should not claim the rare earth binds sulfur directly. Marked down for answers that ignore the stated inaccessibility.
- **Source:** Lee, K. X. et al. *J. Phys. Chem. C* 2021 (doi:10.1021/acs.jpcc.1c01103), Rietveld refinement; Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512 (site II occupancy and capacity); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Cu–Ce NBOs)

**Q44.** *[NEW DRAFT: please review before finalizing. Replaces the removed regeneration question (Q9) with a defensible framing.]*
A Cu/Ce co-exchanged mesoporous Y zeolite binds 4,6-dimethyldibenzothiophene through strong chemisorption. After saturation, it was regenerated by heating in air at 500 °C for 5 h, then reducing in H₂ at 400 °C for 5 h, and it recovered nearly 100% of its original capacity over two cycles. A colleague argues that full recovery proves the sulfur–metal interaction must be weak and reversible. Evaluate this argument.
- **Rubric:** Should reject the argument: regenerability and binding strength are separate properties, and this procedure does not rely on equilibrium desorption. The air step removes adsorbed organosulfur oxidatively (combustion) and also re-oxidizes Cu⁺ to Cu²⁺; the H₂ step then re-reduces Cu²⁺ to the active Cu⁺. Capacity is restored by chemically resetting the sites, which is fully consistent with strong chemisorption (and the harsh conditions needed are themselves a sign of strong binding). Strong answers note possible failure modes the result rules out over two cycles, such as residual sulfate or coke formation, or metal migration/sintering, and caution that two cycles is limited evidence for long-term stability.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (regeneration procedure in Methods; Figure 11)

**Q46.** *[NEW DRAFT: please review before finalizing]*
In microporous Cu/Ce co-exchanged Y zeolite, dibenzothiophene (DBT) removal was severely suppressed when 20 wt% benzene was added to the fuel. The same metals in a mesoporous Y zeolite (DBT diffusivity about 4.5 times higher) retained a substantially larger DBT capacity in the same benzene-containing fuel. Aromatic competition is usually described as a *chemical* effect (benzene competing for the same metal sites), while mesoporosity is a *physical* change. Why would a physical change to the pore structure reduce the impact of a chemical competition effect?
- **Rubric:** Should recognize that competition has a kinetic component: in micropores, small, fast-diffusing, highly concentrated benzene reaches and occupies the active sites long before slow-diffusing DBT arrives, so DBT loses the race regardless of relative binding strength. Mesopores speed DBT transport, letting it reach sites on a comparable timescale and access more sites overall (more total accessible sites also means the competitor exhausts a smaller share). Strong answers note that thermodynamic selectivity and kinetic access are separate, and that the chemical competition does not disappear, it is only partly offset. The mechanism is not directly tested in the source, so score on reasoning.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Conclusions; Table 2 diffusivities)

**Q59.** *[NEW DRAFT: please review before finalizing]*
In a series of activated carbons made from food waste at different activation levels, sulfur capacity increased linearly with micropore volume. But carbons made from walnut shell and coconut shell under the same conditions had *higher* micropore volumes (0.293 and 0.283 cm³/g) than the best food-waste carbon (0.246 cm³/g), similar total surface areas, and yet *lower* capacities (dibenzothiophene: 4.2 and 5.1 vs. 6.3 mg S/g; 4,6-dimethyldibenzothiophene: 7.4 and 7.0 vs. 10.2 mg S/g). How can micropore volume predict capacity within one series but fail across feedstocks?
- **Rubric:** Should recognize that a correlation within one feedstock series holds other variables (surface chemistry, inorganic content) roughly constant, so micropore volume appears to be the controlling factor; across feedstocks those other variables change. Should identify at least two differences favoring the food-waste carbon: much higher inorganic content (Na, Ca, P; the nut-shell carbons contain very little Na or P), mesopore volume more than double (0.501 vs. about 0.2 cm³/g) aiding access and diffusion, and greater carbon disorder. Full credit: micropore volume is necessary but not sufficient, plus at least two named confounders including inorganic content.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–3; §3.2; Fig. S9)

**Q60.** *[NEW DRAFT: please review before finalizing]*
A commercial, mesopore-dominated activated carbon performed poorly for dibenzothiophene removal from a model petroleum fuel, below several biomass carbons and below ion-exchanged Y zeolites. Yet when the same type of carbon was tested on biodiesel made from fats, oils, and grease, it was the best of the sorbents tested, removing about 38% of the sulfur versus 24–28% for HY zeolite, NaY zeolite, and β-cyclodextrin. The sulfur in this biodiesel consisted of light sulfides plus long-chain thiols and sulfur-containing esters. Explain this reversal.
- **Rubric:** Should tie the reversal to the size and type of the target molecules. Biodiesel sulfur species are long-chain, bulky, non-aromatic molecules that cannot readily enter zeolite micropores (Y zeolite windows are ~7.4 Å) and are not suited to π-based interactions; the carbon's large mesopore volume accommodates them. Biodiesel's higher viscosity also slows diffusion, further favoring wide pores. The properties that suited thiophenic DBT (size-matched micropores, π-complexation) are irrelevant or unfavorable here. Strong answers note the zeolites in the biodiesel test (HY, NaY) lacked metal sites, so the comparison is not identical to the model-fuel one.
- **Source:** Dissertation, Ch. 7, §7.3.1–7.3.2 (biodiesel sulfur speciation, batch sorbent comparison); *ACS Omega* 2025 (model-fuel AC performance)

**Q61.** *[NEW DRAFT: please review before finalizing]*
Biodiesel containing 212 ppm sulfur was passed through a fixed bed of commercial activated carbon. The very first 0.5 mL of effluent already contained about 40 ppm S, after which the effluent concentration rose slowly to saturation at about 12 mL/g. The integrated capacity (about 1.1 mg S/g) was only half the maximum capacity from batch isotherms with the same carbon (2.19 mg S/g, Langmuir fit). Two explanations were considered: (a) some sulfur species cannot adsorb on the carbon and pass straight through, or (b) the bed is limited by mass transfer and diffusion. Sulfur-selective GC of the first effluent sample showed the same light and heavy sulfur peaks as the feed, just at lower intensity. Which explanation does this support, and what accounts for the gap between batch and fixed-bed capacity?
- **Rubric:** Should conclude (b). If (a) were true, the early effluent would be enriched in specific non-adsorbing species, so its sulfur profile would differ from the feed; seeing every species at reduced intensity means all species adsorb but too slowly to be fully captured in the available contact time, consistent with diffusion-dominated transport and a dispersed breakthrough front. The capacity gap reflects incomplete bed utilization in the dynamic test: short contact time, slow access to smaller or less accessible pores, and possibly flow channeling, versus long contact and good mixing in batch. Bonus for noting biodiesel's viscosity as a contributor.
- **Source:** Dissertation, Ch. 7, §7.3.2 (Fig. 54 breakthrough, Fig. 55 isotherms)

**Q62.** *[NEW DRAFT: please review before finalizing]*
Commercial activated carbon used for biodiesel desulfurization was regenerated by heating under argon. Heating at 100 or 200 °C removed no sulfur. At 400 °C, the carbon's total pore volume fell by about 25% after the first adsorption–regeneration cycle but did not decrease further in later cycles; residual sulfur in the carbon rose from 40 ppm (fresh) to 123 ppm after one cycle and 157 ppm after two; and the carbon still retained 83% of its original sulfur capacity at the third cycle. Explain how sulfur can accumulate and pore volume can drop while most of the capacity is retained.
- **Rubric:** Should propose that a fraction of adsorbed sulfur species is held too strongly (or is too heavy and non-volatile) to be removed by inert heating at 400 °C, so it accumulates, likely at a limited set of strong sites or as deposits; the slowing accumulation suggests those sites or traps become saturated. The first-cycle pore volume loss points to partial pore blocking by residues or structural change that then stabilizes. Because most capacity comes from the bulk of accessible pore surface, which remains available, capacity is largely retained. Strong answers note that no removal at 100–200 °C shows the adsorbed species are not simply volatile and loosely held, and that inert (non-oxidative) heating cannot burn off heavy organosulfur; they may suggest an oxidative step, while noting it would also consume carbon.
- **Source:** Dissertation, Ch. 7, §7.3.3 (Table 23, Fig. 57, conclusions)

---

## Reserve Questions

Cut to make room for activated carbon coverage while keeping 10 per tier. Kept here as swaps if a tier question is dropped during review.

**Q3.** Fresh (as-prepared) CuY zeolite begins with Cu in the +2 oxidation state. Describe what happens to the Cu oxidation state during the reduction process used to activate the sorbent, and why this matters for sulfur adsorption.
- **Rubric:** Identifies Cu²⁺ → Cu⁺ transition during reduction; notes Cu⁺ is the active π-complexation site, so incomplete reduction limits adsorption performance. Strong answers note that Cu²⁺'s d⁹ configuration lacks the fully occupied d-shell needed for effective back-donation, explaining specifically why reduction to Cu⁺ (not just "some reduced state") is required.
- **Source:** Dissertation, Ch. 3, §4.3.6 (Cu K-edge XANES reduction data); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Cu⁺ d¹⁰ requirement for π-complexation)

**Q5.** *[Checked against Dissertation Fig. 31: η⁶ geometry confirmed. Rubric fix pending: NBO analysis found no bonding orbitals between Ce and BT, so replace "σ-donation" with electrostatic/dispersion-dominated binding.]*
CeY has been shown to preferentially adsorb benzothiophene (BT) through η⁶ coordination, with the aromatic ring centered over the Ce³⁺ cation, rather than the η² π-complexation mode seen with Cu⁺. Explain the electronic difference between these two coordination modes.
- **Rubric:** Distinguishes η² Cu⁺ π-complexation (two π-bonded carbons, back-donation from filled Cu d-orbitals into the aromatic π* system) from η⁶ Ce³⁺ coordination (whole-ring interaction, more consistent with σ-donation/electrostatic-dominated bonding from Ce's f/d character).
- **Source:** Dissertation, Ch. 5, §5.3 (adsorption geometries, Figure 30–32)

**Q10.** Explain what "back-donation" means in the context of Cu⁺–thiophene π-complexation, and why the +1 (not +2 or 0) oxidation state of Cu is specifically favorable for this interaction.
- **Rubric:** Describes back-donation as electron density flowing from filled Cu d-orbitals into the empty π* antibonding orbitals of the aromatic/thiophene ring; explains Cu⁺'s d10 configuration provides favorable orbital energy/occupancy for this donation, which Cu²⁺ (fewer d-electrons available) and Cu⁰ (different bonding environment) do not replicate as effectively.
- **Source:** Dissertation, Ch. 5 (NBO analysis, §5.3–5.4)

**Q11.** For a bimetallic CuCeY sorbent, Natural Bond Orbital (NBO) analysis reveals direct electron-sharing interactions between the Cu and Ce cations themselves. What does this suggest about the relationship between the two metal sites, beyond each acting as an independent, separate adsorption site?
- **Rubric:** Recognizes this as evidence of direct electronic coupling/synergy between the two metal centers, not just two independent active sites coexisting in the same material — i.e., the metals influence each other's electronic structure.
- **Source:** Dissertation, Ch. 5, §5.4, Table 9 (Cu-Ce bonding NBOs)

**Q16.** In Y zeolite, extra-framework cations occupy several distinct crystallographic positions: site I and I' are located deep within the hexagonal prism/sodalite cage regions, largely inaccessible to adsorbing molecules, while site II is located in the supercage, directly accessible to adsorbates. Cu tends to preferentially occupy site II, while Ce tends to preferentially occupy sites I/I'. What does this difference in site preference suggest about the relative *effective* (accessible) active site fraction between CuY and CeY, independent of each metal's intrinsic per-site binding strength?
- **Rubric:** Recognizes that even if Ce had comparable or favorable per-site electronic binding character, its strong preference for inaccessible interior sites (I/I') means a smaller fraction of total Ce is actually available to participate in adsorption, compared to Cu's preference for the directly accessible supercage site II — this site-accessibility effect is a separate limiting factor from per-site bonding strength, and can suppress CeY's real-world performance independent of its electronic mechanism.
- **Source:** Dissertation, Ch. 3, §3.2–3.4 (Cu/Ce site occupancy, supercage vs. interior sites)

**Q17.** Would you expect metal-exchanged Y zeolites like CuY and CeY to show strong chemical selectivity for sulfur-containing compounds specifically, over other aromatic compounds like benzene and naphthalene that are also present in real fuels? What property is primarily responsible for their improved desulfurization performance relative to unmodified Y or NaY?
- **Rubric:** A well-reasoned answer should not simply assume high sulfur-specific selectivity by default; the correct characterization is that metal exchange provides only modest chemical selectivity for sulfur over aromatics (computed binding strengths for aromatics can be comparable to smaller sulfur compounds), and the improved performance is better explained by a large increase in overall adsorption *capacity*/number of strong-binding sites introduced by metal exchange, rather than intrinsic sulfur-specific selectivity.
- **Source:** Dissertation, Ch. 5, §5.4, Table 11

**Q22.** *[NEW DRAFT — please review before finalizing]*
Without competing aromatics, CuY produced a BT breakthrough capacity of 65 mL/g. With 20 wt% benzene added to the feed, this dropped to about 12 mL/g. Would you expect this magnitude of performance loss (roughly 80%) to be primarily due to benzene physically blocking pore access, or due to a more specific chemical competition effect? Justify your reasoning.
- **Rubric:** Should reason toward chemical competition rather than simple pore blocking — benzene, like the sulfur compounds, can interact with the same Cu⁺ active sites (via π-complexation or related aromatic-metal interactions), directly competing for the limited number of specific chemisorption sites, rather than merely obstructing physical access to them.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Fig. 4a, BT breakthrough with 20 wt% benzene)

**Q24.** A colleague claims that increasing Cu loading in CuY zeolite will always increase sulfur adsorption capacity. Is this claim correct? What factors could cause it to break down at high loading?
- **Rubric:** Identifies at least one real limiting factor: approaching maximum ion-exchange capacity/saturation, pore blockage, or restricted accessibility to other active sites at high loading. Does not simply affirm "more active sites = more capacity" without qualification.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Figure 10b, Cu loading study)

**Q30.** Based on the relationship between micropore volume and sulfur capacity observed in activated carbon sorbents, what pore size range would you predict is most effective for physisorptive capture of DBT?
- **Rubric:** Should recall or reason toward DBT's kinetic diameter (~9 Å) and predict an ideal pore size just above this (i.e., micropores below ~10 Å) — close enough to provide strong confinement/multi-point van der Waals contact, but not so small that the molecule can't physically enter.
- **Source:** Dissertation, Ch. 6, §6.5, Figure 50 (micropore volume correlation); *ACS Omega* 2025, 10, 42725–42734

**Q31.** Would you expect a zeolite with a higher Si/Al ratio (fewer framework Al sites, and therefore fewer possible cation-exchange positions) to support higher or lower maximum metal loading, and how might this affect its ultimate sulfur adsorption capacity ceiling compared to a lower Si/Al ratio material?
- **Rubric:** Correctly reasons that higher Si/Al ratio means fewer exchangeable cation sites, generally limiting maximum metal loading and therefore capping the number of available strong-binding metal-cation adsorption sites — a plausible answer should connect this to a lower capacity ceiling, while noting this is a generalizable structure-property relationship rather than a specific reported dissertation finding (flag if your sources don't directly test this).
- **Source:** General zeolite ion-exchange chemistry — verify against dissertation background/introduction before finalizing; not a directly tested finding in the DFT/XAFS chapters.

**Q32.** A sorbent shows excellent sulfur breakthrough capacity in laboratory testing using a model fuel of thiophene in octane. Would you expect this capacity to transfer directly to a real diesel or gasoline fuel matrix? What specific complicating factor from this research would you flag as a likely reason for reduced real-world performance?
- **Rubric:** Should flag competitive adsorption from aromatic compounds (benzene, naphthalene, methylnaphthalene) naturally present in real fuels as a concrete, evidence-backed reason for expecting reduced real-world capacity relative to idealized model-fuel testing.
- **Source:** Dissertation, Ch. 4; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (aromatics competition studies)

**Q45.** *[NEW DRAFT: please review before finalizing. Check against Q18: these two findings are in tension, and Q18's rubric may need softening.]*
DFT calculations on single-site models of Cu- and Ce-exchanged Y zeolite give similar adsorption enthalpies for thiophene, benzothiophene, and dibenzothiophene, i.e., little dependence on molecular size. Yet experiments on Cu- and Ce-exchanged *mesoporous* Y (where diffusion limits are largely removed) show a clear preference TP < BT < DBT, in both breakthrough capacity and isosteric heats of adsorption measured from isotherms. Propose reasons both observations can be true.
- **Rubric:** Should not dismiss either result. Credible explanations include: (1) a real sorbent contains several site types (residual Brønsted acid sites, unexchanged framework, pore walls) whose interactions *do* scale with molecular size (H-bonding, dispersion), and an isosteric heat averages over all of them, while the DFT model isolates one metal site; (2) experiments occur in liquid octane, so a larger molecule displaces more solvent and the net free energy differs from a gas-phase-like calculation; (3) real metal speciation (e.g., Ce⁴⁺/Ce³⁺ mixtures, Cu⁰ clusters) differs from the idealized model; (4) the experimental authors attribute the trend to higher electron density in DBT favoring Ce σ-bonding, which a single-site model may underweight. Full credit requires at least two distinct reasons, including the multi-site point. Score on reasoning; this is a genuine tension, not a settled answer.
- **Source:** Lee, K. X.; Valla, J. A. *Appl. Catal. B Environ.* 2017, 201, 359–369 (isosteric heats, §3.3; TP < BT < DBT trend); Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (DFT enthalpies)

**Q47.** *[NEW DRAFT: please review before finalizing. Overlaps in theme with Q43 and Q19; keep the strongest one or two.]*
X-ray absorption analysis shows that in Ce-exchanged Y zeolite, Ce only enters the hexagonal prism (site I, deep in the framework) after heating to 450 °C during reduction. In a Cu/Ce co-exchanged Y zeolite with similar preparation, Ce is already found in site I after calcination, before any reduction. What does this difference suggest, and what does it imply for predicting bimetallic sorbent structure from monometallic data?
- **Rubric:** Should infer that Cu alters where Ce goes: Cu preferentially occupies the more exterior sites during exchange and calcination, driving Ce into interior sites earlier than it would migrate on its own. The two metals are therefore not independent; their siting is coupled. Implication: a bimetallic material's structure (and active-site distribution) cannot be predicted by simply combining the behavior of the two monometallic materials, so characterization must be done on the bimetallic material itself. Strong answers connect this to performance: Ce pushed inward leaves accessible sites for Cu.
- **Source:** Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512 (Ce EXAFS during reduction; Conclusions)

---

## Removed Questions

- Q9: rubric never written; regeneration data from external literature (replaced in spirit by Q44).
- Q12: redundant with Q7.
- Q25: leaked Q24's answer by structure.
- Q26: redundant with Q34.
- Q36: redundant with Q18 and Q23.
- Q37: generic in-situ vs. ex-situ characterization.
- Q38: redundant with Q29.
- Q39: redundant with Q19.
- Q40: redundant with Q17 and Q28.

---

## Next Steps

- Review each tier, starting with Tier 1. Correct anything that misrepresents the data or overstates certainty.
- Verify page, section, and table references against your own copies.
- Resolve flagged items: Q5 (rubric fix), Q18 (number check), Q41 (Ce σ-bonding tension).
- Hand-test 10–15 questions in a chat interface before building the automated harness.
