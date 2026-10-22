# Question Bank: Adsorptive Desulfurization Reasoning Benchmark

## Overview

This question bank evaluates whether large language models can reason through the chemistry of adsorptive desulfurization of liquid fuels, or whether they rely on surface-level associations between metals, sorbents, and sulfur compounds. The questions cover metal-exchanged Y zeolites, activated carbons, and their application to petroleum fuels and biodiesel.

Questions are organized into four tiers of increasing difficulty. Each question includes a rubric defining the points a complete answer must address, and the source of the underlying data.

## Design criteria

1. **Self-contained.** Each question can be answered from the information in the prompt and general chemical knowledge. Familiarity with the source publications is not required.
2. **Defensible answer.** Rubrics reflect what the chemistry supports rather than the conclusions of a single study. Where the evidence permits more than one interpretation, the rubric states this and scores the reasoning.
3. **No answer leakage.** The prompt does not contain or imply the answer.

Sources identify where the data originate and were used to verify the rubrics.

## Scoring

Each answer is graded against its rubric as Full, Partial, or Incorrect.

- **Full:** addresses every required rubric point and commits to the main explanation or conclusion.
- **Partial:** correct in direction but missing a required point, containing a factual error in supporting detail, or listing the correct explanation among several possibilities without identifying it as the most likely.
- **Incorrect:** reaches the wrong conclusion. For Tier 3, this includes adopting the plausible but incorrect conclusion the question invites, even if hedged.

Points introduced with "Strong answers" in a rubric are not required for full credit; they distinguish stronger answers among those that already meet the required points.

## Abbreviations

- **TP, BT, DBT, 4,6-DMDBT**: thiophene, benzothiophene, dibenzothiophene, 4,6-dimethyldibenzothiophene.
- **CuY, CeY, NaY, HY**: Y zeolite in which Cu, Ce, Na<sup>+</sup>, or H<sup>+</sup> is the charge-balancing cation. Cu(I)Y denotes Cu in the +1 oxidation state.
- **ΔH<sub>ads</sub>**: adsorption enthalpy.
- **ppmw**: parts per million by weight.
- **Breakthrough capacity (mL/g)**: volume of fuel treated per gram of sorbent in a fixed-bed experiment before sulfur is detected in the effluent.

## Question counts

| Tier | Focus | Questions |
|---|---|---|
| 1 | Mechanism and materials fundamentals | 8 |
| 2 | Comparative reasoning | 6 |
| 3 | Counterfactual and edge cases | 6 |
| 4 | Diagnostic and anomaly explanation | 5 |
| | **Total** | **25** |

---

## Tier 1: Mechanism and Materials Fundamentals

Tier 1 establishes a baseline. The questions test the fundamentals that later tiers build on: adsorption mechanisms at metal sites, the formation of porosity and its effect on adsorption, and the interpretation of common characterization data.

**Q1.** Identify the primary adsorption mechanism for dibenzothiophene (DBT) on Cu(I)Y zeolite and explain the electronic properties of Cu<sup>+</sup> that enable it.

- **Rubric:** The answer should identify π-complexation. Cu<sup>+</sup> has a filled 3d<sup>10</sup> shell and a vacant 4s orbital. The aromatic π system donates electron density into the vacant 4s orbital (σ-donation), and the filled 3d orbitals donate electron density into the vacant π<sup>\*</sup> orbitals of the ring (back-donation). Full credit requires both components.
- **Source:** [1]; [7] (Ch. 5)

**Q2.** DBT adsorbs much more weakly on NaY than on Cu(I)Y. Explain why Na<sup>+</sup> cannot bind DBT by the same mechanism as Cu<sup>+</sup>, and identify the interactions responsible for DBT adsorption on NaY.

- **Rubric:** Na<sup>+</sup> is an alkali metal cation without valence d electrons. It cannot back-donate into the π<sup>\*</sup> orbitals of DBT and therefore cannot form a π-complex. Adsorption on NaY arises from weaker interactions: electrostatic (cation–π) interaction with Na<sup>+</sup> and dispersion interactions with the zeolite framework. Strong answers note that framework interactions increase with adsorbate size, so larger sulfur compounds adsorb more strongly on NaY. Reference values (DFT): ΔH<sub>ads</sub> for DBT is −92 kJ/mol on NaY and −143 kJ/mol on CuY.
- **Source:** [1] (Table 4)

**Q3.** Explain the role of framework Al in zeolite ion exchange.

- **Rubric:** Isomorphous substitution of Al<sup>3+</sup> for Si<sup>4+</sup> in the aluminosilicate framework generates a net negative framework charge, which is balanced by extra-framework cations. These cations can be exchanged (e.g., Na<sup>+</sup> for Cu<sup>2+</sup> or Ce<sup>3+</sup>), allowing metal cations to be introduced as adsorption sites. Strong answers note that the Si/Al ratio therefore determines the maximum exchange capacity.
- **Source:** [7] (Ch. 1–2)

**Q4.** Cu is introduced into Y zeolite by aqueous ion exchange with a Cu(II) salt, followed by calcination in air. The sorbent is then heated in H<sub>2</sub> before use for desulfurization. (a) Why is this reduction step necessary for π-complexation with thiophenic compounds? (b) Why is Cu not introduced directly as Cu<sup>+</sup> from aqueous solution?

- **Rubric:** (a) Ion exchange introduces Cu<sup>2+</sup> (3d<sup>9</sup>), which remains Cu<sup>2+</sup> after calcination in air. Its higher charge and partially filled d shell make it a poor π back-donor, whereas π-complexation requires Cu<sup>+</sup>, with a filled 3d<sup>10</sup> shell for back-donation and a vacant 4s orbital for σ-acceptance. Reduction converts Cu<sup>2+</sup> to Cu<sup>+</sup>. (b) Cu<sup>+</sup> is unstable in aqueous solution and disproportionates (2Cu<sup>+</sup> → Cu + Cu<sup>2+</sup>), and common Cu(I) salts are poorly soluble in water, so aqueous exchange delivers Cu<sup>2+</sup>. Full credit requires both parts.
- **Source:** [1]; [2]

**Q5.** For a series of activated carbons evaluated for DBT removal from a model fuel, predict whether sulfur capacity will correlate more strongly with micropore volume (pores < 2 nm) or with mesopore volume (pores 2–50 nm), and justify the prediction.

- **Rubric:** Micropore volume. DBT has a molecular dimension of approximately 9 Å, and pores of similar width provide overlapping potentials from opposing walls and substantially stronger adsorption than wider pores. Mesopores primarily provide transport to the micropores and influence adsorption kinetics more than capacity. Strong answers note that mesopores remain important for accessibility, so effective carbons require both.
- **Source:** [3] (Fig. S9)

**Q6.** Activated carbon can be produced by pyrolysis of biomass to biochar under an inert atmosphere, followed by steam activation at approximately 900 °C. (a) Explain how steam activation generates porosity. (b) Over a moderate range, increasing the degree of activation increases BET surface area and decreases mass yield. Explain this trend and state whether it continues indefinitely.

- **Rubric:** (a) Steam gasifies carbon (H<sub>2</sub>O + C → CO + H<sub>2</sub>), creating and widening pores by removing carbon from the framework. (b) Greater activation removes more carbon, lowering yield while increasing pore volume and surface area. The trend does not continue indefinitely: with further activation, micropores widen into mesopores and macropores and pore walls collapse or merge, so micropore volume and surface area eventually decrease. In the limit, the carbon is fully consumed. Strong answers note that steam widens pores at an earlier stage of activation than CO<sub>2</sub>, producing a broader pore size distribution.
- **Source:** [3] (§1, §3.1)

**Q7.** Raman spectra of activated carbons show a D band near 1350 cm<sup>−1</sup> and a G band near 1580 cm<sup>−1</sup>. XRD patterns (Cu Kα) show broad reflections near 24° and 43° 2θ. (a) What structural features does each signal indicate? (b) What does an increase in I<sub>D</sub>/I<sub>G</sub> indicate?

- **Rubric:** (a) The G band arises from in-plane stretching of sp<sup>2</sup> carbon in graphitic domains. The D band is activated by defects and disorder in the carbon lattice. The broad reflections near 24° (002) and 43° (100) indicate carbon with limited long-range order (amorphous or turbostratic). (b) A higher I<sub>D</sub>/I<sub>G</sub> indicates greater structural disorder; comparisons are most reliable within a series measured under the same conditions.
- **Source:** [3] (Fig. 2, Table 3)

**Q8.** An activated carbon derived from food waste has the following characterization data. ICP-OES: 2–3 wt% each of Na, Ca, K, and P. XRD: sharp, narrow reflections superimposed on the broad carbon reflections. STEM-EDS mapping: particles enriched in these elements, up to approximately 100 nm in size, on the carbon surface. (a) What do these results indicate about the chemical form of these elements? (b) How might these species affect sulfur adsorption?

- **Rubric:** (a) The elements are present, at least in part, as crystalline inorganic particles (e.g., phosphates) dispersed on the carbon, rather than solely as isolated ions or surface groups. (b) They may provide additional sites that bind sulfur compounds more specifically than the carbon surface (chemisorption), and they may increase disorder in the carbon structure. Strong answers note that these roles are inferred from correlation rather than directly demonstrated, and that inorganic particles add mass without contributing pore volume.
- **Source:** [3] (Table 2, Fig. 1)

---

## Tier 2: Comparative Reasoning

Tier 2 questions require the model to predict relative performance between sorbents or adsorbates and to justify the prediction with the appropriate structure–property relationship.

**Q9.** CuY and CeY, each prepared by ion exchange to a target loading of 5 wt% metal, are evaluated for BT removal from *n*-octane under identical fixed-bed conditions. (a) Predict which sorbent binds BT more strongly and which has the higher breakthrough capacity. (b) Justify the prediction in terms of adsorption mechanism and cation accessibility. (c) What does this comparison suggest about transition metal versus rare earth cations in Y zeolite?

- **Rubric:** (a) CuY on both counts. (b) Cu<sup>+</sup> binds BT through π-complexation. Ce cations preferentially occupy sites within the sodalite cages and hexagonal prisms, which BT cannot access, whereas Cu preferentially occupies sites accessible from the supercage. Strong answers note that, at the same mass loading, CuY contains approximately twice as many metal atoms as CeY because the molar mass of Ce is more than twice that of Cu. (c) Transition metal cations such as Cu tend to provide accessible, strongly binding sites, whereas rare earth cations tend to migrate to inaccessible interior sites. Reference values: DFT ΔH<sub>ads</sub> for BT is −149 kJ/mol on CuY and −126 kJ/mol on CeY; breakthrough capacities are 65 mL/g (CuY) and 35 mL/g (CeY).
- **Source:** [1] (Table 4); [4] (Table 1, Discussion)

**Q10.** Bimetallic CuCeY zeolite exhibits a higher sulfur breakthrough capacity than either CuY or CeY. Propose an explanation.

- **Rubric:** The best-supported explanation is cation distribution. Ce preferentially occupies interior sites, so a larger fraction of Cu resides at sites accessible to sulfur compounds. This increases the number of usable Cu<sup>+</sup> sites while the adsorption mechanism (π-complexation at Cu<sup>+</sup>) is unchanged. Answers may cite DFT evidence of electron sharing between Cu and Ce as a possible contribution to binding strength, provided it is presented as such. Answers are marked down for asserting a distinct new bonding mechanism as established, or for treating the bimetallic sorbent as an average of the two monometallic sorbents.
- **Source:** [1]; [2]

**Q11.** DFT adsorption enthalpies for TP, BT, DBT, and 4,6-DMDBT generally become more negative with increasing molecular size on HY and NaY (from approximately −50 to −100 kJ/mol). On CuY and CeY, the values for the same four adsorbates fall within approximately 10 kJ/mol of one another. Explain both trends.

- **Rubric:** HY and NaY lack a strong specific binding site, so adsorption is dominated by interactions with the zeolite framework, primarily dispersion. Larger adsorbates have more atoms in contact with the framework and therefore adsorb more strongly. On CuY and CeY, a strong, localized cation–adsorbate interaction dominates (for Cu, π-complexation involving only part of the aromatic ring). This interaction is similar for all four adsorbates and much larger than the size-dependent framework contribution, so the size dependence largely disappears.
- **Source:** [1] (Table 4)

**Q12.** CuY and CeY are tested for BT removal from *n*-octane under identical fixed-bed conditions (feed concentration, flow rate, and bed dimensions). The breakthrough capacities are 65 mL/g for CuY and 35 mL/g for CeY. After breakthrough, the effluent sulfur concentration rises much more steeply for CeY than for CuY. What does the difference in breakthrough curve shape indicate?

- **Rubric:** The slope reflects how quickly sulfur is taken up as the feed passes through the bed. Because both sorbents share the same Y framework, differences in diffusion through the pore structure are unlikely to explain the difference, which therefore lies with the metal sites. Possible explanations include faster adsorption kinetics at the accessible Ce sites, and a narrower distribution of site strengths in CeY (few, relatively uniform accessible sites) than in CuY, where Cu<sup>+</sup> at different positions and some Cu<sup>0</sup> give a range of binding strengths that broadens the breakthrough curve. Differences in how the cations themselves obstruct diffusion may contribute but are likely minor. Full credit requires attributing the difference to the metal sites and distinguishing curve shape from capacity: the slope describes how sharply the bed saturates, not how much sulfur it holds. Answers that attribute the difference solely to framework diffusion are marked down.
- **Source:** [4] (Discussion); [2]

**Q13.** DFT adsorption enthalpies on CuY are: TP −141, BT −149, DBT −143, 4,6-DMDBT −142, benzene −125, and naphthalene −143 kJ/mol. Based on these values, predict whether competitive adsorption of aromatics is a more serious limitation for desulfurization of gasoline (principal sulfur compounds TP and BT; principal competing aromatic benzene) or diesel (principal sulfur compounds DBT and 4,6-DMDBT; principal competing aromatic naphthalene).

- **Rubric:** Diesel. Benzene binds 16–24 kJ/mol more weakly than TP and BT, providing some selectivity toward gasoline sulfur compounds, whereas naphthalene binds as strongly as DBT and 4,6-DMDBT, providing essentially no selectivity. Strong answers also note that aromatics are present at percent levels and sulfur compounds at ppm levels, so even a moderate enthalpic advantage may not prevent aromatics from occupying most sites, and that single-site DFT enthalpies exclude diffusion and solvent effects.
- **Source:** [1] (Table 4)

**Q14.** In a model fuel containing 100 ppmw S as 4,6-DMDBT and 1 wt% naphthalene in *n*-octane, an activated carbon derived from food waste achieved a higher sulfur capacity (approximately 10 mg S/g) than the best-performing Cu- and Ce-exchanged mesoporous Y zeolite (approximately 7 mg S/g). The zeolite contains Cu and Ce cations at ion-exchange sites. The carbon contains no exchanged cations but contains several wt% of Na, K, Ca, and P as inorganic particles. It has a BET surface area of approximately 900 m<sup>2</sup>/g and a total pore volume of approximately 0.75 cm<sup>3</sup>/g, roughly twice that of the zeolite. Propose explanations for the higher capacity of the carbon.

- **Rubric:** The answer should identify more than one factor. (1) The larger pore volume and surface area, including micropores comparable in size to 4,6-DMDBT, provide more physisorption capacity than the limited number of metal sites in the zeolite. (2) The inorganic species, which include metals (Na, K, Ca), may provide additional sulfur binding sites. (3) The capacity of the zeolite is limited by the number of accessible metal sites and by diffusion of a bulky adsorbate through its pore system. Answers are marked down for stating that the carbon contains no metal-containing species.
- **Source:** [3] (Tables 1–2, Fig. 6); [5]

---

## Tier 3: Counterfactual and Edge Cases

Tier 3 questions present situations that invite a plausible but incorrect conclusion, such as extrapolating a trend beyond its range or over-interpreting a characterization result. The prompt does not indicate which conclusion is wrong; the model must avoid it on its own.

**Q15.** CuY, CeY, and CuCeY were reduced in H<sub>2</sub>. XRD patterns collected after reduction show only reflections of the zeolite framework, with no reflections from crystalline Cu or Ce metal or oxide phases. What can be concluded from these data about changes in the oxidation state and coordination of Cu and Ce during reduction?

- **Rubric:** Nothing can be concluded about oxidation state or local coordination. XRD detects only crystalline phases with sufficient long-range order and crystallite size. Isolated cations at exchange sites, very small clusters, and disordered species produce no distinct reflections. The data show only that no large crystalline Cu or Ce phases formed. Strong answers propose element-specific methods, such as X-ray absorption spectroscopy (XANES for oxidation state, EXAFS for local structure), XPS, or H<sub>2</sub> temperature-programmed reduction. (In this system, XANES showed reduction of Cu<sup>2+</sup> to Cu<sup>+</sup> with some Cu<sup>0</sup>, and of Ce<sup>4+</sup> to Ce<sup>3+</sup>.) Answers concluding that Cu and Ce were unchanged are marked as incorrect.
- **Source:** [2]

**Q16.** A series of activated carbons was prepared from food waste by steam activation to mass yields of 65, 55, 45, 35, and 25 wt%. Across this series, BET surface area increased with the degree of activation, sulfur capacity increased with micropore volume, and the maximum capacity was obtained at 25 wt% yield. Predict how micropore volume, BET surface area, and sulfur capacity will change if activation is continued to 15 wt% yield.

- **Rubric:** All three are expected to decrease. With continued activation, pores widen and adjacent micropores merge, converting micropores into mesopores and macropores, so micropore volume and surface area decrease. A large fraction of the carbon framework is also lost. Because capacity depends on micropore volume, capacity is expected to decrease. (Observed: at 15 wt% yield, micropore volume and surface area decreased and the carbon content decreased by approximately half.) Answers that extrapolate the earlier trend and predict further increases are marked as incorrect.
- **Source:** [3] (§3.1)

**Q17.** A food waste feedstock was washed five times with deionized water to remove soluble minerals, then pyrolyzed and steam-activated to approximately 25 wt% mass yield. Predict whether inorganic elements (e.g., Na, Ca, K, and P) will be present in the final carbon at levels high enough to influence sulfur adsorption, and explain.

- **Rubric:** Yes, they are likely to be present at significant levels. (1) Washing removes only water-soluble salts; insoluble mineral phases and elements bound within the biomass remain. (2) Pyrolysis and activation remove most of the carbon while largely retaining inorganic elements, so their concentration in the final carbon increases several-fold. Strong answers propose measuring the inorganic content directly (e.g., ICP-OES or ICP-MS, XRF, ash content by TGA, XRD for crystalline phases, or EDS mapping). (In this case, the washed carbon contained 2–3 wt% each of Na, Ca, K, and P.) Answers predicting negligible inorganic content because of washing are marked as incorrect.
- **Source:** [3] (§2, Table 2)

**Q18.** Two activated carbons were prepared from different biomass feedstocks under identical conditions. They have similar BET surface areas and micropore volumes (0.25 and 0.26 cm<sup>3</sup>/g). Their other properties are given below.

| | Carbon X | Carbon Y |
|---|---|---|
| Mesopore volume (cm<sup>3</sup>/g) | 0.50 | 0.30 |
| K (wt%) | 2.5 | 3.5 |
| Na (wt%) | 2.6 | 0.2 |
| Ca (wt%) | 2.1 | 1.0 |
| P (wt%) | 3.0 | 1.0 |
| DBT capacity (mg S/g) | 6.3 | 4.7 |

Which property best explains the higher capacity of carbon X?

- **Rubric:** No single property can be identified from these data. K can be ruled out, because carbon Y contains more K but has the lower capacity. Na, Ca, P, and mesopore volume are all higher in X, and with two samples their effects cannot be separated; a controlled experiment, such as varying one element at a time on the same carbon, would be required. Micropore volume does not explain the difference, since it is nearly the same in both carbons, but this does not make it unimportant: it remains a primary determinant of capacity, with other properties modifying capacity in addition to it. Answers that confidently attribute the difference to a single property are marked down.
- **Source:** [3] (Tables 1–2)

**Q19.** Rietveld refinement of XRD data for CuCeY zeolite assigned Ce cations primarily to sodalite cage sites (SI′ and SII′), which DBT cannot enter, and Cu cations primarily to site SII, which is accessible from the supercage. Based on this assignment, can Ce cations contribute directly to DBT adsorption?

- **Rubric:** A direct contribution cannot be excluded. Rietveld refinement models electron density at each cation site and has limited ability to distinguish different cations at partially occupied sites. A site assigned to Cu may also contain Ce, so some Ce may occupy accessible sites and bind DBT directly. The refinement indicates a site preference, not strict exclusion. Strong answers also note that Ce at inaccessible sites may still contribute indirectly, for example by influencing the distribution of Cu. Answers concluding that Ce cannot contribute because of the site assignment are marked as incorrect.
- **Source:** [6]; [2]

**Q20.** π–π stacking between aromatic rings and the graphitic planes of activated carbon has been proposed as a mechanism for DBT adsorption. Four activated carbons with similar BET surface areas (850–930 m<sup>2</sup>/g) have the properties below. Rank them by expected DBT capacity and justify the ranking.

| Carbon | Raman I<sub>D</sub>/I<sub>G</sub> | Micropore volume (cm<sup>3</sup>/g) | Composition |
|---|---|---|---|
| Commercial | 1.1 | 0.16 | ~37 wt% O |
| Nut shell A | 1.8 | 0.29 | ~2 wt% K; little Na or P |
| Nut shell B | 2.0 | 0.28 | ~2 wt% K; little Na or P |
| Food waste | 2.9 | 0.25 | 2–3 wt% each of Na, Ca, K, P |

- **Rubric:** The commercial carbon should be ranked lowest, because it has by far the lowest micropore volume, despite being the most graphitic. The food waste and nut shell carbons should be ranked above it; either order of these is acceptable if justified, with credit for weighing micropore volume (favoring the nut shell carbons) against inorganic content (favoring the food waste carbon). Answers that rank the carbons by graphitization (lowest I<sub>D</sub>/I<sub>G</sub> highest) are marked as incorrect. (Observed DBT capacities: commercial 2.3, nut shell 4.2 and 5.1, food waste 6.3 mg S/g.)
- **Source:** [3] (Tables 1–3)

---

## Tier 4: Diagnostic and Anomaly Explanation

Tier 4 questions present experimental results that contradict a simple expectation. The model must reason from mechanism to explain them.

**Q21.** In situ X-ray absorption spectroscopy of CuY during H<sub>2</sub> reduction shows that Cu<sup>2+</sup> is reduced to Cu<sup>+</sup>, and that small metallic Cu<sup>0</sup> clusters, absent before reduction, also form. How would Cu<sup>0</sup> cluster formation affect sulfur adsorption?

- **Rubric:** Cu<sup>0</sup> cluster formation reduces the number of active sites. Each Cu atom incorporated into a cluster is no longer an isolated Cu<sup>+</sup> cation at an exchange site, and most atoms within a cluster are inaccessible to adsorbates. Metallic Cu also lacks the vacant 4s orbital that makes Cu<sup>+</sup> an effective σ-acceptor for π-complexation, and clusters may partially block pores. Total Cu loading therefore overstates the number of active sites. Strong answers note that reduction conditions involve a trade-off (sufficient to convert Cu<sup>2+</sup> to Cu<sup>+</sup>, but more severe or prolonged reduction promotes Cu<sup>0</sup> formation), and that reduction of Cu<sup>+</sup> to Cu<sup>0</sup> requires the framework charge to be balanced by other cations, such as H<sup>+</sup>.
- **Source:** [2]

**Q22.** Bimetallic Cu–Ce mesoporous Y zeolites were prepared with different nominal metal loadings and tested in a model fuel containing 100 ppmw S as 4,6-DMDBT and 1 wt% naphthalene in *n*-octane. Measured metal contents (ICP) and relative capacities are given below.

| Nominal loading | Measured Cu (wt%) | Measured Ce (wt%) | Relative capacity |
|---|---|---|---|
| 2% Cu, 2% Ce | 1.7 | 1.6 | Reference |
| 5% Cu, 2% Ce | 2.8 | 1.8 | Lower |
| 10% Cu, 2% Ce | 2.7 | 1.7 | Lower |
| 2% Cu, 5% Ce | 1.4 | 5.7 | Higher |
| 2% Cu, 10% Ce | 0.9 | 8.0 | Highest (~50 mL/g) |

Interpret these data.

- **Rubric:** A complete answer addresses four points. (1) Nominal loadings are misleading, and comparisons must use measured contents. Cu uptake plateaus near 2.7–2.8 wt%, indicating that the exchange capacity available to Cu has been reached. (2) Cu and Ce compete for a limited number of exchange sites, so increasing Ce displaces Cu. (3) Capacity increased as Cu content decreased, so Cu content alone does not determine capacity. Ce contributes, either by binding sulfur compounds directly or by influencing the location and accessibility of the remaining Cu. (4) The lower capacity at higher Cu content may result from Cu in less effective positions or as extra-framework species, but the data do not identify the cause, and this should be presented as a hypothesis.
- **Source:** [5] (Table 3, Fig. 10)

**Q23.** After use for 4,6-DMDBT adsorption from *n*-octane, a bimetallic Cu–Ce mesoporous Y zeolite was regenerated by calcination in air at 500 °C for 5 h, followed by reduction in H<sub>2</sub> at 400 °C for 5 h. It recovered nearly all of its original capacity over two cycles. What does this result indicate about the strength of 4,6-DMDBT adsorption on the sorbent?

- **Rubric:** The result provides no information on adsorption strength, because the regeneration does not rely on desorption of the intact adsorbate. Calcination in air combusts the adsorbed organosulfur compounds and oxidizes Cu<sup>+</sup> to Cu<sup>2+</sup>; the subsequent H<sub>2</sub> treatment reduces Cu<sup>2+</sup> to the active Cu<sup>+</sup>, restoring the sites chemically. The severity of the required conditions is itself consistent with strong adsorption. Strong answers note that two cycles provide limited evidence of long-term stability, and identify possible degradation pathways such as residual sulfate, loss of porosity, or metal migration. Answers concluding that 4,6-DMDBT is weakly or reversibly adsorbed are marked as incorrect.
- **Source:** [5] (§2, Figs. 11–12)

**Q24.** Biodiesel containing 212 ppmw S was passed through a fixed bed of commercial activated carbon. The first 0.5 mL of effluent already contained approximately 40 ppmw S, after which the effluent concentration increased gradually until saturation at approximately 12 mL/g. The capacity calculated from the breakthrough curve (approximately 1.1 mg S/g) was half the Langmuir maximum capacity obtained from batch isotherms with the same carbon (2.2 mg S/g). Gas chromatography with sulfur-selective detection showed that the first effluent sample contained the same light and heavy sulfur compounds as the feed, at lower concentrations. Explain the early appearance of sulfur in the effluent and the difference between the fixed-bed and batch capacities.

- **Rubric:** Early breakthrough is not caused by a subset of non-adsorbing compounds; in that case, the first effluent would contain only those compounds. Because all compounds appear at reduced concentrations, all are adsorbed, but not rapidly enough to be fully retained within the available contact time. This indicates mass transfer (diffusion) limitations. Flow channeling, in which part of the feed bypasses the bed, would produce the same signature and should also receive credit. The lower fixed-bed capacity reflects incomplete bed utilization due to short contact time, slow access to smaller or less accessible pores, and possibly flow channeling, compared with the long contact time and thorough mixing of batch experiments. Strong answers note that the higher viscosity of biodiesel slows diffusion.
- **Source:** [7] (Ch. 7, Figs. 54–55)

**Q25.** Commercial activated carbon used for biodiesel desulfurization was thermally regenerated under argon. Heating at 100 or 200 °C removed no sulfur. Regeneration at 400 °C gave the following results: total pore volume decreased by approximately 25% after the first adsorption–regeneration cycle and did not decrease further in subsequent cycles; residual sulfur in the carbon increased from 40 ppmw (fresh) to 123 ppmw after one cycle and 157 ppmw after two; and the carbon retained 83% of its original sulfur capacity in the third cycle. Explain how sulfur accumulation and pore volume loss can occur while most of the capacity is retained.

- **Rubric:** A fraction of the adsorbed sulfur is either bound too strongly or present in compounds of too low volatility to be removed by heating under an inert atmosphere at 400 °C, and therefore accumulates. The decreasing rate of accumulation suggests a limited population of strong sites or traps that become saturated. The first-cycle loss of pore volume suggests partial pore blocking by residues, or a structural change that then stabilizes. Because most of the capacity arises from the large remaining pore surface, most of it is retained. Strong answers note that the absence of sulfur removal at 100–200 °C shows that the adsorbed compounds are not simply volatile and weakly held, and that heating under an inert atmosphere cannot combust heavy organosulfur compounds. An oxidizing treatment would remove more sulfur but would also consume carbon.
- **Source:** [7] (Ch. 7, Table 23, Fig. 57)

---

## References

1. Sokol, H. J.; Lee, K. X.; Valla, J. A. The Mechanism of Adsorptive Desulfurization on Cu and Ce Exchanged Y Zeolite Using Density Functional Theory. *Comput. Mater. Sci.* **2024**, 235, 112813.
2. Sokol, H. J.; Ebrahim, A. M.; Caratzoulas, S.; Frenkel, A. I.; Valla, J. A. In Situ XAFS, XRD, and DFT Characterization of the Sulfur Adsorption Sites on Cu and Ce Exchanged Y Zeolites. *J. Phys. Chem. C* **2022**, 126, 1496–1512.
3. Sokol, H. J.; Pedram, S.; Jankovic, J.; Valla, J. A. Renewable Activated Carbon Sorbent for the Desulfurization of Liquid Fuels. *ACS Omega* **2025**, 10, 42725–42734.
4. Lee, K. X.; Tsilomelekis, G.; Valla, J. A. Removal of Benzothiophene and Dibenzothiophene from Hydrocarbon Fuels Using CuCe Mesoporous Y Zeolites in the Presence of Aromatics. *Appl. Catal. B Environ.* **2018**, 234, 130–142.
5. Lee, K. X.; Wang, H.; Karakalos, S.; Tsilomelekis, G.; Valla, J. A. Adsorptive Desulfurization of 4,6-Dimethyldibenzothiophene on Bimetallic Mesoporous Y Zeolites: Effects of Cu and Ce Composition and Configuration. *Ind. Eng. Chem. Res.* **2019**, 58, 18301–18312.
6. Lee, K. X.; Crowl, T. B.; Sokol, H. J.; Morales-Acosta, M. D.; Valla, J. A. Understanding the Role of Rare Earths in Zeolite Y on the Removal of Sulfur from Hydrocarbon Fuels. *J. Phys. Chem. C* **2021**, 125, 9107–9118.
7. Sokol, H. J. Ph.D. Dissertation, University of Connecticut.
