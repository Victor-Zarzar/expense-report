from datetime import datetime

import pandas as pd

from config.settings import FinanceSettings


def build_expenses_dataframe(settings: FinanceSettings) -> pd.DataFrame:
    rows = [
        ("Salário", "Salário Mensal", settings.SALARIO),
        ("Adicionais (Salário)", "Adicional", settings.ADICIONAL_SALARIO),
        ("Aluguel", "Aluguel Mensal", settings.ALUGUEL),
        ("Internet", "Internet", settings.INTERNET),
        ("Condominio", "Condomínio", settings.CONDOMINIO),
        ("Energia", "Energia Elétrica", settings.ENERGIA),
        ("Plano Celular", "Celular", settings.PLANO_CELULAR),
        ("Impostos mensais", "Impostos", settings.IMPOSTOS_MENSAIS),
        ("Saúde", "Plano de Saúde", settings.SAUDE),
        ("Lazer", "Lazer", settings.LAZER),
        ("Investimentos", "Investimentos", settings.INVESTIMENTOS),
        ("Gastos Extras", "Extras", settings.GASTOS_EXTRAS),
    ]

    df = pd.DataFrame(rows, columns=["categoria", "descricao", "valor"])
    df = df[df["valor"] > 0]

    df["data"] = datetime.now()
    df["mes_referencia"] = settings.REFERENCE_MONTH

    return df
