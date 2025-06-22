from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


# Categories considered variable expenses
CATEGORIES_VARIABLES = [
    "Aluguel", "Investimentos", "Impostos", "Saúde", "Lazer", "Gastos Extras"
]

# Categories considered fixed income
CATEGORIES_FIXED_REVENUE = ["Salário"]


def generate_pdf(df, chart_path):
    doc = SimpleDocTemplate("reports/expenses_2025_07.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    def classificar_linha(row):
        if row['categoria'] in CATEGORIES_FIXED_REVENUE:
            return 'receita_fixa'
        elif row['categoria'] == "Adicionais":
            return 'receita_variavel'
        elif row['categoria'] in CATEGORIES_VARIABLES:
            return 'despesa_variavel'
        else:
            return 'despesa_fixa'

    df['tipo'] = df.apply(classificar_linha, axis=1)

    receitas_fixas = df[df['tipo'] == 'receita_fixa']['valor'].sum()
    receitas_variaveis = df[df['tipo'] == 'receita_variavel']['valor'].sum()
    despesas_fixas = df[df['tipo'] == 'despesa_fixa']['valor'].sum()
    despesas_variaveis = df[df['tipo'] == 'despesa_variavel']['valor'].sum()

    saldo = (receitas_fixas + receitas_variaveis) - \
        (despesas_fixas + despesas_variaveis)

    grouped = df.groupby('categoria')['valor'].sum()

    story.append(Paragraph("Relatório de Gastos Mensais", styles['Title']))
    story.append(Paragraph(
        f"Data de geração: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(Spacer(1, 9))

    # Resume
    story.append(Paragraph("Resumo Financeiro:", styles['Heading2']))
    story.append(
        Paragraph(f"Receitas Fixas: R$ {receitas_fixas:,.2f}", styles['Normal']))
    story.append(Paragraph(
        f"Receitas Variáveis: R$ {receitas_variaveis:,.2f}", styles['Normal']))
    story.append(
        Paragraph(f"Despesas Fixas: R$ {despesas_fixas:,.2f}", styles['Normal']))
    story.append(Paragraph(
        f"Despesas Variáveis: R$ {despesas_variaveis:,.2f}", styles['Normal']))
    story.append(
        Paragraph(f"<b>Saldo Final: R$ {saldo:,.2f}</b>", styles['Normal']))
    story.append(Spacer(1, 9))

    story.append(Paragraph("Resumo por Categoria:", styles['Heading2']))
    for categoria, valor in grouped.items():
        story.append(
            Paragraph(f"{categoria}: R$ {valor:.2f}", styles['Normal']))
    story.append(Spacer(1, 18))

    # Chart
    story.append(Paragraph("Gráfico de Gastos:", styles['Heading2']))
    story.append(Image(chart_path, width=400, height=300))

    doc.build(story)
