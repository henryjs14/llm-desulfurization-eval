# Grader comparison: claude-opus-5-5 vs. gpt-6.1-sol

Answers graded by both: 125

- Same grade: 103 (82%)
- Cohen's kappa: 0.70
- Full vs. Incorrect (largest disagreements): 0

## Grade pairs

Rows: claude-opus-5-5. Columns: gpt-6.1-sol.

| | Full | Partial | Incorrect |
|---|---|---|---|
| Full | 40 | 16 | 0 |
| Partial | 2 | 52 | 3 |
| Incorrect | 0 | 1 | 11 |

## Average score by model

Full = 1, Partial = 0.5, Incorrect = 0.

| Model | claude-opus-5-5 | gpt-6.1-sol | Difference |
|---|---|---|---|
| claude-fable-5-1 | 0.70 | 0.60 | +0.10 |
| gemini-4-argon | 0.72 | 0.60 | +0.12 |
| gpt-6-astra | 0.72 | 0.70 | +0.02 |
| gpt-6-luna | 0.60 | 0.54 | +0.06 |
| gpt-6.1-sol | 0.64 | 0.62 | +0.02 |

## Disagreements

### Q2, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** The answer states that Na⁺ has no d electrons and so cannot back-donate into DBT's π* orbitals or form a π-complex. It identifies cation–π electrostatic interaction with Na⁺ and dispersion forces with the zeolite framework as the interactions holding DBT on NaY, which covers every required rubric point. The additional points on ion–dipole and induction effects are reasonable and contain no factual errors.

**gpt-6.1-sol:** The answer correctly identifies the absence of Na⁺ valence d electrons and back-donation, and names both cation–π electrostatics and framework dispersion as the adsorption interactions. However, its stated Na⁺ configuration, “[Ne] 2s²2p⁶,” is incorrect: Na⁺ is [Ne], or 1s²2s²2p⁶, so the answer contains a factual error in supporting detail.

### Q3, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** The answer explains that Al³⁺ substituting for Si⁴⁺ creates a net negative framework charge. It notes this charge is balanced by extra-framework cations that can be exchanged, including metal cations such as Cu²⁺, though it never explicitly says these cations then act as adsorption sites. It also gives the stronger point that Si/Al ratio sets exchange capacity, with no factual errors.

**gpt-6.1-sol:** The answer correctly explains that Al³⁺ substitution for Si⁴⁺ creates negative framework charge balanced by exchangeable extra-framework cations, and it connects Al content to exchange capacity. However, it does not state the required functional consequence that exchanging in metal cations introduces adsorption sites.

### Q5, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** The answer commits to micropore volume and justifies it with DBT's molecular size (about 0.8–1.2 nm) and the overlapping wall potentials in pores of similar width. It also states that mesopores mainly serve as transport arteries affecting kinetics rather than capacity, which covers every required rubric point. Its note that mesopores remain important for transport also touches the 'strong answer' point.

**gpt-6.1-sol:** The answer correctly predicts stronger correlation with micropore volume, explains overlapping adsorption potentials in molecule-sized pores, and identifies mesopores primarily as transport pathways. However, its claim that mesopores shorten breakthrough times is incorrect as a general statement: improved transport and micropore accessibility generally delay breakthrough by improving bed utilization.

### Q6, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** For (a), the answer explains that steam gasifies carbon (C + H₂O → CO + H₂), which opens, widens and creates pores. For (b), it links greater carbon removal to lower yield and higher surface area, and states the trend does not continue indefinitely: micropores widen to meso/macropores, walls collapse, and surface area falls, with burn-off eventually consuming the particle down to ash. All rubric points are addressed with no significant errors.

**gpt-6.1-sol:** The answer correctly explains steam gasification, pore creation and widening, decreasing yield, and the eventual decline in BET area through pore coalescence and wall collapse. However, it does not state that micropore volume eventually decreases or that carbon is fully consumed in the limit, and its categorical claim that activation is kinetically controlled rather than diffusion-limited is not generally valid.

### Q8, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** For (a), the answer concludes that the elements are present as a separate crystalline inorganic phase, most likely phosphates, dispersed as particles on the carbon. For (b), it identifies these particles as additional chemisorption/reactive sites for sulfur species, and it also notes the added non-porous mass that lowers capacity per gram. It does not explicitly flag these roles as unproven hypotheses, but that point is not required for full credit.

**gpt-6.1-sol:** The answer correctly identifies crystalline inorganic particles, plausibly phosphates, and proposes additional chemisorption sites for sulfur compounds. However, it incorrectly treats the ICP-OES concentrations as ruling out atomically dispersed species and asserts crystallite sizes from XRD without quantitative peak-width data; the evidence establishes that at least some, not necessarily all, of these elements occur in crystalline particles.

### Q17, claude-fable-5-1: Partial vs. Full

**claude-opus-5-5:** The answer predicts 'yes' and covers both required points: washing removes only soluble salts while insoluble or bound minerals remain, and the ~25% yield concentrates the retained inorganics roughly fourfold. However, it contains a supporting factual error. Its conclusion that washing 'removes mostly Na' contradicts the case result, where the washed carbon still held 2–3 wt% Na alongside Ca, K and P.

**gpt-6.1-sol:** The answer clearly predicts significant residual inorganic content and explains both required mechanisms: washing removes only water-soluble minerals, while insoluble or biomass-bound elements remain, and pyrolysis/activation concentrates retained inorganics several-fold at a 25 wt% yield. It also explicitly connects those residual elements to sulfur adsorption.

### Q22, claude-fable-5-1: Full vs. Partial

**claude-opus-5-5:** The answer covers all four rubric points. It says nominal loadings mislead and identifies the Cu plateau near 2.7–2.8 wt% as exchange-site saturation. It attributes the Cu drop to competitive displacement by Ce, and notes that capacity rose as Cu fell, with Ce as the main contributor through direct S binding. It offers several candidate explanations for the poorer high-Cu samples (oxide clusters, aromatic inhibition) rather than one proven cause, which reasonably meets the hypothesis-framing requirement.

**gpt-6.1-sol:** The answer correctly emphasizes measured loadings, Cu uptake saturation, Cu–Ce exchange competition, and the fact that capacity does not depend on Cu content alone. However, it asserts specific Cu oxide/blocking and Ce adsorption mechanisms, and concludes that Ce is the active component, without acknowledging that the data cannot distinguish direct Ce binding from changes in Cu location or accessibility. The cause of poorer performance at higher Cu content must remain a hypothesis.

### Q2, gemini-4-argon: Full vs. Partial

**claude-opus-5-5:** The answer says Na⁺ has no d electrons, so it cannot back-donate into DBT's π* orbitals or form a π-complex. It attributes adsorption on NaY to weaker cation–π/electrostatic interactions with Na⁺ and dispersion forces with the zeolite framework, which covers all required points. Saying Na⁺ 'lacks d-orbitals entirely' is imprecise, since empty high-energy 3d orbitals exist, but the key point that there are no filled d orbitals for back-donation is correct.

**gpt-6.1-sol:** The answer correctly identifies the absence of Na⁺ valence d electrons needed for back-donation and attributes NaY adsorption to cation–π electrostatics and framework dispersion. However, its claim that Na⁺ lacks d orbitals entirely is incorrect: it lacks occupied valence d orbitals, not d orbitals altogether.

### Q6, gemini-4-argon: Full vs. Partial

**claude-opus-5-5:** The answer states that steam gasifies carbon (C + H2O → CO + H2), creating and widening pores, and that greater activation removes more carbon, lowering yield and raising surface area. It also says the trend is not indefinite: walls burn through, micropores merge into meso- and macropores and collapse, surface area falls, and in the limit the carbon is fully gasified. All required rubric points are covered without errors.

**gpt-6.1-sol:** The answer covers the required gasification reaction, carbon removal and yield loss, initial surface-area increase, and eventual pore widening, merging, collapse, and complete carbon consumption. However, the claim that escaping product gases help “wedge open” the carbon structure introduces an incorrect supporting mechanism; porosity develops through carbon removal rather than gas-driven mechanical opening.

### Q8, gemini-4-argon: Full vs. Partial

**claude-opus-5-5:** (a) The answer identifies the elements as crystalline inorganic nanoparticles, such as phosphates and carbonates, dispersed on the carbon rather than as atomically dispersed or organically bound species. (b) It proposes that these particles add basic sites that chemisorb sulfur species. It also notes that the non-porous ash adds dead weight, but it does not frame the roles as unproven hypotheses; that point is not required.

**gpt-6.1-sol:** The answer correctly identifies crystalline inorganic particles dispersed on carbon and their potential to provide sulfur-binding chemisorption sites. However, it incorrectly equates the summed elemental concentrations with total ash content and overstates the evidence by claiming XRD proves these particular elements form crystalline phases; the data support their presence at least partly in such particles, not the exclusion of other chemical forms.

### Q11, gemini-4-argon: Partial vs. Incorrect

**claude-opus-5-5:** The HY/NaY explanation matches the rubric: with no strong specific site, framework dispersion dominates and grows with molecular size. For CuY/CeY, the answer attributes the narrow range to steric weakening of S–M bonding being offset by rising dispersion, rather than to a strong, localized cation interaction (partial-ring π-complexation for Cu) that is similar for all four adsorbates and swamps the size-dependent framework term. That misses the rubric's key mechanism for the second trend.

**gpt-6.1-sol:** The HY/NaY explanation correctly attributes stronger adsorption of larger molecules to increased framework dispersion. However, the answer explains the CuY/CeY trend through steric weakening of S–metal bonding compensated by increasing dispersion, rather than the required dominant, localized cation–adsorbate interaction that is similar across all four adsorbates and overwhelms the size-dependent framework contribution.

### Q14, gemini-4-argon: Full vs. Partial

**claude-opus-5-5:** The answer covers all three rubric factors. It credits the carbon's larger pore volume and surface area, with micropores of about 0.9–1.5 nm suited to 4,6-DMDBT, for greater physisorption capacity, and it treats the Na/K/Ca/P inorganic particles as additional binding sites. It attributes the zeolite's limit to its finite Cu/Ce sites, which naphthalene saturates and 4,6-DMDBT can reach only with steric hindrance, and to constrained pore access and mass transfer for the bulky adsorbate.

**gpt-6.1-sol:** The answer identifies greater physical adsorption capacity, appropriately sized micropores, possible sulfur binding at inorganic species, and diffusion constraints in the zeolite. However, it does not clearly identify the limited number of accessible exchanged-metal sites as a constraint on zeolite capacity, a required rubric point.

### Q21, gemini-4-argon: Full vs. Partial

**claude-opus-5-5:** The answer concludes that Cu⁰ clustering reduces the number of accessible active sites. It attributes this to lost isolated Cu⁺ sites and reduced dispersion, and notes that Cu⁰ lacks the empty s-orbital acceptor configuration needed for π-complexation. It also covers partial pore blockage. The extra discussion of reactive sulfidation is supplementary and does not undermine its main conclusion that adsorption capacity falls.

**gpt-6.1-sol:** The answer correctly identifies loss of isolated Cu⁺ π-complexation sites, loss of the empty-s-orbital electronic configuration, and possible pore blockage. However, it does not explicitly explain that most Cu atoms within clusters are inaccessible to adsorbates or draw the required conclusion that total Cu loading therefore overstates the number of active sites.

### Q4, gpt-6-astra: Full vs. Partial

**claude-opus-5-5:** For (a), the answer says exchange and calcination leave Cu²⁺, that H₂ reduction gives Cu⁺, and that Cu⁺ (3d¹⁰) binds thiophene by σ/π donation plus d→π* back-donation. It does not spell out the 3d⁹ configuration or vacant 4s orbital, but its contrast with Cu²⁺ covers the required point. For (b), it correctly cites Cu⁺ disproportionation in water and the poor solubility of Cu(I) salts.

**gpt-6.1-sol:** The answer correctly explains reduction to Cu⁺, its filled 3d¹⁰ shell and back-donation, and both aqueous Cu⁺ disproportionation and poor Cu(I) salt solubility. However, it omits the required explanation that Cu²⁺ is 3d⁹ and a poor back-donor because of its higher charge and partially filled d shell, and it does not identify the vacant Cu⁺ 4s orbital responsible for σ-acceptance.

### Q5, gpt-6-luna: Full vs. Partial

**claude-opus-5-5:** The answer commits to micropore volume and explains that overlapping potentials from opposing walls in pores sized to fit DBT strengthen adsorption. It also states that mesopores mainly provide transport and affect rate rather than capacity. It omits the ~9 Å figure but conveys the size-matching concept through 'suitably sized' micropores and excluding ultramicropores too narrow for DBT.

**gpt-6.1-sol:** The answer correctly predicts a stronger correlation with accessible micropore volume, explains overlapping wall potentials, and distinguishes mesopore transport effects from capacity. However, it omits the required approximate DBT molecular dimension of 9 Å and the explicit connection to pores of comparable width.

### Q6, gpt-6-luna: Full vs. Partial

**claude-opus-5-5:** Part (a) gives the C + H₂O → CO + H₂ gasification and explains that removing framework carbon creates and widens pores. Part (b) links burn-off to lower yield and higher surface area, and states the trend is not indefinite because pores widen and merge and walls are removed, so micropore volume and surface area decline while yield keeps falling. That falling yield implies the rubric's full-consumption limit, though the answer does not state it explicitly.

**gpt-6.1-sol:** The answer correctly explains steam gasification, pore creation and widening, and the moderate-activation tradeoff between surface area and yield. It also identifies pore widening and merging during overactivation, but does not state that carbon is fully consumed in the limit and describes the eventual surface-area decrease only as a possibility.

### Q10, gpt-6-luna: Partial vs. Incorrect

**claude-opus-5-5:** The answer leads with complementary Cu and Ce sulfur binding sites, which is not the rubric's explanation, and never states that Ce occupies interior sites so that more Cu⁺ sits at accessible sites, or that π-complexation at Cu⁺ remains the mechanism. It does mention improved dispersion and more accessible active sites, which points toward the correct idea, but only as one possibility among several. Its framing of the Cu–Ce electronic interaction as a possible effect is acceptable.

**gpt-6.1-sol:** The answer identifies complementary Cu/Ce sulfur binding and possible redox chemistry as its main explanation, rather than the rubric-supported cation distribution. Its generic discussion of dispersion and accessibility does not explain that Ce preferentially occupies interior sites, leaving more accessible Cu⁺ sites while retaining the same π-complexation mechanism.

### Q3, gpt-6.1-sol: Full vs. Partial

**claude-opus-5-5:** The answer explains that substituting Al³⁺ for Si⁴⁺ creates a net negative framework charge, balanced by extra-framework cations that can be exchanged for others from solution. Its Na⁺/Ca²⁺ example shows metal cations being introduced this way, though it does not explicitly call them adsorption sites. It also gives the stronger point that a lower Si/Al ratio raises the maximum exchange capacity.

**gpt-6.1-sol:** The answer correctly explains Al³⁺ substitution for Si⁴⁺, the resulting negative framework charge, and exchange of extra-framework charge-balancing cations; it also relates Si/Al ratio to exchange capacity. However, it omits the required point that ion exchange allows metal cations to be introduced as adsorption sites.

### Q9, gpt-6.1-sol: Partial vs. Incorrect

**claude-opus-5-5:** The answer leans toward CuY via Cu(I) π-complexation and correctly notes that CuY has about 2.2 times as many metal atoms, but it explicitly refuses to commit to CuY on both counts. It never states that Ce preferentially occupies inaccessible sodalite and hexagonal-prism sites while Cu sits at supercage-accessible sites. It also declines to draw the transition-metal versus rare-earth conclusion asked for in (c).

**gpt-6.1-sol:** The answer rejects the required conclusion that CuY binds BT more strongly and has higher breakthrough capacity, offering it only conditionally. Although it correctly describes Cu(I) π-complexation and the metal atom-count advantage, it does not identify Ce’s preferential occupation of inaccessible sodalite-cage and hexagonal-prism sites versus Cu’s accessible supercage sites, and it rejects the rubric’s transition-metal versus rare-earth trend.

### Q14, gpt-6.1-sol: Full vs. Partial

**claude-opus-5-5:** The answer cites several factors. It covers greater accessible pore volume and surface area, including suitable micropores and mesopores, with physisorption on the carbon framework (point 1). It notes that the zeolite is limited by cation accessibility, narrow windows and the bulky adsorbate (point 3), and lists the Na/K/Ca/P phases as a possible contributor to local adsorption sites without claiming the carbon lacks metal species (point 2, though heavily hedged).

**gpt-6.1-sol:** The answer explains greater accessible pore space and physisorption, as well as diffusion and accessibility limitations on zeolite metal sites. However, it does not identify Na-, K-, and Ca-containing inorganic species as possible additional sulfur-binding sites, instead discussing indirect effects and emphasizing that sulfur-specific binding is unproven.

### Q19, gpt-6.1-sol: Incorrect vs. Partial

**claude-opus-5-5:** The answer's headline ('Not directly') and final conclusion ('direct participation... is unsupported') adopt the invited conclusion that the site assignment rules out direct Ce adsorption. It notes in passing that a minority of Ce might be accessible but dismisses this. It also misses the key rubric point that Rietveld refinement cannot reliably distinguish Ce from Cu at partially occupied sites, so the Cu-assigned SII site may itself hold Ce.

**gpt-6.1-sol:** The answer acknowledges that some Ce could occupy accessible sites and interact directly with DBT, so it does not strictly exclude direct adsorption. However, it omits the required explanation that Rietveld refinement has limited ability to distinguish cation species at partially occupied sites, meaning sites assigned to Cu may also contain Ce.

### Q20, gpt-6.1-sol: Partial vs. Full

**claude-opus-5-5:** The answer puts the commercial carbon lowest and mentions its much smaller micropore volume, and it weighs the food-waste carbon's minerals against the nut shells' larger micropore volume, so its direction is correct. But it does not commit: it calls the ranking a provisional working hypothesis, makes commercial-lowest conditional on an oxygen interpretation, and concludes that only A ≈ B is defensible.

**gpt-6.1-sol:** The answer ranks commercial lowest based on its markedly smaller micropore volume rather than favoring it for greater graphitization. Its ranking of the nut shell carbons above food waste is acceptable and justified by their larger micropore volumes, while acknowledging that inorganic species could provide additional DBT-binding sites.

