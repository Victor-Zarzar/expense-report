import pandas as pd
import os


def load_data(filepath: str) -> pd.DataFrame:
    """Loads and validates spending data from a CSV file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")

    try:
        df = pd.read_csv(filepath)
    except Exception as e:
        raise ValueError(f"Erro ao ler o arquivo CSV: {e}")

    # Check if required columns exist
    required_columns = {"categoria", "descricao", "valor", "data"}
    if not required_columns.issubset(df.columns):
        raise ValueError(
            f"Colunas obrigatórias faltando. Esperado: {required_columns}")

    # Convert numeric values
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df['data'] = pd.to_datetime(df['data'], errors='coerce')

    # Remove invalid entries
    df = df.dropna(subset=['valor', 'data'])

    return df
