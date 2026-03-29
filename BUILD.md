# Build and Verification

This repository has two reproducible workflows:

- reference verification for machine-readable audit outputs
- optional local document build for a non-tracked PDF artifact

## Prerequisites

Required:

- `python3` 3.9+
- `pip`

Optional but recommended:

- `make`
- TeX toolchain for PDF builds
  - `latexmk`, or
  - `pdflatex` + `bibtex`

## Python Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you want the wider scientific stack mentioned in the verification report:

```bash
pip install -r requirements-full.txt
```

## Reference Verification

Quick online audit:

```bash
python3 scripts/verify_references.py
```

Quick offline audit that only checks identifier presence and document-count
consistency:

```bash
python3 scripts/verify_references.py --offline \
  --json-output verification/verification-offline.json \
  --csv-output verification/verification-offline.csv
```

Generated files:

- `verification/verification.json`
- `verification/verification.csv`

The script reads `latex/references.bib`, verifies DOI entries against Crossref,
checks URL and arXiv entries over HTTP, and reports any entries that still need
manual review.

## Convenience Commands

If `make` is available:

```bash
make setup
make verify-references
make verify-references-offline
```

## PDF Build

The repository does not track compiled PDFs in git. The primary PDF workflow for
this project is to maintain `latex/main.tex` in the repository, sync it to
Overleaf, collaborate there as needed, and export the PDF from Overleaf.

If you still want a local fallback build, install MacTeX or TeX Live first,
then run:

```bash
make pdf
```

The optional `pdf` target will:

- prefer `latexmk` when available
- fall back to `pdflatex` + `bibtex`
- copy the resulting PDF to `cosmic_diaspora_hypothesis.pdf`

## Troubleshooting

- If URL checks fail intermittently, rerun the script. Some institutional sites
  rate-limit or redirect aggressively.
- If a reference has no DOI, URL, or arXiv identifier, it will be marked as
  `manual_review_required` until better metadata is added.
- If PDF build fails locally, confirm that `pdflatex` and `bibtex` are on your
  `PATH`.
