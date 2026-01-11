# Makefile: Expense Report Automation
PYTHON = python3
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON_VENV = $(VENV)/bin/python
TAG = 1.0.0

setup:
	$(PYTHON) -m venv $(VENV)

install: setup
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

create:
	@echo "Gerando relatório completo (PDF + Excel)..."
	MODE=all $(PYTHON_VENV) src/main.py

create-pdf:
	@echo "Gerando relatório em PDF..."
	MODE=pdf $(PYTHON_VENV) src/main.py

create-excel:
	@echo "Gerando relatório em Excel..."
	MODE=excel $(PYTHON_VENV) src/main.py

clean:
	rm -f reports/*.pdf reports/*.png reports/*.xlsx
	rm -rf $(VENV)
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

lint:
	$(PYTHON_VENV) -m pylint src

help:
	@echo ""
	@echo "Expense Report Makefile ($(TAG))"
	@echo "  make setup         → Create virtual environment"
	@echo "  make install       → Install dependencies"
	@echo "  make create        → Generate full report"
	@echo "  make create-pdf    → Generate only PDF report"
	@echo "  make create-excel  → Generate only Excel report"
	@echo "  make clean         → Clean generated files and venv"
	@echo "  make lint          → Run code linting"
	@echo ""
