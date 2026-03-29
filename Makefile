PYTHON ?= python3
VENV ?= .venv
VENV_PIP := $(VENV)/bin/pip
VENV_PYTHON := $(VENV)/bin/python
VERIFY_SCRIPT := scripts/verify_references.py
VERIFY_JSON := verification/verification.json
VERIFY_CSV := verification/verification.csv
VERIFY_JSON_OFFLINE := verification/verification-offline.json
VERIFY_CSV_OFFLINE := verification/verification-offline.csv

ifeq ("$(wildcard $(VENV_PYTHON))","")
RUN_PYTHON := $(PYTHON)
else
RUN_PYTHON := $(VENV_PYTHON)
endif

.PHONY: setup verify-references verify-references-offline pdf clean

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV_PIP) install -r requirements.txt

verify-references:
	$(RUN_PYTHON) $(VERIFY_SCRIPT) --json-output $(VERIFY_JSON) --csv-output $(VERIFY_CSV)

verify-references-offline:
	$(RUN_PYTHON) $(VERIFY_SCRIPT) --offline --json-output $(VERIFY_JSON_OFFLINE) --csv-output $(VERIFY_CSV_OFFLINE)

pdf:
	@if command -v latexmk >/dev/null 2>&1; then \
		cd latex && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex; \
	elif command -v pdflatex >/dev/null 2>&1 && command -v bibtex >/dev/null 2>&1; then \
		cd latex && pdflatex -interaction=nonstopmode main.tex && bibtex main && pdflatex -interaction=nonstopmode main.tex && pdflatex -interaction=nonstopmode main.tex; \
	else \
		echo "Missing TeX build tools. Install latexmk or pdflatex + bibtex first."; \
		exit 1; \
	fi
	@cp latex/main.pdf cosmic_diaspora_hypothesis.pdf

clean:
	@rm -f latex/*.aux latex/*.bbl latex/*.blg latex/*.fdb_latexmk latex/*.fls latex/*.log latex/*.out latex/*.synctex.gz latex/*.toc latex/main.pdf
