from models.data_loader import load_data
from charts.chart_generator import generate_pie_chart
from reports.report_generator import generate_pdf


def main():
    df = load_data('data/expenses_2025_07.csv')
    chart_path = generate_pie_chart(df)
    generate_pdf(df, chart_path)


if __name__ == "__main__":
    main()
