# Contributing to Cosmic Diaspora Hypothesis

Thanks for contributing. This repository is a research-document project rather
than a conventional software library, so the most valuable contributions are
usually one of the following:

- citation fixes and metadata corrections
- verification upgrades that make claims easier to audit or reproduce
- wording changes that improve precision, scope control, or falsifiability
- bilingual synchronization between the English and `zh-TW` documents
- structural refactors that improve readability without overstating evidence

## Ground Rules

- Prefer evidence-backed edits over stylistic rewrites.
- Distinguish clearly between observation, inference, speculation, and
  non-falsifiable thought experiments.
- When a claim is debated, preserve hedging language unless you are adding
  stronger evidence.
- If you update references or verification language, refresh the machine-readable
  verification outputs before opening a pull request.
- If a change affects both English and zh-TW / 正體中文 content, keep both
  versions aligned or call out the mismatch explicitly in the PR.

## Local Setup

1. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

2. Run the reproducible reference audit:

   ```bash
   python3 scripts/verify_references.py
   ```

3. Optional: install the extended verification stack for future astrophysics or
   biology checks:

   ```bash
   pip install -r requirements-full.txt
   ```

More detailed commands are documented in [BUILD.md](./BUILD.md).

## Expected Workflow

1. Create a focused branch. A good default is
   `codex/<type>/<short-description>`.
2. Make the smallest coherent change you can.
3. If you touch `latex/references.bib`, `README.md`, `README-zh-TW.md`, or the
   verification reports, rerun `python3 scripts/verify_references.py`.
4. If you touch `latex/main.tex`, rebuild the PDF when a TeX toolchain is
   available.
5. Open a pull request with a concise summary, verification notes, and any
   translation follow-up.

## Evidence and Citation Expectations

- Prefer peer-reviewed literature, institutional mission pages, and stable
  archival links.
- Keep DOI, URL, arXiv, and access metadata consistent with the cited source.
- If an entry cannot be machine-verified, mark that fact clearly and keep the
  claim language conservative.
- Do not treat company roadmaps, mission pages, or general-interest summaries as
  equivalent to peer-reviewed evidence.

## Commit and PR Style

This repository uses Conventional Commits:

- `docs(readme): clarify reproducible verification workflow`
- `fix(references): correct DOI metadata for ref 64`
- `feat(verification): add machine-readable reference audit`

For pull requests, please include:

- a short summary of what changed
- the commands you ran
- whether bilingual files remain aligned
- whether any manual review items remain unresolved

## Pull Request Checklist

- [ ] The change is scoped to one clear improvement.
- [ ] Citations and links were checked for any modified claims.
- [ ] `python3 scripts/verify_references.py` was run when references or reports changed.
- [ ] `verification/verification.json` and `verification/verification.csv` were refreshed when needed.
- [ ] English and `zh-TW` content remain aligned, or the gap is documented.
- [ ] PDF output was rebuilt if `latex/main.tex` changed and TeX was available.
