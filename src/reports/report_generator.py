from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_pdf(df, chart_path):
    doc = SimpleDocTemplate("reports/expenses_2025_07.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    total = df['valor'].sum()
    grouped = df.groupby('categoria')['valor'].sum()

    story.append(Paragraph("Relatório de Gastos Mensais", styles['Title']))
    story.append(Paragraph(
        f"Data de geração: {datetime.now().strftime('%d/%m/%Y')}", styles['Normal']))
    story.append(Paragraph(f"Total: R$ {total:,.2f}", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Resumo por categoria:", styles['Heading2']))
    for categoria, valor in grouped.items():
        story.append(
            Paragraph(f"{categoria}: R$ {valor:.2f}", styles['Normal']))

    story.append(Spacer(1, 24))
    story.append(Paragraph("Gráfico:", styles['Heading2']))
    story.append(Image(chart_path, width=400, height=300))

    doc.build(story)
