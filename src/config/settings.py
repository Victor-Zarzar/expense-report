from pydantic_settings import BaseSettings, SettingsConfigDict


class FinanceSettings(BaseSettings):
    REFERENCE_MONTH: str

    SALARIO: float
    ADICIONAL_SALARIO: float = 0

    ALUGUEL: float
    INTERNET: float
    CONDOMINIO: float
    ENERGIA: float
    PLANO_CELULAR: float
    IMPOSTOS_MENSAIS: float

    SAUDE: float
    LAZER: float
    INVESTIMENTOS: float
    GASTOS_EXTRAS: float

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


finance_settings = FinanceSettings()
