import pandas as pd
from datetime import datetime
import os


def export_to_excel(df: pd.DataFrame, output_dir: str = "reports") -> str:
    """Exports the expense DataFrame to Excel with financial summary on top."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    filename = f"expenses_{datetime.now().strftime('%Y_%m')}.xlsx"
    filepath = os.path.join(output_dir, filename)

    df_sorted = df.sort_values(by="data")

    # Classification of types
    CATEGORIES_VARIABLES = ["Aluguel", "Investimentos",
                            "Impostos", "Saúde", "Lazer", "Gastos Extras"]
    CATEGORIES_FIXED_REVENUE = ["Salário"]

    def classificar_linha(row):
        if row['categoria'] in CATEGORIES_FIXED_REVENUE:
            return 'receita_fixa'
        elif row['categoria'] == "Adicionais":
            return 'receita_variavel'
        elif row['categoria'] in CATEGORIES_VARIABLES:
            return 'despesa_variavel'
        else:
            return 'despesa_fixa'

    df_sorted['tipo'] = df_sorted.apply(classificar_linha, axis=1)

    receitas_fixas = df_sorted[df_sorted['tipo']
                               == 'receita_fixa']['valor'].sum()
    receitas_variaveis = df_sorted[df_sorted['tipo']
                                   == 'receita_variavel']['valor'].sum()
    despesas_fixas = df_sorted[df_sorted['tipo']
                               == 'despesa_fixa']['valor'].sum()
    despesas_variaveis = df_sorted[df_sorted['tipo']
                                   == 'despesa_variavel']['valor'].sum()
    saldo = (receitas_fixas + receitas_variaveis) - \
        (despesas_fixas + despesas_variaveis)

    # Export with ExcelWriter
    with pd.ExcelWriter(filepath, engine="openpyxl", datetime_format="DD/MM/YYYY") as writer:
        # First: write the DataFrame
        df_sorted.drop(columns="tipo").to_excel(
            writer, index=False, sheet_name="Gastos", startrow=7)

        worksheet = writer.sheets["Gastos"]
        workbook = writer.book

        # Write the summary manually in the first lines
        resumo = [
            ["Resumo Financeiro", ""],
            ["Receitas Fixas", f"R$ {receitas_fixas:,.2f}"],
            ["Receitas Variáveis", f"R$ {receitas_variaveis:,.2f}"],
            ["Despesas Fixas", f"R$ {despesas_fixas:,.2f}"],
            ["Despesas Variáveis", f"R$ {despesas_variaveis:,.2f}"],
            ["Saldo Final", f"R$ {saldo:,.2f}"]
        ]

        for i, linha in enumerate(resumo, start=1):
            worksheet.cell(row=i, column=1, value=linha[0])
            worksheet.cell(row=i, column=2, value=linha[1])

        # Adjust column width
        for column_cells in worksheet.columns:
            length = max(
                len(str(cell.value)) if cell.value is not None else 0 for cell in column_cells)
            adjusted_width = length + 2
            col_letter = column_cells[0].column_letter
            worksheet.column_dimensions[col_letter].width = adjusted_width

    return filepath
