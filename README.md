<h1 align="center" id="header">
  Gerador de Relatórios de Despesas
</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white" alt="Matplotlib">
</p>

<p align="center">
  Automatize seus relatórios mensais de despesas com Python. Gere relatórios profissionais em PDF, planilhas Excel e gráficos visuais a partir das suas configurações financeiras.
</p>

---

<h2 id="stack">
  Stack Tecnológica
</h2>

<p>
<img src="https://github.com/tandpfun/skill-icons/blob/main/icons/Python-Dark.svg" width="48" title="Python">
</p>

### Tecnologias Principais

- **Python 3.11+** - Linguagem de programação principal
- **Pydantic Settings V2** - Gerenciamento de configurações e validação
- **ReportLab** - Geração profissional de PDFs
- **Matplotlib** - Visualização de dados e gráficos
- **Pandas** - Manipulação e análise de dados
- **OpenPyXL** - Geração de arquivos Excel com formatação

### Recursos & Integrações

- **Validação de Configurações** - Validação automática de dados financeiros via Pydantic
- **Variáveis de Ambiente** - Configuração segura através de arquivo `.env`
- **Gráficos de Pizza** - Distribuição visual por categoria
- **Relatórios PDF** - Relatórios financeiros detalhados com resumos
- **Exportação Excel** - Planilhas auto-formatadas com cálculos
- **Automação Makefile** - Comandos simplificados de workflow

---

<h2 id="prerequisites">
  Pré-requisitos
</h2>

Antes de começar, certifique-se de ter instalado:

- [Python](https://www.python.org/downloads/) (v3.11 ou superior) - runtime principal
- [Make](https://www.gnu.org/software/make/) - ferramenta de automação de build
- [Git](https://git-scm.com/)

---

<h2 id="installation">
  Instalação & Configuração
</h2>

### 1. Clone o Repositório

```bash
git clone https://github.com/Victor-Zarzar/expense-report
cd expense-report
```

### 2. Abra no seu editor (exemplo: Zed Editor)

```bash
zed .
```

### 3. Configuração do Ambiente

Copie o arquivo de exemplo e configure suas despesas:

```bash
cp .env-example .env
```

Em seguida, edite o `.env` com seus valores reais:

```env
REFERENCE_MONTH=2026/01
SALARIO=6000
ADICIONAL_SALARIO=1500
ALUGUEL=1500
INTERNET=150
CONDOMINIO=350
ENERGIA=400
PLANO_CELULAR=120
IMPOSTOS_MENSAIS=400
SAUDE=600
LAZER=500
INVESTIMENTOS=1500
GASTOS_EXTRAS=300
```

> **Importante:** Nunca faça commit do seu arquivo `.env` para o controle de versão. Ele já está no `.gitignore`.

### 4. Instale as Dependências

```bash
make install
```

Ou manualmente com pip:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

<h2 id="usage">
  Uso
</h2>

### Comandos Disponíveis

Visualize todos os comandos Make disponíveis:

```bash
make help
```

### Estrutura de Configuração

O projeto utiliza **Pydantic Settings V2** para gerenciar suas configurações financeiras de forma type-safe:

```python
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
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )
```

### Gerar Relatórios

#### Relatório Completo (PDF + Excel)

```bash
make create
```

#### Apenas Relatório PDF

```bash
make create-pdf
```

#### Apenas Relatório Excel

```bash
make create-excel
```

Os arquivos gerados serão salvos no diretório `reports/`.

---

<h2 id="makefile-commands">
  Referência de Comandos do Makefile
</h2>

| Comando             | Descrição                                        |
| ------------------- | ------------------------------------------------ |
| `make install`      | Instala dependências e configura virtualenv      |
| `make create`       | Gera relatório completo (PDF + Excel + Gráficos) |
| `make create-pdf`   | Gera apenas o relatório PDF                      |
| `make create-excel` | Gera apenas o relatório Excel                    |
| `make setup`        | Cria ambiente virtual                            |
| `make clean`        | Remove relatórios, imagens e artefatos           |
| `make help`         | Mostra todos os comandos disponíveis             |

---

<h2 id="project-structure">
  Estrutura do Projeto
</h2>

```
expense-report/
├── reports/                # PDFs, Excel e gráficos gerados
│   ├── *.pdf
│   ├── *.xlsx
│   └── *.png
├── src/
│   ├── config/            # Configurações do projeto
│   │   └── settings.py    # Pydantic Settings (FinanceSettings)
│   ├── domain/            # Lógica de domínio
│   │   └── expense_builder.py  # Construtor de despesas
│   ├── charts/            # Geração de gráficos (pizza, etc.)
│   ├── reports/           # Geradores de relatório PDF e Excel
│   └── main.py            # Ponto de entrada principal
├── .env                   # Variáveis de ambiente (não commitado)
├── .env-example           # Template de variáveis de ambiente
├── Makefile               # Automação de build
├── requirements.txt       # Dependências Python
└── README.md              # Documentação do projeto
```

---

<h2 id="features">
  Funcionalidades
</h2>

### Geração de Relatórios

- **Relatórios PDF**: Relatórios financeiros profissionais com resumos por categoria, cálculos totais e gráficos embutidos
- **Exportação Excel**: Planilhas auto-formatadas com fórmulas, tabelas de resumo e estilização profissional
- **Gráficos Visuais**: Gráficos de pizza mostrando distribuição de despesas por categoria

### Processamento de Dados

- **Validação com Pydantic**: Validação automática e type-safe das configurações financeiras
- **Variáveis de Ambiente**: Configuração segura através de arquivo `.env`
- **Agrupamento por Categoria**: Agrupamento inteligente de despesas por categoria
- **Tratamento de Datas**: Suporte para rastreamento de despesas baseado em datas
- **Estatísticas de Resumo**: Cálculo automático de totais e percentuais

### Automação

- **Integração Makefile**: Comandos simples para todas as operações
- **Processamento em Lote**: Geração de múltiplos relatórios de uma vez

---

<h2 id="environment-variables">
  Variáveis de Ambiente
</h2>

O arquivo `.env-example` contém todas as variáveis necessárias com valores de exemplo:

| Variável            | Descrição                          | Exemplo   |
| ------------------- | ---------------------------------- | --------- |
| `REFERENCE_MONTH`   | Mês de referência do relatório     | `2026/01` |
| `SALARIO`           | Salário líquido mensal             | `6000`    |
| `ADICIONAL_SALARIO` | Bônus ou adicionais (opcional)     | `1500`    |
| `ALUGUEL`           | Valor do aluguel                   | `1500`    |
| `INTERNET`          | Plano de internet                  | `150`     |
| `CONDOMINIO`        | Taxa de condomínio                 | `350`     |
| `ENERGIA`           | Conta de luz                       | `400`     |
| `PLANO_CELULAR`     | Plano de celular                   | `120`     |
| `IMPOSTOS_MENSAIS`  | Impostos mensais (INSS, DAS, etc.) | `400`     |
| `SAUDE`             | Gastos com saúde                   | `600`     |
| `LAZER`             | Gastos com lazer                   | `500`     |
| `INVESTIMENTOS`     | Valor investido mensalmente        | `1500`    |
| `GASTOS_EXTRAS`     | Despesas extras e variáveis        | `300`     |

---

<h2 id="development">
  Desenvolvimento
</h2>

### Executando Localmente

Ative seu ambiente virtual:

```bash
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

Execute o script principal:

```bash
python src/main.py
```

### Adicionando Novas Funcionalidades

O projeto é organizado em módulos para fácil extensão:

- Adicione novos tipos de gráfico em `src/charts/`
- Estenda layouts de PDF em `src/reports/pdf_generator.py`
- Adicione recursos Excel em `src/reports/excel_generator.py`
- Modifique configurações em `src/config/settings.py`
- Ajuste lógica de negócio em `src/domain/expense_builder.py`

### Linting & Formatação

Verifique problemas no código:

```bash
python -m pylint src/
```

Formate automaticamente:

```bash
python -m black src/
```

---

<h2 id="contributing">
  Contribuindo
</h2>

Contribuições são bem-vindas! Sinta-se à vontade para enviar um Pull Request.

1. Faça um Fork do projeto
2. Crie sua branch de feature (`git checkout -b feature/NovaFuncionalidade`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. Push para a branch (`git push origin feature/NovaFuncionalidade`)
5. Abra um Pull Request

---

<h2 id="license">
  Licença
</h2>

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

<h2 id="contact">
  Contato
</h2>

Victor Zarzar - [@Victor-Zarzar](https://github.com/Victor-Zarzar)

Link do Projeto: [https://github.com/Victor-Zarzar/expense-report](https://github.com/Victor-Zarzar/expense-report)

---

<p align="center">
  Feito com ❤️ por Victor Zarzar
</p>
