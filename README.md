# 🧾 Expense Report Generator

Automate your monthly expense reports using **Python**, and **Makefile**. This project reads a CSV file containing your expenses, generates charts, builds a professional PDF report, and exports your data to Excel — all ready for bookkeeping or personal analysis.

## 📦 Features

- ✅ Read and validate structured expense data from a CSV file
- 📊 Generate pie charts showing category distribution
- 📝 Create a detailed PDF financial report with summary + chart
- 📈 Export your data to Excel with auto-formatting and summary
- 🐳 Run locally or inside a Docker container
- 🔁 Automate your workflow using Makefile targets

---

## 🗂️ Project Structure

```
expense-report/
├── data/                   # CSV files with monthly expenses
├── reports/                # Generated PDF, Excel files and charts
├── src/
│   ├── models/            # Data loading and validation
│   ├── charts/            # Chart generation (e.g., pie chart)
│   ├── reports/           # PDF (ReportLab) and Excel (pandas/openpyxl)
│   └── main.py            # Main entry point
├── Dockerfile
├── Makefile
├── requirements.txt
└── README.md
```

---

## 🦾 Stack

- 🔠 **Language:** Python
- 📊 **PDF/Excel:** ReportLab, Matplotlib, Pandas, OpenPyXL
- 📦 **Dependency Management:** Virtualenv + Pip
- ⚙️ **Automation:** Makefile

---

## 🔧 Requirements

- 💻 Python 3.11+
- ✅ Make (GNU)

---

## 🚀 Quick Start

### 1. Project Clone
```bash
git clone https://github.com/Victor-Zarzar/expense-report
```

### 2. Enter in directory and open in your favorite editor(e.g. VSCode):
```bash
cd expense-report
code .
```

### 3. Local Development

```bash
make install   # Set up virtualenv and install dependencies
```

### 4. Run the Report (Full Report (PDF + Excel))

```bash
make create    # Generate full report (PDF + Excel)
```

### 5. PDF Only

```bash
make create-pdf   # Generate only the PDF report
```

### 6. Excel Only

```bash
make create-excel   # Generate only the Excel report

```

---

## 📊 CSV Input Format (`data/expenses_2025_08.csv`)

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
Gastos Extras,Viagem,150.00,2025-07-02
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
make install  # Install Python dependencies
make create   # Generate full report (PDF + Excel)
make create-pdf   # Generate only the PDF report
make create-excel   # Generate only the Excel report
make setup    # Create a virtual environment
make clean    # Clean all generated files
make help     # Show the help menu
```