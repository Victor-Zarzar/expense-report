from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime

# Categories considered variable expenses
CATEGORIES_VARIABLES = [
    "Aluguel", "Investimentos", "Impostos mensais", "Saúde", "Lazer", "Gastos Extras"
]

# Categories considered fixed income
CATEGORIES_FIXED_REVENUE = ["Salário"]

# Updated mapping of categories to payment methods
PAYMENT_METHOD_MAPPING = {
    "Salário": "Pix",
    "Adicionais (Salário)": "Pix",
    "Internet": "Débito Automático",
    "Condominio": "Pix",
    "Energia": "Pix",
    "Plano Celular": "Pix",
    "Investimentos": "Pix",
    "Impostos mensais": "Débito Automático",
    "Gastos Extras": "Cartão de Crédito",
    "Alimentação": "Cartão de Débito",
    "Transporte": "Cartão de Débito",
    "Lazer": "Cartão de Crédito",
    "Aluguel": "Pix",
    "Saúde": "Cartão de Débito"
}


def generate_pdf(df, chart_path):
    """
    Generates a PDF report with financial and payment method analysis   
    """
    styles = getSampleStyleSheet()
    story = []

    # Detect reference month
    reference_month = df['mes_referencia'].iloc[0].replace('/', '_').lower()
    pdf_path = f"reports/expenses_{reference_month}.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=A4)

    # Classify line type (revenue/fixed/variable expense)
    def classify_line(row):
        if row['categoria'] in CATEGORIES_FIXED_REVENUE:
            return 'receita_fixa'
        elif row['categoria'] == "Adicionais (Salário)":
            return 'receita_variavel'
        elif row['categoria'] in CATEGORIES_VARIABLES:
            return 'despesa_variavel'
        else:
            return 'despesa_fixa'

    # Apply ratings
    df['tipo'] = df.apply(classify_line, axis=1)
    df['metodo_pagamento'] = df['categoria'].map(PAYMENT_METHOD_MAPPING)

    # Total calculations
    fixed_recipes = df[df['tipo'] == 'receita_fixa']['valor'].sum()
    variable_recipes = df[df['tipo'] == 'receita_variavel']['valor'].sum()
    fixed_expenses = df[df['tipo'] == 'despesa_fixa']['valor'].sum()
    variable_expenses = df[df['tipo'] == 'despesa_variavel']['valor'].sum()
    balance = (fixed_recipes + variable_recipes) - \
        (fixed_expenses + variable_expenses)

    grouped = df.groupby('categoria')['valor'].sum()
    payment_grouped = df.groupby('metodo_pagamento')['valor'].sum()

    # Headers
    story.append(Paragraph(
        f"Relatório de Gastos - {df['mes_referencia'].iloc[0]}", styles['Title']))
    story.append(Paragraph(
        f"Data de geração: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Financial summary
    story.append(Paragraph("Resumo Financeiro:", styles['Heading2']))
    story.append(
        Paragraph(f"Receitas Fixas: R$ {fixed_recipes:,.2f}", styles['Normal']))
    story.append(Paragraph(
        f"Receitas Variáveis: R$ {variable_recipes:,.2f}", styles['Normal']))
    story.append(
        Paragraph(f"Despesas Fixas: R$ {fixed_expenses:,.2f}", styles['Normal']))
    story.append(Paragraph(
        f"Despesas Variáveis: R$ {variable_expenses:,.2f}", styles['Normal']))
    story.append(
        Paragraph(f"<b>Saldo Final: R$ {balance:,.2f}</b>", styles['Normal']))
    story.append(Spacer(1, 12))

    # Summary by category
    story.append(Paragraph("Resumo por Categoria:", styles['Heading2']))
    for categoria, valor in grouped.items():
        story.append(
            Paragraph(f"{categoria}: R$ {valor:.2f}", styles['Normal']))
    story.append(Spacer(1, 12))

    # Summary by category
    story.append(
        Paragraph("Análise por Método de Pagamento:", styles['Heading2']))

    # Use of cards
    card_expenses = df[df['metodo_pagamento'].isin(
        ['Cartão de Crédito', 'Cartão de Débito'])]
    total_card_spending = card_expenses['valor'].sum()
    total_expenses = fixed_expenses + variable_expenses
    card_percentage = (total_card_spending / total_expenses) * \
        100 if total_expenses > 0 else 0

    story.append(Paragraph(
        f"<b>Gastos com Cartões: R$ {total_card_spending:,.2f} ({card_percentage:.1f}% do total)</b>", styles['Normal']))
    story.append(Spacer(1, 6))

    for metodo, valor in payment_grouped.items():
        if metodo in ['Cartão de Crédito', 'Cartão de Débito']:
            story.append(
                Paragraph(f"• {metodo}: R$ {valor:.2f}", styles['Normal']))
    story.append(Spacer(1, 6))

    # Use of Pix
    pix_expenses = df[df['metodo_pagamento'] == 'Pix']
    total_pix_spending = pix_expenses['valor'].sum()
    pix_percentage = (total_pix_spending / total_expenses) * \
        100 if total_expenses > 0 else 0

    story.append(Paragraph(
        f"<b>Gastos via Pix: R$ {total_pix_spending:,.2f} ({pix_percentage:.1f}% do total)</b>", styles['Normal']))
    story.append(Spacer(1, 6))

    # Detailed table
    story.append(
        Paragraph("Detalhamento por Método de Pagamento:", styles['Heading3']))

    table_data = [['Método de Pagamento', 'Valor Total', '% do Total']]
    for metodo, valor in payment_grouped.items():
        percentage = (valor / total_expenses) * \
            100 if total_expenses > 0 else 0
        table_data.append([metodo, f"R$ {valor:.2f}", f"{percentage:.1f}%"])

    # Table style
    table = Table(table_data, colWidths=[150, 100, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    story.append(table)
    story.append(Spacer(1, 12))

    # Recommendations
    story.append(
        Paragraph("Recomendações sobre Uso de Cartão:", styles['Heading3']))
    if card_percentage > 50:
        story.append(Paragraph(
            "• Alto uso de cartão - considere revisar gastos com cartão de crédito", styles['Normal']))
    elif card_percentage > 30:
        story.append(Paragraph(
            "• Uso moderado de cartão - monitore os gastos regularmente", styles['Normal']))
    else:
        story.append(
            Paragraph("• Baixo uso de cartão - bom controle financeiro", styles['Normal']))
    story.append(Spacer(1, 6))

    story.append(
        Paragraph("Recomendações sobre Uso de Pix:", styles['Heading3']))
    if pix_percentage > 70:
        story.append(Paragraph(
            "• Uso intenso de Pix — excelente agilidade nos pagamentos.", styles['Normal']))
    elif pix_percentage > 40:
        story.append(Paragraph(
            "• Uso equilibrado de Pix — ótimo controle digital.", styles['Normal']))
    else:
        story.append(Paragraph(
            "• Baixo uso de Pix — avalie migrar pagamentos para Pix quando possível.", styles['Normal']))
    story.append(Spacer(1, 18))

    # Chart
    story.append(Paragraph("Gráfico de Gastos:", styles['Heading2']))
    story.append(Image(chart_path, width=400, height=300))

    doc.build(story)
    print("Relatório gerado com sucesso!")
