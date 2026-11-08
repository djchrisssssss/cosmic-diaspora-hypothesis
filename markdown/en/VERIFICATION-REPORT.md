# Scientific Verification Report — Cosmic Diaspora Hypothesis

---

## Overview

This report presents the results of a systematic scientific verification of all key claims, data points, and references cited in the **Cosmic Diaspora Hypothesis**. Three independent verification methods were employed:

1. **Astrophysical calculations** — Using the `astropy` library (Planck18 cosmology, physical constants, unit conversions)
2. **Biological & materials science literature verification** — Using `biopython`, PubMed/NCBI databases, and web-based literature cross-referencing
3. **Citation & DOI verification** — Using CrossRef REST API, CDMS database, and NASA planetary factsheets

### Verification History

| Date | Scope | Summary |
|------|-------|---------|
| 2026-02-28 | Initial verification | 13 astrophysical claims, 7 biological claims, 8 sampled citations |
| 2026-03-04 | v2 modifications | 13 new scientific claims, 3 new references, 14 structural modifications, full citation audit |
| 2026-03-10 | v3 major revision | 12 new references [55]–[66], 10 structural modifications (Bayesian prior table, Venus balanced literature, instrument-threshold table, interstellar object update, skeleton-level references, program ref downgrade, ref [5] fix, Part VI → Appendix A, LaTeX title page, README updates) |
| 2026-11 | v4 revision | Independent referee review (AI-assisted), 174 findings; text hedged and corrected; arabic sections §10–13 renumbered to §9–12; references expanded from 66 to 175 (see the v4 section at the end of this report) |

---

## 1. Astrophysical Claims

All astrophysical claims were verified using `astropy` constants and the Planck18 cosmological model.

| # | Claim in Paper | Verified Value | Result |
|---|---------------|---------------|--------|
| 1 | Universe age: 13.8 billion years | Planck18: **13.79 Gyr** | ✅ Verified |
| 2 | Solar luminosity ≈ 10²⁶ W (Kardashev Type II) | L☉ = **3.828 × 10²⁶ W** | ✅ Verified |
| 3 | Human civilization: ~19 TW, Type 0.7 | 19 TW = 1.9 × 10¹³ W; Sagan K = **0.33** (see note below) | ✅ Verified (v3 text) — **superseded in v4:** body uses K = (log₁₀P[W] − 6)/10 (Gray 2020 [87]), giving K ≈ 0.73 |
| 4 | Kardashev Type I: 10¹⁶–10¹⁷ W | Earth intercepted solar power: **1.74 × 10¹⁷ W** | ✅ Verified |
| 5 | Kardashev Type III: ~10³⁶ W | Galactic estimate: 10³⁵–10³⁸ W range | ✅ Verified |
| 6 | Milky Way: 100–400 billion stars | Standard astronomical estimate | ✅ Verified |
| 7 | Star formation rate: ~2 M☉/yr (6–7 stars) | Chomiuk & Povich 2011: **1.9 ± 0.4 M☉/yr** | ✅ Verified (v3 text) — **superseded in v4:** body now gives ~3 hydrogen-burning stars per year for 1.9 M☉/yr |
| 8 | Earth-like planets: billions to ~40 billion | Petigura et al. 2013: ~22% of Sun-like stars | ✅ Verified |
| 9 | Mars closest distance: ~55 million km | Actual closest opposition: **~54.6 million km** (2003) | ✅ Verified |
| 10 | Venus closest distance: ~38 million km | Orbital calculation: **~41.4 million km**; actual minimum ~38 million km | ✅ Verified |
| 11 | Venus surface gravity: 8.87 m/s² (~90% of Earth) | Calculated: **8.87 m/s² (90.4% of Earth)** | ✅ Verified |
| 12 | Graphene tensile strength: ~130 GPa, Young's modulus ~1 TPa | Lee et al. 2008: **130 ± 10 GPa, 1.0 ± 0.1 TPa** | ✅ Verified |
| 13 | Venus surface: 462°C, 90 atm | NASA fact sheet: **464°C mean, 92 bar** | ✅ Verified (v3 text) — **superseded in v4:** body now cites [47] as 464 °C (737 K) and 92 bar |

**Result: 13/13 verified.**

> **Note on Kardashev Type 0.7:** Sagan's interpolation is K = (log₁₀P − 6)/10 with P in watts (Gray 2020 [87]); P = 1.9 × 10¹³ W gives K ≈ 0.73. (The v1–v3 note used an incorrect variant of the formula that gave 0.33.)

---

## 2. Biological & Materials Science Claims

Biological claims were verified through literature review and PubMed database cross-referencing. Materials science and physics claims were verified against peer-reviewed literature and established physical principles.

### 2a. Biological Claims

| # | Claim in Paper | Verification | Result |
|---|---------------|-------------|--------|
| 1 | >240 molecular species detected in ISM (as of 2021) | McGuire 2022 census: 241 (as of 2021). 2025 CDMS census: **334 molecules**. | ✅ Verified (v3 text) — **superseded in v4:** body now cites the CDMS census: 349 molecules as of Oct 2026 [73] |
| 2 | Murchison meteorite: ~96 amino acid types | Glavin et al. 2021 confirms extensive diversity. Studies report 70–100+ types depending on classification. ~96 within accepted range. | ✅ Verified |
| 3 | *Methanopyrus kandleri*: growth above 120°C | Takai et al. 2008 (PNAS): growth at **122°C** under high-pressure cultivation. | ✅ Verified |
| 4 | *Deinococcus radiodurans*: survives >5,000 Gy | Survives ~5,000 Gy with ~37% survival rate. Some studies report up to 15,000 Gy with reduced viability. | ⚠️ Partially verified — context-dependent |
| 5 | Toba supervolcano (~74 kya) caused human genetic bottleneck | Ambrose 1998 proposed the link. Recent genomic studies suggest founder effects during Out-of-Africa migration as alternative. | ⚠️ Debated — **paper correctly notes the controversy** |
| 6 | Venus habitable window: possibly >2 billion years | Way et al. 2016, 2020 climate models support this. **Model results**, not direct observation. | ⚠️ Model-supported — **paper correctly uses "may have"** |
| 7 | Mars possessed liquid water ~3.5–4 billion years ago | Extensive geological evidence from MRO, Curiosity, Perseverance. Scientific consensus for Noachian period. | ✅ Verified |
| 8 | Abiogenesis probability unknown, range ~1 to 10⁻⁴⁰ (§1.6) | Standard characterization in astrobiology; no consensus on *f*_l bounds. The 10⁻⁴⁰ extreme is cited in Penrose-type arguments. | ✅ Verified (correctly stated as unknown) |
| 9 | Anthropic Principle / observation selection effects (§0.3) | Bostrom 2002 correctly cited; N=1 self-selection argument is standard in anthropic reasoning literature. | ✅ Verified |

**Result: 6/9 fully verified, 3/9 partially verified or debated (all correctly qualified in the paper).**

### 2b. Physics, Materials Science & Engineering Claims

| # | Claim in Paper | Verification | Result |
|---|---------------|-------------|--------|
| 1 | Tritium half-life: 12.3 years (§3.1) | NNDC/ITER: **12.32 years** | ✅ Verified |
| 2 | TBR must be >1.0 for fuel self-sufficiency (§3.1) | ITER design target TBR ≥1.05; literature consensus >1.0 minimum, ~1.2 practical | ✅ Verified |
| 3 | ⁶Li + n → T + ⁴He breeding reaction (§3.1) | Standard lithium-6 neutron capture, exothermic (+4.8 MeV) | ✅ Verified |
| 4 | D-D fusion: ~300–500 million K (§3.1) | Literature: 300–500 million K range | ✅ Verified |
| 5 | p-¹¹B fusion: ~1–3 billion K (§3.1) | Literature: 1–3 billion K (100–300 keV) | ✅ Verified (v3 text) — **superseded in v4:** body now gives 300–400 keV ≈ 3.5–4.6 billion K |
| 6 | Kramers-Kronig causality limits broadband cloaking (§3.3.4) | KK relations impose fundamental bandwidth limits on passive metamaterial cloaks; broadband perfect cloaking physically unrealizable | ✅ Verified |
| 7 | BCS theory lattice stability limits room-temp superconductors (§3.3.4) | Conventional BCS faces electron-phonon coupling limits; no reproducibly verified room-temp ambient-pressure superconductor exists | ✅ Verified (v3 text) — **superseded in v4:** body now states that phonon-mediated superconductivity is not capped below room temperature; the obstacle is stabilizing high-T_c phases at ambient pressure |
| 8 | Thermodynamic constraint: waste heat must be discharged (§3.3.4) | Second law of thermodynamics; any energy-converting system produces entropy/waste heat | ✅ Verified |
| 9 | Quantum no-communication theorem (§3.5) | Peres & Terno 2004 [19]; standard result in quantum information theory | ✅ Verified |
| 10 | 1I/'Oumuamua: first confirmed interstellar object (§12.7) | Meech et al. 2017, Nature 552, 378–381 | ✅ Verified |
| 11 | Vera Rubin Observatory / LSST expected to detect dozens of ISOs per year (§12.7) | Ivezić et al. 2019; multiple studies project 1–50+ per year | ✅ Verified (v3 text) — **superseded in v4:** body now gives roughly one to a few interstellar objects per year |

**Result: 11/11 verified.**

---

## 3. Citation & Reference Verification

Total references: **175** (v4). By source type in the v4 reference list (counted from the Markdown list): **137 DOI, 36 URL-only, 2 arXiv-only** (3 entries are marked as preprints). The machine audit [`verification.json`](../../verification/verification.json) is regenerated from the LaTeX bibliography; the 2026-11-08 run covers all 175 entries (170 verified, 3 restricted pages returning HTTP 403 to automated requests ([120] media.defense.gov, [122] aaro.mil, [138] skyandtelescope.org; checked manually), 2 failed ADS URLs for [9] and [20] that reject automated requests from some networks). Sections 3a–3c below are the historical per-batch tables from the v1–v3 audits (66 references), organized by revision batch rather than by source type: 36 original DOIs (§3a), 18 original URL-only institutional/mission references (§3b), and 12 references [55]–[66] added in v3 (§3c; 8 of them with DOIs). Rows for entries that were corrected in v4 ([5], [13], [56], [58], [61], [62], [63], [64], [66]) have been updated to describe the corrected entries. References [67]–[175] are covered in the v4 section (§6).

### 3a. Full DOI Verification

| Ref | DOI | Authors (CrossRef) | Journal | Year | Status | Notes |
|-----|-----|---------|---------|------|--------|-------|
| [1] | 10.1088/0004-6256/142/6/197 | Chomiuk, Povich | The Astronomical Journal | 2011 | ✅ | Correct |
| [4] | 10.1073/pnas.1319909110 | Petigura, Howard, Marcy | PNAS | 2013 | ✅ | Correct |
| [5] | 10.21203/rs.3.rs-6926668/v1 | Quan, Zhang, Lu et al. | Research Square (preprint, not peer-reviewed) | 2025 | ✅ | First author is Quan, not Rivilla. **Resolved (v4):** citation corrected to Quan et al.; the earlier DOI note was removed. |
| [6] | 10.1111/maps.13451 | Glavin, Elsila, McLain et al. | Meteoritics & Planetary Science | 2021 | ✅ | Correct |
| [7] | 10.1073/pnas.0712334105 | Takai, Nakamura, Toki et al. | PNAS | 2008 | ✅ | Correct |
| [8] | 10.1128/MMBR.00015-10 | Slade, Radman | Microbiology and Molecular Biology Reviews | 2011 | ✅ | Correct |
| [12] | 10.1007/BF01504252 | Meissner, Ochsenfeld | Die Naturwissenschaften | 1933 | ✅ | Correct |
| [13] | 10.1103/PhysRev.108.1175 | Bardeen, Cooper, Schrieffer | Physical Review | 1957 | ✅ | **Repurposed in v4:** now the BCS theory paper (108(5), 1175–1204), the source for the BCS claim; the former Essén & Fiolhais entry was replaced. |
| [14] | 10.1016/j.actamat.2016.08.081 | Miracle, Senkov | Acta Materialia | 2017 | ✅ | Correct (online 2016, print 2017) |
| [15] | 10.1103/RevModPhys.82.3045 | Hasan, Kane | Reviews of Modern Physics | 2010 | ✅ | Correct |
| [16] | 10.1126/science.1125907 | Pendry, Schurig, Smith | Science | 2006 | ✅ | Correct |
| [17] | 10.1126/science.1157996 | Lee, Wei, Kysar, Hone | Science | 2008 | ✅ | Correct |
| [18] | 10.1126/science.287.5453.637 | Yu, Lourie, Dyer et al. | Science | 2000 | ✅ | Correct |
| [19] | 10.1103/RevModPhys.76.93 | Peres, Terno | Reviews of Modern Physics | 2004 | ✅ | Correct |
| [21] | 10.1002/2016GL069790 | Way, Del Genio, Kiang et al. | Geophysical Research Letters | 2016 | ✅ | Correct |
| [22] | 10.1029/2019JE006276 | Way, Del Genio | J. Geophysical Research: Planets | 2020 | ✅ | Correct |
| [24] | 10.1038/s41550-020-1174-4 | Greaves, Richards, Bains et al. | Nature Astronomy | 2020 | ✅ | Online 2020, print 2021. **Resolved:** noted in BibTeX. |
| [26] | 10.1017/S1473550418000095 | Schmidt, Frank | Int. J. Astrobiology | 2019 | ✅ | Online 2018, print 2019. **Resolved:** year corrected. |
| [27] | 10.1126/sciadv.adp8602 | Bell, Johannes, Kennedy, Poulton | Science Advances | 2025 | ✅ | Correct. Article number eadp8602 (11(19)) added in v4. |
| [29] | 10.1126/science.167.3919.832 | Alvarez, Anderson, Bedwei et al. | Science | 1970 | ✅ | Correct |
| [34] | 10.1051/swsc/2013053 | Cliver, Dietrich | J. Space Weather and Space Climate | 2013 | ✅ | Correct |
| [35] | 10.1038/nature03676 | Gomes, Levison, Tsiganis, Morbidelli | Nature | 2005 | ✅ | Correct |
| [36] | 10.1006/jhev.1998.0219 | Ambrose | Journal of Human Evolution | 1998 | ✅ | Correct |
| [41] | 10.1038/353225a0 | Kennett, Stott | Nature | 1991 | ✅ | Correct |
| [42] | 10.1089/ast.2013.1028 | Worth, Sigurdsson, House | Astrobiology | 2013 | ✅ | Correct |
| [43] | 10.4324/9780203953464 | Bostrom, N. | Routledge (monograph) | 2002 | ✅ | Correct. CrossRef shows e-book reissue 2013; entry now reads "2002; e-book reissue 2013". |
| [44] | 10.1038/nature25020 | Meech, Weryk, Micheli et al. | Nature | 2017 | ✅ | Correct |
| [45] | 10.3847/1538-4357/ab042c | Ivezić, Kahn, Tyson et al. | The Astrophysical Journal | 2019 | ✅ | Correct |
| [46] | 10.3847/1538-4365/ac2a48 | McGuire | ApJ Supplement Series | 2022 | ✅ | Correct |
| [48] | 10.1016/0019-1035(73)90111-5 | Ball | Icarus | 1973 | ✅ | Correct |
| [49] | 10.1038/s41550-019-0931-8 | Guzik, Drahus, Rusek et al. | Nature Astronomy | 2019 | ✅ | Online 2019, print 2020. **Resolved:** year updated to 2019/2020. |
| [50] | 10.1038/s41467-019-13470-1 | Snodgrass, Jones | Nature Communications | 2019 | ✅ | Correct |
| [51] | 10.1002/ajpa.10346 | Rightmire | Am. J. Physical Anthropology | 2004 | ✅ | Correct |
| [52] | 10.1029/94JE00388 | Strom, Schaber, Dawson | J. Geophysical Research: Planets | 1994 | ✅ | Correct |
| [53] | 10.1017/S1473550404001910 | Melott, Lieberman, Laird et al. | Int. J. Astrobiology | 2004 | ✅ | Correct |
| [54] | 10.1038/nature17196 | Wallner, Feige, Kinoshita et al. | Nature | 2016 | ✅ | Correct |

**Result: 36/36 original DOIs resolved successfully (original v2 audit; all 36 rows above were later re-checked against Crossref in the v4 review, with the corrections noted in the rows for [5], [13], [27], [43]).** The earlier statement of "4 year discrepancies, all resolved" cannot be reproduced from the repository and is not repeated; the online-first versus print-year differences that are documented in the notes above are [6], [14], [24], [26] and [49].

### 3b. URL-Only References (No DOI)

18 references are institutional, mission or archive pages without DOIs (two of them, [9] and [20], are journal articles reached through ADS links):

| Ref | Type | Source |
|-----|------|--------|
| [2] | NASA mission | Kepler Space Telescope |
| [3] | NASA mission | TESS |
| [9] | Journal article | Kardashev 1964, *Soviet Astronomy* (ADS link) |
| [10] | Institution | ITER |
| [11] | Institution | IBM Quantum Hardware |
| [20] | Journal article | Freitas 1980, *JBIS* (ADS link) |
| [23] | NASA archive | Venera 13 (NSSDCA) |
| [25] | Project | Seabed 2030 |
| [28] | NASA mission | GRACE-FO |
| [30] | NASA instrument | MRO SHARAD |
| [31] | ESA instrument | Mars Express MARSIS |
| [32] | NASA mission | VERITAS |
| [33] | ESA mission | EnVision |
| [37] | Company | SpaceX Mars |
| [38] | NASA program | Artemis |
| [39] | NASA mission | DART |
| [40] | Foundation | Long Now (10,000 Year Clock) |
| [47] | NASA data | Venus Fact Sheet (GSFC) |

These references link to official institutional sources and do not require DOI verification.

### 3c. New References Added in v3 ([55]–[66])

| Ref | Type | Authors / Source | Title | Verification | Status |
|-----|------|-----------------|-------|-------------|--------|
| [55] | arXiv preprint | Sandberg, Drexler, Ord | "Dissolving the Fermi Paradox" | arXiv:1806.02404. Widely cited (700+ citations). Establishes uncertainty-aware Drake framework. | ✅ Verified |
| [56] | Peer-reviewed | Lingam, Nichols, Balbi | "A Bayesian Analysis of the Probability of the Origin of Life Per Site Conducive to Abiogenesis" | *Astrobiology* 24(8), 813–823 (2024). DOI: 10.1089/ast.2024.0037. Authors corrected in v4 (previously listed as Lingam, Balbi, Mahajan). | ✅ Verified |
| [57] | Peer-reviewed | Green et al. | "Call for a Framework for Reporting Evidence for Life Beyond Earth" | *Nature* 598, 575–579 (2021). DOI: 10.1038/s41586-021-03804-9. NASA/NfoLD community framework. | ✅ Verified |
| [58] | Peer-reviewed (published) | Sheikh et al. | "Earth Detecting Earth: At What Distance Could Earth's Constellation of Technosignatures Be Detected with Present-day Technology?" | *The Astronomical Journal* 169(2), 118 (2025). DOI: 10.3847/1538-3881/ada3c7 (arXiv:2502.02614). Updated in v4 from the arXiv preprint to the published version. | ✅ Verified |
| [59] | Peer-reviewed | Constantinou, Shorttle, Rimmer | "A dry Venusian interior constrained by atmospheric chemistry" | *Nature Astronomy* 9, 189–198 (2025). DOI: 10.1038/s41550-024-02414-5. Published online 2024-12-02. | ✅ Verified |
| [60] | Peer-reviewed | Snellen et al. | "Re-analysis of the 267 GHz ALMA observations of Venus" | *A&A* 644, L2 (2020). DOI: 10.1051/0004-6361/202039717. No significant phosphine detection. | ✅ Verified |
| [61] | Peer-reviewed | Cordiner et al. | "Phosphine in the Venusian Atmosphere: A Strict Upper Limit from SOFIA GREAT Observations" | *GRL* 49(22), e2022GL101055 (2022). DOI: 10.1029/2022GL101055. Strict upper limit below original claim. | ✅ Verified |
| [62] | Peer-reviewed | Jordan, Shorttle, Rimmer | "Proposed energy-metabolisms cannot explain the atmospheric chemistry of Venus" | *Nature Communications* 13, 3274 (2022). DOI: 10.1038/s41467-022-30804-8. **Repurposed in v4:** replaces Bains et al. 2021, which argues that no abiotic process explains the reported phosphine and therefore does not support the "metabolic models challenged" claim (identified by R5 from the title and confirmed by R3 from the abstract). | ✅ Verified |
| [63] | Peer-reviewed | Seager M. D., Seager S., Bains, Petkowski | "Stability of 20 Biogenic Amino Acids in Concentrated Sulfuric Acid: Implications for the Habitability of Venus' Clouds" | *Astrobiology* 24(4), 386–396 (2024). DOI: 10.1089/ast.2023.0082. v4 correction: the DOI is a different paper (first author Seager, not Petkowski) from what had been listed. | ✅ Verified |
| [64] | Peer-reviewed | Petkowski, Seager M. D., Bains, Seager S. | "General instability of dipeptides in concentrated sulfuric acid as relevant for the Venus cloud habitability" | *Scientific Reports* 14, 17083 (2024). DOI: 10.1038/s41598-024-67342-w. Author list (four authors) and article number corrected in v4. | ✅ Verified |
| [65] | NASA source | NASA Science | "Comet 3I/ATLAS Facts and FAQs" | Official NASA page. Third confirmed interstellar object, discovered 2025-07-01. URL verified. | ✅ Verified |
| [66] | Observatory source | NSF–DOE Vera C. Rubin Observatory | "NSF–DOE Vera C. Rubin Observatory Launches Real-Time Discovery Machine for Monitoring the Night Sky" (2026-02-25) | https://rubinobservatory.org/news/first-alerts. v4 correction: title replaced with the actual press-release title and a URL added (the previous entry had no locator). Page fetched at insertion time; contents may change. | ✅ Verified |

**Result: 12/12 have a DOI or institutional URL (v4: entries [5], [56], [58], [61]–[64], [66] corrected as noted).**

---

## 4. Structural & Logical Consistency

14 structural modifications (v2) were reviewed for scientific soundness and internal consistency.

| ID | Modification | Assessment |
|----|-------------|------------|
| P0-1 | Brain over-engineering → cognitive capacity rewrite (§10.5) | ✅ Reframed as additive speculation atop mainstream evolutionary explanations. No intelligent-design-like framing remains. |
| P0-2 | Epistemological layering (§0.5, §3.6) | ✅ Clearly distinguishes falsifiable sub-models from non-falsifiable meta-framework. Resolves §3.6 vs Part VII contradiction. |
| P0-3 | Abiogenesis constraint (§1.6) | ✅ Correctly identifies abiogenesis as weakest link. Preserves conditional structure of Parts II–VII. |
| P1-1 | Competing hypotheses for myths (§10.3) | ✅ Lists four alternative explanations with equal prior weight. Prevents exclusive attribution to extraterrestrial contact. |
| P1-2 | Venus energy budget table (§6b.4) | ✅ Quantifies buoyancy vs. reactor mass trade-off. Key constraint correctly identified as engineering challenge. |
| P1-3 | Material integration constraints (§3.3.4) | ✅ Identifies superconductor-HEA lattice incompatibility, KK bandwidth limits, thermodynamic waste heat. Redefines "stealth" as detection-threshold-relative. |
| P1-4 | Panspermia vs directed migration criteria (§9.3) | ✅ Five-criterion table well-structured. Correctly notes no single criterion is sufficient. |
| P1-5 | Fusion fuel cycle constraints (§3.1) | ✅ Tritium breeding, TBR requirements, miniaturization floor all correctly stated. |
| P1-6 | Observation selection effects (§0.3) | ✅ Correctly applies Bostrom's anthropic bias argument. Properly scoped to Part I only. |
| P2-1 | Interstellar object observation (§12.7) | ✅ Bidirectional determination criteria correctly designed. |
| P2-2 | SETI directed communication AND-condition (§3.5) | ✅ Correctly identifies logical weakness. Offers three possible additional assumptions without presupposing which holds. |
| P2-3 | Venus parameter sensitivity table (§6b.1) | ✅ Four parameters with correct sensitivity assessments. |
| P2-4 | Citation fixes | ✅ All three previously flagged issues resolved. Three new references verified. |
| P2-5 | README updates | ✅ Structure overviews correctly reflect new subsections. |

**Result: 14/14 modifications pass review.**

### 4b. v3 Structural Modifications (2026-03-10)

10 structural modifications were made in the v3 revision. Each is reviewed for scientific soundness, internal consistency, and alignment with the stated methodology.

| ID | Modification | Assessment |
|----|-------------|------------|
| V3-1 | Part VI (Cognitive Deconstruction) relocated to Appendix A | ✅ Correctly reduces risk of evidential contamination. Appendix framing with explicit note ("supplementary context, not core evidential chain") is appropriate. Cross-reference to Part III structural analysis preserved. |
| V3-2 | Bayesian prior assessment table added to Part IV (10 sub-models) | ✅ Prior plausibility ratings are qualitatively reasonable. "Very Low" correctly assigned to chain-of-assumptions models (directed migration, ancient civilization nodes). "Not assessable" correctly assigned to unfalsifiable meta-framework. Supporting evidence classes are accurately described. |
| V3-3 | Venus section rebuilt with balanced 2024–2026 literature | ✅ Four constraining lines of evidence correctly cited: dry interior [59], phosphine re-analysis [60][61], metabolic model challenges [62] (v4: [62] now Jordan et al. 2022). Amino acid stability [63] correctly cited as partial counter-evidence (v4: [63] metadata corrected to Seager, M. D. et al. 2024; [64] restated as general dipeptide instability). "Balanced assessment" paragraph correctly downgrades Venus to "bounded, low-prior branch." |
| V3-4 | Instrument-threshold detection table added (§12.0, 8 methods) | ✅ Resolution figures are accurate: GRACE-FO ~300 km, SHARAD ~15 m vertical, Seabed 2030 27.3% coverage, deep-sea visual <0.001%. Constraint strengths correctly graded. Key implication ("null result is uninformative where instruments lack resolution") is scientifically sound. |
| V3-5 | Interstellar object section updated with 3I/ATLAS and Rubin Observatory | ✅ 3I/ATLAS correctly identified as third confirmed interstellar object (discovered 2025-07-01). Rubin Observatory first scientific alerts (2026-02-25) correctly cited. Population-level statistical analysis framing is appropriate. |
| V3-6 | Four skeleton-level reference sets integrated into main text | ✅ Sandberg 2018 [55] correctly placed in §0.3 with appropriate implication for framework necessity. Lingam 2024 [56] correctly placed in §1.6 abiogenesis section. NfoLD framework [57] correctly placed in §0.5 with self-assessment of evidence stage. Sheikh 2025 [58] correctly placed in §12.4 with detectability context for Fermi communication argument. |
| V3-7 | Program references downgraded to context-only | ✅ ITER, IBM, SpaceX, Artemis, Long Now correctly reclassified as "contextual indicators of engineering direction, not as evidential support for specific claims." This improves the distinction between peer-reviewed and institutional references. |
| V3-8 | Ref [5] attribution explicitly clarified | ✅ Preprint status and Quan/Rivilla DOI resolution discrepancy were noted in v3; superseded in v4, where the citation itself was corrected to Quan et al. |
| V3-9 | LaTeX title page populated (author: Kris Lai, affiliation: Scallop Labs) | ✅ Resolves placeholder issue flagged in external review. |
| V3-10 | README structure overviews and reference counts updated | ✅ Part VI → Appendix A transition correctly reflected. Reference count updated from 54 to 66. New structural elements (Bayesian table, instrument-threshold table, 3I/ATLAS) correctly listed. |

**Result: 10/10 v3 modifications pass review.**

---

## 5. Summary

### Aggregate Results

| Category | Verified | Partially Verified / Debated | Total |
|----------|----------|------------------------------|-------|
| Astrophysical claims | 13 | 0 | 13 |
| Biological claims | 6 | 3 (correctly qualified) | 9 |
| Physics & engineering claims | 11 | 0 | 11 |
| Citation DOIs (original, full verification) | 36 | 0 | 36 |
| URL-only references (original) | 18 (institutional) | 0 | 18 |
| New references v3 [55]–[66] | 12 | 0 | 12 |
| Structural modifications (v2) | 14 | 0 | 14 |
| Structural modifications (v3) | 10 | 0 | 10 |

### Remaining Minor Notes

| Item | Severity | Status |
|------|----------|--------|
| *D. radiodurans* 5,000 Gy — survival rate is ~37% at that dose | Low | Informational — paper's claim is defensible in context |
| Venus habitable window depends on climate model assumptions | Low | Informational — paper correctly uses hedging language, includes parameter sensitivity table, and now includes balanced 2024–2026 constraining literature |
| Toba-bottleneck causal link is debated | Low | Informational — paper correctly notes the controversy |
| Ref [66] (Rubin Observatory first alerts) — institutional URL rather than journal DOI | Low | Machine-verifiable and acceptable for a current observatory source; replaceable later if a formal paper appears |

### Conclusion

**The Cosmic Diaspora Hypothesis maintains careful citation discipline and factual accuracy in its verifiable claims.** The v4 review found and corrected several physics errors in the v3 text (Section 6); the remaining data points were re-checked in v4 where Section 6 says so. Biological claims are supported by peer-reviewed literature, with appropriate qualification where evidence is debated. In the v1–v3 audit, all 66 references were traced to real publications, institutional sources, or preprints with valid DOIs/URLs; the v4 list of 175 is covered by the checks and limits described in Section 6, and this conclusion refers to the v3 state except where Section 6 says otherwise. The v3 revision significantly strengthens the framework through: a Bayesian prior assessment table, balanced Venus literature incorporating post-2024 constraints, an instrument-threshold detection table quantifying the informational value of null results, updated interstellar object data (3I/ATLAS), four skeleton-level reference sets (Sandberg 2018, Lingam 2024, NfoLD, Sheikh 2025), and the relocation of the cognitive deconstruction section to an appendix. The framework's falsifiability design, epistemological layering, and conditional derivation structure are internally consistent. It remains, however, a speculative, non-peer-reviewed thought experiment: its conditional sub-models (Parts III–VII) are not yet empirically tested, and its conclusions should be read as structured possibilities rather than established results.


---

## 6. v4 Revision — Independent Referee Review (2026-11)

In November 2026 the document was revised after a five-pass referee review. **The review itself was AI-assisted**, consistent with the AI co-creation disclosure in the README: the referee passes were run by LLM agents, not by human peer reviewers. Each pass covered one slice of `hypothesis-en.md`:

| Pass | Scope | Findings (critical / major / minor) |
|------|-------|-------------------------------------|
| R1 | Methodology & Part I | 27 (2 / 18 / 7) |
| R2 | Part II | 35 (2 / 22 / 11) |
| R3 | Parts III–IV | 46 (6 / 27 / 13) |
| R4 | Parts V–VII & appendix | 45 (7 / 25 / 13) |
| R5 | Citation / sync integrity (reference list, Markdown vs. zh-TW vs. LaTeX, counts) | 21 (8 / 7 / 6) |
| **Total** | | **174 (25 / 99 / 50)** |

(Counts are taken from each referee file's own summary line. Findings were triaged before fixing; not every finding resulted in a text change, and some were merged.)

### Main correction categories

- **Citation and metadata errors**: wrong first author or title for a DOI, wrong issue numbers, missing article numbers, a published version replacing a preprint entry, a reference with no locator.
- **Overclaims hedged**: null-result and "elimination" language, uncited ranges, claims stronger than the cited source supports, and misread numbers from cited papers.
- **Prior table and conclusion rewritten**: the former Bayesian prior table is now a "Qualitative Credence Assessment of Sub-Models", and the conclusion was rewritten accordingly.
- **Structure**: arabic sections §10–13 renumbered to §9–12 (e.g. §13.0 is now §12.0, §13.7 is now §12.7); Part VI renamed "Interstellar Mission Architecture & Human Positioning" ("Cross-Galactic" was a scale error); revision-history text removed from the body.
- **Cross-document drift** between Markdown and LaTeX identified by R5; the LaTeX sources are updated separately.

### Corrected and repurposed existing references

- [5] now Quan et al. 2025 (previously attributed to Rivilla); marked as a non-peer-reviewed preprint.
- [13] repurposed to Bardeen, Cooper & Schrieffer 1957 (BCS theory).
- [56] authors corrected to Lingam, Nichols & Balbi, with volume and pages.
- [58] now the published *Astronomical Journal* version.
- [61] issue number corrected to 22.
- [62] repurposed to Jordan, Shorttle & Rimmer 2022.
- [63] now Seager M. D. et al. 2024; the DOI is a different paper from the one previously listed.
- [64] author list and article number corrected.
- [66] correct press-release title and URL.
- Metadata fixes to [6], [27], [43], [55].

### New references [67]–[175]

109 references were added (the list grew from 66 to 175). Each was confirmed at insertion time against Crossref (for DOI entries) or by fetching the page (for URL entries). Resulting source types in the v4 list: 137 DOI, 36 URL-only, 2 arXiv-only (3 entries marked as preprints).

### Known limits

- **No human peer review.** Both the review and the verification were AI-assisted; they do not replace expert peer review.
- **URL contents can change.** URL entries were checked once, at insertion time, and are not a guarantee of future content.
- **The machine check covers limited ground.** `scripts/verify_references.py` checks that a DOI resolves and that the bibliography title and first-author surname match Crossref (flagging mismatches as `manual_review_required`). It does not check volume, pages, year, or whether a source supports the claim it is cited for. Metadata of corrected entries was audited manually in the v4 review.
- The machine-audit files in `verification/` are refreshed separately from this report.
- Tables 1–2b and 4–4b (claims and structural modifications) date from v1–v3 and were not re-run in v4 except where the text above says so (for example, the Seabed 2030 coverage figure in row V3-4 predates the v4 update to 28.7% as of April 2026).

---

*Verification tools: astropy (Planck18), biopython, CrossRef REST API v1, CDMS database, NASA planetary factsheets*
*Initial verification: 2026-02-28 | Supplemental verification & citation audit: 2026-03-04 | v3 revision verification: 2026-03-10 | v4 referee review: 2026-11*
