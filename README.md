**[正體中文版](./README-zh-TW.md)**

# Cosmic Diaspora Hypothesis

**宇宙播遷假說**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18965614.svg)](https://doi.org/10.5281/zenodo.18965614)

A structured hypothesis framework exploring the statistical foundations of cosmic life, the energy and material thresholds of civilization evolution, and a rigorous multi-source classification model for extraterrestrial phenomena — grounded in physics, engineering feasibility, and falsifiable reasoning.

> This is a living document. Contributions, critiques, and falsification attempts are welcome.

![Cosmic Diaspora Hypothesis](./assets/cover.png)

---

## Author

**Kris Lai**
- Email: kriss@scallop.io
- ORCID: [0009-0000-2223-4826](https://orcid.org/0009-0000-2223-4826)
- Affiliation: [Scallop Labs](https://www.scallop.io/)

---

## Documents

| Document | Language | Description |
|----------|----------|-------------|
| [`hypothesis-en.md`](./markdown/en/hypothesis-en.md) | English | Full hypothesis framework in Markdown |
| [`hypothesis-zh-TW.md`](./markdown/zh-TW/hypothesis-zh-TW.md) | 正體中文 | Full hypothesis framework in zh-TW / 正體中文 |
| [`latex/main.tex`](./latex/main.tex) | English | LaTeX publication/export source used for Overleaf-based PDF generation |
| [`VERIFICATION-REPORT.md`](./markdown/en/VERIFICATION-REPORT.md) | English | Scientific verification report |
| [`VERIFICATION-REPORT-zh-TW.md`](./markdown/zh-TW/VERIFICATION-REPORT-zh-TW.md) | 正體中文 | Scientific verification report in zh-TW / 正體中文 |

---

## Verification Summary

Factual claims and references were checked with computational tools and public databases (author-run pipeline). In November 2026 the document also went through an AI-assisted five-pass referee review (the v4 revision; see the Verification Report). There has been no human peer review.

| Category | Verified (v1–v3 text) | Method |
|----------|----------|--------|
| Astrophysical claims | 13/13 | `astropy` (Planck18 cosmology) |
| Biological claims | 9 (6 verified + 3 qualified) | PubMed / NCBI literature review |
| Physics & engineering claims | 11/11 | Peer-reviewed literature |
| DOI references | 137 | DOIs resolve and title/first author match Crossref (machine check, see `verification.json`); metadata of corrected entries audited manually in the v4 review |
| URL-only references | 36 | Page fetched at insertion time (contents may change) |
| arXiv-only preprints | 2 | arXiv |
| **Total references** | **175** | |

> Per-claim counts (astrophysical, biological, physics & engineering) come from the v1–v3 audits; several of those claims were corrected in v4 (star-formation conversion, Venus surface values, CDMS molecule count, p-¹¹B temperature, room-temperature superconductivity limit, LSST interstellar-object rate) — see the notes in the [Verification Report](./markdown/en/VERIFICATION-REPORT.md).
>
> Reference counts follow the Markdown reference list (the machine audit in [`verification.json`](./verification/verification.json) counts the 2 arXiv-only entries as URL sources). Of the 175, references [55]–[66] (12) were added in the v3 revision and [67]–[175] (109) in the v4 revision (3 entries in the list are marked as preprints). The v3 additions cover: Fermi paradox dissolution, abiogenesis Bayesian analysis, NfoLD framework, technosignature detectability, Venus constraints, 3I/ATLAS, Rubin Observatory. Latest machine audit (2026-11-08, 175 entries): 170 verified, 3 restricted (pages that return HTTP 403 to automated requests: [120] media.defense.gov, [122] aaro.mil, [138] skyandtelescope.org; checked manually), 2 failed ([9] Kardashev 1964 and [20] Freitas 1980, whose ADS abstract pages reject automated requests from some networks). Full methodology, per-claim tables, and the complete DOI audit are documented in the [Verification Report](./markdown/en/VERIFICATION-REPORT.md).

---

## Structure Overview

- **0. Methodology & Scope** — Problem definition, falsifiability, observation selection effects (Anthropic Principle), epistemological layering, and statistical cosmology framework
- **Part I — Foundations of Cosmic Life Diffusion** — Stellar formation, habitable zones, extremophiles, lithopanspermia, abiogenesis probability constraint (§1.6)
- **Part II — Civilization Evolution & Technology Thresholds** — Energy hierarchy, fusion fuel cycle constraints, material breakthroughs, material system integration limits (§3.3.4), compact fusion, metamaterials
- **Part III — Structural Classification of ET Events** — 7-source classification model for contemporary extraterrestrial events, SETI directed communication limitations
- **Part IV — Civilization Existence Models** — qualitative credence assessment table, extra-solar observers, ancient Martian civilization, ancient Venus civilization (with balanced 2024–2026 literature constraints), ancient Earth civilization, panspermia vs directed migration distinction criteria
- **Part V — Base Engineering & Stealth Matrix** — Site selection, energy self-sufficiency, EM/thermal suppression, Venus atmospheric energy budget & parameter sensitivity analysis
- **Part VI — Interstellar Mission Architecture & Human Positioning** — Deployment logic, civilization reset cycles, memory compression, human mission positioning
- **Part VII — Verifiable Observation Pathways** — Instrument-threshold detection table (§12.0), subsurface imaging, deep-sea scanning, gravitational anomaly monitoring, interstellar object spectral analysis including 3I/ATLAS (§12.7)
- **v4 review (2026-11)** — Five-pass AI-assisted referee review (174 findings); text hedged and corrected, arabic sections §10–13 renumbered to §9–12, references expanded from 66 to 175 (details in the Verification Report)
- **Appendix A — Cognitive Deconstruction** — "Alien" as semantic compression, multi-source model ensemble (relocated from former Part VI)

---

## Co-Created With

This hypothesis was co-created with the assistance of AI models and tools:

**AI Models:**
- [GPT-5](https://openai.com/) (OpenAI)
- [Claude Opus 4](https://anthropic.com/) (Anthropic)

**Tools:**
- [OpenClaw](https://github.com/openclaw/openclaw) — AI gateway & agent runtime
- [Claude Code](https://claude.ai/claude-code) — Anthropic's agentic coding tool

---

## Collaboration

- [CONTRIBUTING.md](./CONTRIBUTING.md) — contribution workflow, evidence expectations, and PR checklist
- [BUILD.md](./BUILD.md) — local setup, optional local PDF build, and reproducible verification commands
- [`verification/verification.json`](./verification/verification.json) — latest machine-readable reference audit
- [`verification/verification.csv`](./verification/verification.csv) — latest flat reference audit export

## Document Sync Rules

- `markdown/en/hypothesis-en.md` is the working source for English prose edits and AI-assisted content iteration.
- `markdown/zh-TW/hypothesis-zh-TW.md` is the working source for zh-TW / 正體中文 prose edits and AI-assisted content iteration.
- `latex/main.tex` is the publication/export source used when preparing the final PDF in Overleaf.
- Section numbers in the PDF follow LaTeX automatic numbering and therefore differ from the Markdown section numbers; citation numbers are forced to match the Markdown via `\nocite`.
- The compiled PDF is not tracked in this repository. Export it from Overleaf when needed.
- When a structural or citation change affects more than one document, update the related Markdown and LaTeX files in the same PR or note the remaining sync gap explicitly.

## PDF Workflow

The primary PDF workflow for this project is:

1. Draft and revise content in the Markdown and LaTeX sources in this repository.
2. Copy or sync the LaTeX source to Overleaf.
3. Use Claude Browser Extension inside Overleaf when collaborating on final PDF-facing edits.
4. Export the PDF from Overleaf as needed.

The repository keeps the editable sources, not the compiled PDF artifact.

## Reproducible Verification

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/verify_references.py
```

This refreshes the machine-readable audit outputs from `latex/references.bib`.

---

## License

This work is licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this work, provided appropriate credit is given. See the root [LICENSE](./LICENSE) file for the repository-level notice.
