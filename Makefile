# Makefile: Expense Report Automation
DOCKER_IMAGE_NAME = expense-report
PYTHON = python3
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON_VENV = $(VENV)/bin/python

.PHONY: build setup install create local clean help

build:
	docker build -t $(DOCKER_IMAGE_NAME) .

setup:
	@echo "🔧 Creating virtual environment..."
	$(PYTHON) -m venv $(VENV)
	@echo "✅ Virtual environment created."

install: setup
	@echo "📦 Installing dependencies..."
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencies installed."

create:
	docker run --rm \
		-v $(PWD)/data:/app/data \
		-v $(PWD)/reports:/app/reports \
		$(DOCKER_IMAGE_NAME)

local:
	$(PYTHON_VENV) src/main.py

clean:
	@echo "🧹 Cleaning up local environment and generated files..."
	rm -f reports/*.pdf reports/*.png
	rm -rf $(VENV)
	rm -rf __pycache__
	rm -rf .pytest_cache
	@echo "🗑️ Removing Docker containers and image..."
	docker container prune -f
	docker image rm -f $(DOCKER_IMAGE_NAME) || true
	@echo "✅ Cleaned up."

help:
	@echo ""
	@echo "📘 Available commands:"
	@echo "  make build     → Build the Docker image"
	@echo "  make create    → Generate the report via Docker"
	@echo "  make setup     → Set up a virtual environment"
	@echo "  make install   → Install Python dependencies"
	@echo "  make local     → Run the report generation locally"
	@echo "  make clean     → Remove reports and reset environment"
	@echo "  make help      → Show this help menu"
	@echo ""
