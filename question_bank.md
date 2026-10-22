# Question Bank: Adsorptive Desulfurization Reasoning Benchmark

## Overview

This question bank tests whether large language models can reason through the chemistry of sorbent-based sulfur removal from liquid fuels, or whether they rely on surface-level associations between metals, materials, and sulfur compounds. It covers metal-exchanged Y zeolites, activated carbons, and the application of both to real fuels and biodiesel.

Questions are grouped into four tiers of increasing difficulty. Each question has a rubric listing the points a correct answer must address, and a source for the data and findings it is based on.

## Design criteria

Every question is written to meet three criteria:

1. **Answerable from the prompt and general chemistry.** A model does not need to have read the source papers. Any data needed to answer is given in the question.
2. **One defensible answer.** The rubric reflects what the chemistry supports, not only what a single study reported. Where the evidence leaves room for interpretation, the rubric says so and scores the reasoning.
3. **The answer is not in the question.**

The sources are where the data come from and how the rubrics were checked. They are not required reading for the model being tested.

## Abbreviations used in questions

- **TP, BT, DBT, 4,6-DMDBT**: thiophene, benzothiophene, dibenzothiophene, and 4,6-dimethyldibenzothiophene.
- **CuY, CeY, NaY, HY**: Y zeolite with Cu, Ce, Na, or H<sup>+</sup> as the charge-balancing cation. Cu(I)Y specifies Cu in the +1 state.
- **Breakthrough capacity (mL/g)**: volume of sulfur-free fuel produced per gram of sorbent in a fixed-bed test before sulfur appears in the outlet.

## Question counts

| Tier | Focus | Questions |
|---|---|---|
| 1 | Mechanism and materials fundamentals | 9 |
| 2 | Comparative reasoning | 6 |
| 3 | Counterfactual and edge cases | 6 |
| 4 | Diagnostic and anomaly explanation | 6 |
| | **Total** | **27** |

---

## Tier 1: Mechanism and Materials Fundamentals

Can the model explain the foundations the later tiers rely on: how sulfur compounds bind to metal sites and carbon surfaces, how porosity is created and how it affects adsorption, and what common characterization results mean?

**Q1.** Cu(I)Y zeolite is exposed to dibenzothiophene (DBT). What is the main adsorption mechanism, and why does Cu<sup>+</sup> enable it?

- **Rubric:** Identifies π-complexation. Cu<sup>+</sup> has a filled 3d<sup>10</sup> shell and an empty 4s orbital. Electron density from the π system of the aromatic ring is donated into the empty 4s orbital (σ-donation), and electron density from the filled 3d orbitals is donated back into the empty π<sup>\*</sup> orbitals of the ring (back-donation). Both are needed for full credit.
- **Source:** Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813; Sokol, H. J. PhD Dissertation, Ch. 5

**Q2.** For the same sulfur compound, NaY zeolite adsorbs DBT much more weakly than Cu(I)Y. Why can Na<sup>+</sup> not bind DBT the way Cu<sup>+</sup> does, and what holds DBT in NaY instead?

- **Rubric:** Na<sup>+</sup> is an alkali metal cation with no valence d electrons, so it cannot back-donate into the π<sup>\*</sup> orbitals of DBT and cannot form a π-complex. DBT in NaY is held by weaker interactions: electrostatic (cation–π) interaction with Na<sup>+</sup> and dispersion interactions with the zeolite framework. Strong answers note that the framework interactions grow with molecular size, so larger sulfur compounds bind somewhat more strongly in NaY. Reference values (DFT): ΔH<sub>ads</sub> of DBT is about -92 kJ/mol on NaY and -143 kJ/mol on CuY.
- **Source:** Sokol, H. J.; Lee, K. X.; Valla, J. A. *Comput. Mater. Sci.* 2024, 235, 112813 (Table 4)

**Q3.** What is the role of framework Al in zeolite ion exchange?

- **Rubric:** Substituting Al<sup>3+</sup> for Si<sup>4+</sup> in the aluminosilicate framework creates a net negative charge that must be balanced by extra-framework cations. These cations can be exchanged for others (for example Na<sup>+</sup> for Cu<sup>2+</sup> or Ce<sup>3+</sup>), which is what allows metal cations to be introduced and act as adsorption sites. Strong answers note that the Si/Al ratio therefore sets the maximum number of exchangeable cations.
- **Source:** Sokol, H. J. PhD Dissertation, Ch. 1–2

**Q4.** DBT can be removed from a hydrocarbon fuel using either a microporous activated carbon or Cu(I)Y zeolite. Describe the main interaction holding DBT on each sorbent, and classify each as physisorption or chemisorption.

- **Rubric:** Activated carbon: mainly dispersion (van der Waals) interactions, strengthened when DBT sits in micropores close to its own size, where it contacts the pore walls on several sides. This is physisorption and is not specific to sulfur. Cu(I)Y: π-complexation between Cu<sup>+</sup> and the aromatic ring of DBT, an orbital interaction that is chemisorption. Full credit also goes to answers noting that real sorbents can show both, for example activated carbons with surface groups or inorganic species that bind sulfur compounds more specifically.
- **Source:** *ACS Omega* 2025, 10, 42725–42734; *Comput. Mater. Sci.* 2024, 235, 112813

**Q5.** Y zeolite normally contains only micropores. Introducing mesopores (2–50 nm) into Y zeolite increases its adsorption capacity for bulky sulfur compounds such as DBT and 4,6-DMDBT. Explain why, and state whether this is a chemical or a physical effect.

- **Rubric:** Physical effect. DBT and 4,6-DMDBT are similar in size to the Y zeolite pore openings (about 7.4 Å), so diffusion through the micropores is slow and many internal sites are not reached during an adsorption test. Mesopores shorten diffusion paths and give access to internal sites. The adsorption sites and binding mechanism are unchanged.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312; Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Table 2, diffusivities)

**Q6.** For a set of activated carbons tested for DBT removal from a model fuel, would you expect sulfur capacity to correlate better with micropore volume (pores below 2 nm) or with mesopore volume (pores of 2–50 nm)? Explain.

- **Rubric:** Micropore volume. DBT is about 9 Å across, and pores close to that size give overlapping attraction from opposite pore walls and much stronger adsorption than wider pores. Mesopores mainly provide transport to the micropores and affect adsorption rate more than capacity. Strong answers note that mesopores still matter for access, so the best carbons need both.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (capacity vs. micropore volume, Fig. S9)

**Q7.** Activated carbon can be made by pyrolyzing biomass to biochar under inert gas and then treating the char with steam at around 900 °C. Explain how the steam treatment creates porosity. Over a moderate range of activation, more intense activation raises the BET surface area but lowers the mass yield. Why, and does this trend continue indefinitely?

- **Rubric:** Steam gasifies carbon from the char (H<sub>2</sub>O + C → CO + H<sub>2</sub>), creating and widening pores by removing carbon from the framework. More activation removes more carbon, so yield drops while pore volume and surface area increase. The trend does not continue: with further activation, micropores widen into mesopores and macropores and pore walls collapse or merge, so micropore volume and surface area eventually decrease, and in the limit the carbon is consumed entirely. Bonus for noting that steam tends to widen pores earlier than CO<sub>2</sub>, giving a broader pore size distribution.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Introduction; §3.1)

**Q8.** Raman spectra of activated carbons show a D band near 1350 cm<sup>-1</sup> and a G band near 1580 cm<sup>-1</sup>. X-ray diffraction (Cu Kα) shows broad peaks near 24° and 43° 2θ. What does each of these features indicate about the carbon structure, and what does an increase in the ratio I<sub>D</sub>/I<sub>G</sub> indicate? If sharp, narrow XRD peaks also appear that cannot be assigned to carbon, what might they indicate?

- **Rubric:** G band: in-plane stretching of sp<sup>2</sup> graphitic carbon. D band: activated by defects and disorder in the carbon lattice. A higher I<sub>D</sub>/I<sub>G</sub> indicates a more disordered carbon; comparisons are most reliable within a series measured the same way. The broad XRD peaks near 24° (002) and 43° (100) come from carbon with little long-range order (amorphous or turbostratic). Sharp, narrow peaks not belonging to carbon indicate crystalline non-carbon phases, such as inorganic minerals left over from the feedstock.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Fig. 2, Table 3)

**Q9.** An activated carbon made from food waste was characterized as follows. Elemental analysis (ICP-OES) shows 2–3 wt% each of Na, Ca, K, and P. The XRD pattern shows sharp, narrow peaks in addition to the broad carbon peaks. Electron microscopy with elemental mapping (EDS) shows particles rich in these elements, up to about 100 nm across, on the carbon surface. What do these results together say about the form of these elements, and how might they affect sulfur adsorption?

- **Rubric:** The elements are present at least partly as crystalline inorganic particles (for example phosphates) dispersed on the carbon, not only as isolated ions or surface groups. Possible effects on sulfur adsorption: they may provide additional sites that bind sulfur compounds more specifically than the carbon surface (chemisorption), and they may increase disorder in the carbon structure. Strong answers note that these roles are proposed from correlation and are not directly proven, and that inorganic particles also add mass without adding pore volume.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Table 2, Figs. 1–2)

---

## Tier 2: Comparative Reasoning

Can the model predict relative performance between sorbents or adsorbates and justify it with the right structure-property relationship?

**Q10.** CuY (4.9 wt% Cu) and CeY (5.5 wt% Ce) zeolites are compared for removing BT from n-octane in the same fixed-bed setup. Which would you expect to bind BT more strongly and give the higher breakthrough capacity? Explain using the adsorption mechanism and the accessibility of the metal cations. What does this suggest about transition metal versus rare earth cations in Y zeolite more generally?

- **Rubric:** CuY should perform better on both counts. Cu<sup>+</sup> binds BT by π-complexation. Ce cations tend to sit at sites inside the sodalite cages and hexagonal prisms, which BT cannot enter, while Cu tends to occupy sites accessible from the supercage. Strong answers note that at similar wt% loading CuY contains about twice as many metal atoms as CeY because Ce is more than twice as heavy. Generalization: transition metals such as Cu tend to provide more accessible, strongly binding sites, while rare earths tend to migrate to inaccessible interior sites. Reference values: DFT ΔH<sub>ads</sub> of BT is -149 kJ/mol on CuY and -126 kJ/mol on CeY; breakthrough capacities were 65 mL/g (CuY) and 35 mL/g (CeY).
- **Source:** *Comput. Mater. Sci.* 2024, 235, 112813 (Table 4); Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Table 1, Discussion)

**Q11.** A bimetallic CuCeY zeolite gives a higher sulfur breakthrough capacity than either CuY or CeY. Propose an explanation.

- **Rubric:** The most supported explanation is site distribution: Ce preferentially occupies interior sites, so in the bimetallic material more Cu ends up at sites accessible to sulfur compounds, increasing the number of usable Cu<sup>+</sup> sites while the binding mechanism (π-complexation at Cu<sup>+</sup>) stays the same. Answers may also mention that DFT shows electron sharing between Cu and Ce, which may strengthen binding, but this should be presented as a possible contribution. Marked down for asserting a new, distinct bonding mechanism as established fact, or for simply averaging the two monometallic materials.
- **Source:** Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512; *Comput. Mater. Sci.* 2024, 235, 112813

**Q12.** DFT adsorption enthalpies for thiophene, BT, DBT, and 4,6-DMDBT generally become more negative with molecular size on HY and NaY zeolites (from about -50 to -100 kJ/mol). On CuY and CeY, the values for the same four molecules stay within about 10 kJ/mol of each other. Explain both trends.

- **Rubric:** On HY and NaY there is no strong specific binding site, so adsorption is dominated by interactions with the zeolite framework, mainly dispersion. Larger molecules have more atoms in contact with the framework, so they bind more strongly. On CuY and CeY, a strong, localized interaction between the metal cation and the adsorbate dominates (for Cu, π-complexation involving only part of the ring). This interaction is similar for all four molecules and much larger than the size-dependent framework contribution, so the size trend largely disappears.
- **Source:** *Comput. Mater. Sci.* 2024, 235, 112813 (Table 4 and discussion)

**Q13.** CuY and CeY zeolites were tested in the same fixed-bed setup with the same model fuel (BT in n-octane at the same sulfur concentration, flow rate, and bed size). Breakthrough capacities were 65 mL/g for CuY and 35 mL/g for CeY. After breakthrough, the outlet sulfur concentration rose much more steeply for CeY than for CuY. What does the difference in breakthrough curve shape indicate?

- **Rubric:** The slope of a breakthrough curve reflects the width of the mass transfer zone in the bed. A steep curve means a narrow zone: adsorption is fast relative to the flow, and/or the sites are fairly uniform with a favorable isotherm, so the bed is used efficiently up to breakthrough. A gradual curve means a broad zone, caused by slower mass transfer to the sites (diffusion, adsorption rate) and/or a range of site strengths. Full credit requires separating curve shape from capacity: shape describes how sharply the bed saturates, not how much it holds. Marked down for concluding from the slope alone that CeY simply "saturates faster" or has lower capacity.
- **Source:** Lee, K. X.; Tsilomelekis, G.; Valla, J. A. *Appl. Catal. B Environ.* 2018, 234, 130–142 (Discussion of breakthrough slopes)

**Q14.** DFT adsorption enthalpies on CuY are: thiophene -141, BT -149, DBT -143, 4,6-DMDBT -142, benzene -125, and naphthalene -143 kJ/mol. Based on these values, would you expect aromatic competition to be a bigger problem for desulfurizing gasoline (main sulfur compounds thiophene and BT, main competing aromatic benzene) or diesel (main sulfur compounds DBT and 4,6-DMDBT, main competing aromatic naphthalene)? What other factor would you need to consider?

- **Rubric:** Diesel. Benzene binds about 15–25 kJ/mol more weakly than thiophene and BT, giving some selectivity for gasoline sulfur compounds, while naphthalene binds about as strongly as DBT and 4,6-DMDBT, giving essentially no selectivity. The other key factor is concentration: aromatics are present at percent levels while sulfur compounds are at ppm levels, so even a moderate enthalpy advantage may not be enough to prevent aromatics from occupying most sites. Strong answers also note that enthalpies from single-site DFT models do not include diffusion or solvent effects.
- **Source:** *Comput. Mater. Sci.* 2024, 235, 112813 (Table 4 and discussion)

**Q15.** An activated carbon made from food waste had a higher 4,6-DMDBT capacity (about 10 mg S/g) than the best Cu- and Ce-exchanged mesoporous Y zeolite (about 7 mg S/g) in the same model fuel (100 ppmw S as 4,6-DMDBT with 1 wt% naphthalene in n-octane). The zeolite contains Cu and Ce cations placed at exchange sites to bind sulfur. The carbon has no exchanged cations but contains several wt% of Na, K, Ca, and P as inorganic particles, a BET surface area of about 900 m<sup>2</sup>/g, and a total pore volume of about 0.75 cm<sup>3</sup>/g, roughly twice that of the zeolite. Propose explanations for the carbon's higher capacity.

- **Rubric:** Should identify more than one factor. (1) Much larger pore volume and surface area, including micropores close to the size of 4,6-DMDBT, provide more physisorption capacity than the limited number of metal sites in the zeolite. (2) The inorganic species, which include metals (Na, K, Ca), may provide additional sites that bind sulfur compounds. (3) The zeolite's capacity is limited by the number of accessible metal sites and by diffusion of a bulky molecule through its pore system. Marked down for stating that the carbon has no metal-containing sites at all.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–2, Fig. 6); Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312

---

## Tier 3: Counterfactual and Edge Cases

Does the model avoid conclusions that sound reasonable but are not supported by the data or the chemistry?

**Q16.** A common proposal is that dibenzothiophene adsorbs on activated carbon by π–π stacking between its aromatic rings and the graphitic planes of the carbon. Would naphthalene, a common aromatic in diesel fuel, adsorb the same way? What does this imply for the selectivity of activated carbon for sulfur compounds?

- **Rubric:** Yes. Naphthalene is also a planar aromatic and would interact with graphitic planes in the same way, so it would compete for the same sites. If π–π stacking were the main mechanism, activated carbon would have little selectivity for sulfur compounds over aromatics, which are present at much higher concentrations in real fuels. Competition between aromatics and thiophenic compounds on activated carbon has been reported experimentally.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Discussion)

**Q17.** CuY, CeY, and CuCeY zeolites were reduced in H<sub>2</sub>, and XRD patterns taken afterward showed no peaks from crystalline Cu or Ce metal or oxide phases. A colleague concludes that the Cu and Ce species did not change during reduction. Is this conclusion justified? What would you use instead to check?

- **Rubric:** Not justified. XRD detects only crystalline phases with enough long-range order and crystallite size. Isolated cations at exchange sites, very small clusters, and disordered species give no distinct peaks, so a change in oxidation state or local environment can be invisible to XRD. Element-specific techniques should be used, such as X-ray absorption spectroscopy (XANES for oxidation state, EXAFS for local structure), XPS, or H<sub>2</sub> temperature-programmed reduction. In this case, XANES showed Cu<sup>2+</sup> reduced to Cu<sup>+</sup> and some Cu<sup>0</sup>, and Ce<sup>4+</sup> reduced to Ce<sup>3+</sup>.
- **Source:** Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512

**Q18.** Activated carbons were made from food waste by steam activation to mass yields between 65 and 25 wt%. Over this range, more activation gave a higher BET surface area, and the highest sulfur capacity was at 25 wt% yield. Sulfur capacity also increased with micropore volume across the series. A colleague proposes activating further, to 15 wt% yield, to increase capacity again. What would you expect, and why?

- **Rubric:** Should not expect further gains. As activation continues, pores widen and adjacent micropores merge, converting micropores into mesopores and macropores, so micropore volume and surface area eventually decrease. Much more of the carbon framework is also lost. Since capacity depends on micropore volume, it should drop. (Observed: at 15 wt% yield, micropore volume and surface area decreased and the carbon content fell by about half.) Full credit requires recognizing that the surface area trend reverses, not only citing the lower yield.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (§3.1)

**Q19.** Before pyrolysis, a food waste feedstock was washed five times with deionized water to remove soluble minerals. It was then pyrolyzed and steam activated to about 25 wt% mass yield. A colleague concludes that, because the minerals were washed out, inorganic species cannot play a meaningful role in the sulfur adsorption of the final carbon. Evaluate this reasoning.

- **Rubric:** Should reject it, for two reasons. (1) Washing removes only water-soluble salts. Insoluble mineral phases remain, as do elements bound within the biomass. (2) Pyrolysis and activation remove most of the carbon while inorganic elements are largely retained, so their concentration in the final carbon increases several-fold. Should propose measuring the inorganic content directly. Any suitable technique is acceptable, for example ICP-OES or ICP-MS, XRF, ash content by TGA, XRD for crystalline phases, or EDS mapping. (In this case the washed carbon still contained 2–3 wt% each of Na, Ca, K, and P.)
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Methods; Table 2)

**Q20.** Two activated carbons were made from different biomass under identical conditions and have similar BET surface areas and micropore volumes (0.25 and 0.26 cm<sup>3</sup>/g).

| | Carbon X | Carbon Y |
|---|---|---|
| Mesopore volume (cm<sup>3</sup>/g) | 0.50 | 0.30 |
| K (wt%) | 2.5 | 3.5 |
| Na (wt%) | 2.6 | 0.2 |
| Ca (wt%) | 2.1 | 1.0 |
| P (wt%) | 3.0 | 1.0 |
| DBT capacity (mg S/g) | 6.3 | 4.7 |

A researcher attributes carbon X's higher capacity to its K content. Is this supported? What do these data say about the role of micropore volume?

- **Rubric:** Not supported: carbon Y contains more K but has lower capacity, so K alone cannot explain the difference. Na, Ca, P, and mesopore volume are all higher in X, and with only two samples the data cannot separate their effects. A controlled test is needed, such as adding or removing one element at a time on the same carbon. On micropore volume: because the two carbons have nearly the same micropore volume, it does not explain the difference between them, but this does not mean micropore volume is unimportant. It remains a main factor for capacity, and other properties change capacity on top of it.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–2)

**Q21.** Three groups of activated carbons with similar BET surface areas (850–930 m<sup>2</sup>/g) were tested for DBT removal.

| Carbon | Raman I<sub>D</sub>/I<sub>G</sub> | Micropore volume (cm<sup>3</sup>/g) | Other features | DBT capacity (mg S/g) |
|---|---|---|---|---|
| Commercial | 1.1 | 0.16 | About 37 wt% O | 2.3 |
| Nut shell (two samples) | 1.8–2.0 | 0.28–0.29 | About 2 wt% K; little Na or P | 4.2–5.1 |
| Food waste | 2.9 | 0.25 | 2–3 wt% each of Na, Ca, K, P | 6.3 |

Are these results consistent with π–π stacking between DBT and graphitic carbon planes being the dominant adsorption mechanism? Explain.

- **Rubric:** No. If π–π stacking with graphitic planes dominated, the most graphitic carbon (lowest I<sub>D</sub>/I<sub>G</sub>, the commercial carbon) should adsorb the most, but it adsorbs the least, and the most disordered carbon adsorbs the most. Pore structure and composition explain the ranking better: the commercial carbon has by far the lowest micropore volume, and the best carbon has the most inorganic species. Strong answers note the limits of the comparison: graphitization and micropore volume vary together here, so the data argue against π–π stacking as the dominant factor but do not rule out some contribution.
- **Source:** *ACS Omega* 2025, 10, 42725–42734 (Tables 1–3)

---

## Tier 4: Diagnostic and Anomaly Explanation

Given a real experimental result that runs against a simple expectation, can the model reason from mechanism to explain it?

**Q22.** In situ X-ray absorption spectroscopy of CuY during reduction in H<sub>2</sub> shows that Cu<sup>2+</sup> is reduced to Cu<sup>+</sup>, and that small metallic Cu<sup>0</sup> clusters also form, which were not present before reduction. How would the formation of Cu<sup>0</sup> clusters affect sulfur adsorption by π-complexation, and what does this mean for choosing reduction conditions?

- **Rubric:** Cu<sup>0</sup> clusters reduce the number of active sites. Each Cu atom that ends up in a cluster is no longer an isolated Cu<sup>+</sup> cation at an exchange site, and most atoms in a cluster are not exposed to adsorbates. Metallic Cu also lacks the cationic character (empty 4s orbital) that makes Cu<sup>+</sup> a good σ-acceptor for π-complexation. Clusters may also partly block pores. So total Cu loading overstates the number of active sites. Reduction conditions involve a trade-off: they must be strong enough to convert Cu<sup>2+</sup> to Cu<sup>+</sup>, but harsher or longer reduction risks forming more Cu<sup>0</sup>. Strong answers note that when Cu<sup>+</sup> is reduced to Cu<sup>0</sup>, the framework charge must be balanced another way, for example by H<sup>+</sup>.
- **Source:** Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512 (XANES and EXAFS of CuY)

**Q23.** In bimetallic Cu–Ce Y zeolites, Rietveld refinement of XRD data assigned Ce cations mainly to sites in the sodalite cages (SI′ and SII′), which DBT cannot enter, and Cu cations mainly to site SII, which is accessible from the supercage. Yet adding Ce to CuY increased DBT capacity. Propose explanations, and comment on how firmly the refinement supports the assumption that Ce is inaccessible.

- **Rubric:** Possible explanations: (1) Ce occupying interior sites changes where Cu goes, so more Cu ends up at accessible sites; (2) an electronic interaction between Ce and nearby Cu through the framework may strengthen Cu binding (DFT shows electron sharing between Cu and Ce). On the refinement: it fits electron density at each cation site and has difficulty telling different cations apart at partially occupied sites. A site assigned to Cu may also hold some Ce, so some Ce may be accessible and contribute directly. The refinement shows a preference, not a strict exclusion. Full credit requires at least one indirect mechanism and recognition of the limits of the siting evidence.
- **Source:** Lee, K. X. et al. *J. Phys. Chem. C* 2021, 125, 9107–9118; Sokol, H. J. et al. *J. Phys. Chem. C* 2022, 126, 1496–1512; *Comput. Mater. Sci.* 2024, 235, 112813

**Q24.** Bimetallic Cu–Ce mesoporous Y zeolites were prepared with different target metal loadings and tested for 4,6-DMDBT removal (100 ppmw S as 4,6-DMDBT with 1 wt% naphthalene in n-octane). Measured metal contents (ICP) and results:

| Target loading | Measured Cu (wt%) | Measured Ce (wt%) | 4,6-DMDBT capacity |
|---|---|---|---|
| 2% Cu, 2% Ce | 1.7 | 1.6 | Baseline |
| 5% Cu, 2% Ce | 2.8 | 1.8 | Lower than baseline |
| 10% Cu, 2% Ce | 2.7 | 1.7 | Lower than baseline |
| 2% Cu, 5% Ce | 1.4 | 5.7 | Higher than baseline |
| 2% Cu, 10% Ce | 0.9 | 8.0 | Highest (about 50 mL/g) |

The best sorbent contains the least Cu. Explain what these data show.

- **Rubric:** Should make these points. (1) Target loadings are misleading; only measured contents should be compared. Cu uptake levels off near 2.7–2.8 wt%, indicating the exchange capacity available to Cu is reached. (2) Cu and Ce compete for the same limited exchange sites, so adding more Ce displaces Cu. (3) Capacity rose while Cu fell, so Cu content alone does not control capacity. Ce contributes, either by binding sulfur compounds directly or by influencing where the remaining Cu sits and how accessible it is. (4) The lower capacity at higher Cu could come from Cu in less useful positions or extra-framework species, but the data do not identify the cause, and answers should present this as a hypothesis.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Table 3, Fig. 10)

**Q25.** A bimetallic Cu–Ce mesoporous Y zeolite was used to adsorb 4,6-DMDBT from n-octane. It was then regenerated by heating in air at 500 °C for 5 h, followed by heating in H<sub>2</sub> at 400 °C for 5 h, and recovered nearly all of its original capacity over two cycles. A colleague concludes that 4,6-DMDBT must be weakly and reversibly bound. Evaluate this conclusion.

- **Rubric:** Should reject it. Full recovery after this treatment says nothing about binding strength, because the procedure does not rely on the sulfur compound desorbing. Heating in air burns off the adsorbed organosulfur compounds and oxidizes Cu<sup>+</sup> back to Cu<sup>2+</sup>; the H<sub>2</sub> step then reduces Cu<sup>2+</sup> to the active Cu<sup>+</sup>. The sites are chemically reset. The need for such harsh conditions is itself consistent with strong binding. Strong answers note that two cycles is limited evidence for long-term stability, and mention possible degradation routes such as residual sulfate, loss of porosity, or metal migration.
- **Source:** Lee, K. X. et al. *Ind. Eng. Chem. Res.* 2019, 58, 18301–18312 (Methods; Figs. 11–12)

**Q26.** Biodiesel containing 212 ppm sulfur was passed through a fixed bed of commercial activated carbon. The first 0.5 mL of effluent already contained about 40 ppm S, after which the outlet concentration rose slowly to saturation at about 12 mL/g. The capacity from the breakthrough curve (about 1.1 mg S/g) was half the maximum capacity from batch isotherms with the same carbon (2.2 mg S/g). Gas chromatography with a sulfur-selective detector showed that the first effluent sample contained the same light and heavy sulfur compounds as the feed, at lower concentrations. What does this tell you about why sulfur appeared so early, and why is the fixed-bed capacity lower than the batch capacity?

- **Rubric:** The early sulfur is not from a subset of compounds that cannot adsorb; if it were, the first effluent would contain only those compounds. Since all compounds appear at reduced concentration, all of them adsorb, but not fast enough to be fully captured in the available contact time. This points to mass transfer (diffusion) limitations and a broad mass transfer zone. The lower fixed-bed capacity reflects incomplete use of the bed: short contact time and slow access to smaller or less accessible pores, and possibly flow channeling, compared with long contact time and good mixing in batch tests. Bonus for noting that biodiesel's higher viscosity slows diffusion.
- **Source:** Sokol, H. J. PhD Dissertation, Ch. 7 (Figs. 54–55)

**Q27.** Commercial activated carbon used to adsorb sulfur from biodiesel was regenerated by heating under argon. Heating at 100 or 200 °C removed no sulfur. At 400 °C, the total pore volume dropped by about 25% after the first adsorption and regeneration cycle but did not drop further in later cycles. The sulfur left in the carbon rose from 40 ppm (fresh) to 123 ppm after one cycle and 157 ppm after two. The carbon still kept 83% of its original sulfur capacity in the third cycle. Explain how sulfur can accumulate and pore volume can drop while most of the capacity is retained.

- **Rubric:** Part of the adsorbed sulfur is held too strongly, or is in compounds too heavy to evaporate, to be removed by heating in an inert gas at 400 °C, so it accumulates. The slowing accumulation suggests a limited set of strong sites or traps that fill up. The first-cycle loss of pore volume suggests partial pore blocking by residues or a structural change that then stabilizes. Because most of the capacity comes from the large remaining pore surface, most of it is retained. Strong answers note that no removal at 100–200 °C shows the adsorbed compounds are not simply volatile and weakly held, and that heating in an inert gas cannot burn off heavy organosulfur compounds; an oxidizing step would remove more but would also consume carbon.
- **Source:** Sokol, H. J. PhD Dissertation, Ch. 7 (Table 23, Fig. 57)
