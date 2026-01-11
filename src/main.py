import os

from charts.chart_generator import generate_pie_chart
from config.settings import finance_settings
from domain.expense_builder import build_expenses_dataframe
from reports.excel_exporter import export_to_excel
from reports.report_generator import generate_pdf


def main():
    """
    Main entrypoint for expense report generation.

    Data source:
        - Environment variables (validated by Pydantic Settings)

    Output modes:
        - pdf
        - excel
        - all (default)
    """
    mode = os.getenv("MODE", "all").lower()

    df = build_expenses_dataframe(finance_settings)

    if mode == "pdf":
        chart_path = generate_pie_chart(df)
        generate_pdf(df, chart_path)

    elif mode == "excel":
        export_to_excel(df)

    elif mode == "all":
        chart_path = generate_pie_chart(df)
        generate_pdf(df, chart_path)
        export_to_excel(df)

    else:
        raise ValueError(f"Invalid MODE '{mode}'. Expected: pdf, excel, or all.")


if __name__ == "__main__":
    main()
