import os
from models.data_loader import load_data
from charts.chart_generator import generate_pie_chart
from reports.report_generator import generate_pdf
from reports.excel_exporter import export_to_excel


# This script serves as the main entry point for generating reports.
def main():
    df = load_data('data/expenses_2025_08.csv')
    mode = os.environ.get("MODE", "all")

    if mode == "pdf":
        chart_path = generate_pie_chart(df)
        generate_pdf(df, chart_path)
    elif mode == "excel":
        export_to_excel(df)
    else:
        chart_path = generate_pie_chart(df)
        generate_pdf(df, chart_path)
        export_to_excel(df)


if __name__ == "__main__":
    main()
