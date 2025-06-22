# 🧾 Expense Report Generator

Automate your monthly expense reports using Python, Docker, and Makefile. This project reads a CSV file containing your expenses, generates charts, and outputs a complete PDF report.

## 📦 Features

- Read and validate expense data from a CSV file
- Generate pie charts for category distribution
- Create a professional PDF report
- Run locally or in a Docker container
- Easy automation via Makefile

---

## 🗂️ Project Structure

```
expense-report/
├── data/                   # CSV files with monthly expenses
├── reports/                # Generated PDF reports and images
├── src/
│   ├── models/            # Data loading and validation
│   ├── charts/            # Chart generation (e.g., pie chart)
│   ├── reports/           # PDF generation using ReportLab
│   └── main.py            # Main entry point
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

### 1. Run with Docker

```bash
make build    # Build Docker image
make create   # Generate the report inside Docker
```

### 2. Run Locally (Python)

```bash
make install  # Set up virtualenv and install dependencies
make local    # Run the report generator locally
```

---

## 📊 CSV Input Format (`data/expenses_2025_07.csv.csv`)

```csv
categoria,descricao,valor,data
Food,Supermarket,320.00,2025-07-01
Transport,Uber,45.00,2025-07-02
Leisure,Cinema,60.00,2025-07-10
Rent,Apartment,1500.00,2025-07-05
Health,Pharmacy,85.00,2025-07-08
```

---

## 🧹 Cleanup

```bash
make clean    # Remove reports, images, virtualenv and Docker artifacts
```

---

## 📘 Available Commands

```bash
make build    # Build the Docker image
make create   # Run the report in Docker
make setup    # Create a virtual environment
make install  # Install Python dependencies
make local    # Run the report locally
make clean    # Clean all generated files
make help     # Show the help menu
```