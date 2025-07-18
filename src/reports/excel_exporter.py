import pandas as pd
from datetime import datetime
import os


def export_to_excel(df: pd.DataFrame, output_dir: str = "reports") -> str:
    """Exports the expense DataFrame to Excel with financial summary and generation date."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Extract the reference month from the DataFrame
    reference_month = df['mes_referencia'].iloc[0].replace('/', '_').lower()
    filename = f"expenses_{reference_month}.xlsx"
    filepath = os.path.join(output_dir, filename)

    df_sorted = df.sort_values(by="data")

    # Classification of types
    CATEGORIES_VARIABLES = ["Aluguel", "Investimentos",
                            "Impostos", "Saúde", "Lazer", "Gastos Extras"]
    CATEGORIES_FIXED_REVENUE = ["Salário"]

    def classify_line(row):
        if row['categoria'] in CATEGORIES_FIXED_REVENUE:
            return 'receita_fixa'
        elif row['categoria'] == "Adicionais":
            return 'receita_variavel'
        elif row['categoria'] in CATEGORIES_VARIABLES:
            return 'despesa_variavel'
        else:
            return 'despesa_fixa'

    df_sorted['tipo'] = df_sorted.apply(classify_line, axis=1)

    fixed_recipes = df_sorted[df_sorted['tipo']
                              == 'receita_fixa']['valor'].sum()
    variable_recipes = df_sorted[df_sorted['tipo']
                                 == 'receita_variavel']['valor'].sum()
    fixed_expenses = df_sorted[df_sorted['tipo']
                               == 'despesa_fixa']['valor'].sum()
    variable_expenses = df_sorted[df_sorted['tipo']
                                  == 'despesa_variavel']['valor'].sum()
    saldo = (fixed_recipes + variable_recipes) - \
        (fixed_expenses + variable_expenses)

    # Export with ExcelWriter
    with pd.ExcelWriter(filepath, engine="openpyxl", datetime_format="DD/MM/YYYY") as writer:
        # First: write the DataFrame (starting after the resumo)
        df_sorted.drop(columns="tipo").to_excel(
            writer, index=False, sheet_name="Gastos", startrow=10)

        worksheet = writer.sheets["Gastos"]
        workbook = writer.book

        # Generation date
        generation_data = datetime.now().strftime("Data de geração: %d/%m/%Y")
        worksheet.cell(row=1, column=1, value=generation_data)

        # Financial summary
        resumo = [
            ["Resumo Financeiro", ""],
            ["Receitas Fixas", f"R$ {fixed_recipes:,.2f}"],
            ["Receitas Variáveis", f"R$ {variable_recipes:,.2f}"],
            ["Despesas Fixas", f"R$ {fixed_expenses:,.2f}"],
            ["Despesas Variáveis", f"R$ {variable_expenses:,.2f}"],
            ["Saldo Final", f"R$ {saldo:,.2f}"]
        ]

        for i, linha in enumerate(resumo, start=3):
            worksheet.cell(row=i, column=1, value=linha[0])
            worksheet.cell(row=i, column=2, value=linha[1])

        # Adjusting column widths
        for column_cells in worksheet.columns:
            length = max(
                len(str(cell.value)) if cell.value is not None else 0 for cell in column_cells)
            adjusted_width = length + 2
            col_letter = column_cells[0].column_letter
            worksheet.column_dimensions[col_letter].width = adjusted_width

    return filepath
