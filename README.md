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

## 🦾 Stack
- 🔠 **Language:** Python
- 🛠️ **Containerization:** Docker
- 📂 **Dependency Management:** Virtualenv and Pip
- 🔧 **Automation:** Makefile

---

## 🔧 Requirements
- 💻 Python 3.11+
- 🐳 Docker
- ✅ Make


---

## 🚀 Quick Start

### 1. Local Development

```bash
make build     # Build Docker image
make install   # Set up virtualenv and install dependencies
```

### 2. Run Locally (Python)

```bash
make create   # Generate the report inside Docker
make local    # Run the report generator locally
```

---

## 📊 CSV Input Format (`data/expenses_2025_07.csv`)

```csv
categoria,descricao,valor,data
Salário,Salário Líquido,3500.00,2025-07-01
Adicionais (Salário),Bônus,0.00,2025-07-01
Internet,Plano Vivo,100.00,2025-07-01
Condominio,Apartamento,400.00,2025-07-01
Energia,Conta Luz,180.00,2025-07-01
Plano Celular,Tim Controle,90.00,2025-07-01
Investimentos,Renda Fixa,300.00,2025-07-01
Impostos mensais,INSS DAS,400.00,2025-07-01
Gastos Extras,Viagem,150.00,2025-07-01
Alimentação,Supermercado,550.00,2025-07-01
Transporte,Uber,45.00,2025-07-02
Lazer,Cinema,60.00,2025-07-10
Aluguel,Apartamento,1500.00,2025-07-05
Saúde,Remédio,85.00,2025-07-08
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