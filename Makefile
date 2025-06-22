# Makefile: Expense Report Automation
DOCKER_IMAGE_NAME = expense-report
PYTHON = python3
VENV = .venv
PIP = $(VENV)/bin/pip
PYTHON_VENV = $(VENV)/bin/python

.PHONY: build setup install create local clean help create-pdf create-excel

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

create-pdf:
	docker run --rm \
		-v $(PWD)/data:/app/data \
		-v $(PWD)/reports:/app/reports \
		-e MODE=pdf \
		$(DOCKER_IMAGE_NAME) python3 src/main.py

create-excel:
	docker run --rm \
		-v $(PWD)/data:/app/data \
		-v $(PWD)/reports:/app/reports \
		-e MODE=excel \
		$(DOCKER_IMAGE_NAME) python3 src/main.py

local:
	$(PYTHON_VENV) src/main.py

clean:
	@echo "🧹 Cleaning up local environment and generated files..."
	rm -f reports/*.pdf reports/*.png reports/*.xlsx
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
	@echo "  make build          → Build the Docker image"
	@echo "  make install        → Install Python dependencies locally"
	@echo "  make create         → Generate full report (PDF + Excel) via Docker"
	@echo "  make create-pdf     → Generate only the PDF report via Docker"
	@echo "  make create-excel   → Generate only the Excel report via Docker"
	@echo "  make setup          → Create a local virtual environment"
	@echo "  make local          → Run full report locally (PDF + Excel)"
	@echo "  make clean          → Remove reports, env, and Docker artifacts"
	@echo "  make help           → Show this help menu"
	@echo ""
