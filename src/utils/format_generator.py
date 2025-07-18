import os
import re
from datetime import datetime


# Get the latest expense CSV file based on a specific naming pattern.
def get_latest_expense_csv(data_folder='data'):
    pattern = re.compile(r'expenses_(\d{4})_(\d{2})\.csv')
    latest_file = None
    latest_date = None

    for filename in os.listdir(data_folder):
        match = pattern.match(filename)
        if match:
            year, month = map(int, match.groups())
            file_date = datetime(year, month, 1)

            if not latest_date or file_date > latest_date:
                latest_date = file_date
                latest_file = filename

    if latest_file:
        return os.path.join(data_folder, latest_file)
    else:
        raise FileNotFoundError(
            "Nenhum arquivo de despesas encontrado em formato 'expenses_YYYY_MM.csv'")
