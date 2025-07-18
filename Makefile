# Makefile: Expense Report Automation
PYTHON = python3
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON_VENV = $(VENV)/bin/python

.PHONY: setup install create-pdf create-excel create clean help

setup:
	@echo "📦 Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "✅ Virtual environment created."

install: setup
	@echo "🔧 Installing dependencies..."
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed."

create:
	@echo "📝 Generating full report (PDF + Excel)..."
	$(PYTHON_VENV) src/main.py

create-pdf:
	@echo "📝 Generating PDF report..."
	$(PYTHON_VENV) src/main.py pdf

create-excel:
	@echo "📊 Generating Excel report..."
	$(PYTHON_VENV) src/main.py excel

clean:
	@echo "🧹 Cleaning up..."
	rm -f reports/*.pdf reports/*.png reports/*.xlsx
	rm -rf $(VENV)
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@echo "✅ Cleaned."

help:
	@echo ""
	@echo "📘 Available commands:"
	@echo "  make setup         → Create virtual environment"
	@echo "  make install       → Install dependencies"
	@echo "  make create        → Generate full report"
	@echo "  make create-pdf    → Generate only PDF report"
	@echo "  make create-excel  → Generate only Excel report"
	@echo "  make clean         → Clean generated files and venv"
	@echo ""
