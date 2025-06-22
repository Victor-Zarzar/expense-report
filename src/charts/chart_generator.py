import matplotlib.pyplot as plt
import os


def generate_pie_chart(df):
    # Delete recipes
    df = df[~df['categoria'].str.lower().str.contains('salário|adicional')]

    # Group values ​​by category
    grouped = df.groupby('categoria')[
        'valor'].sum().sort_values(ascending=False)

    total = grouped.sum()
    threshold = 0.04 * total
    grouped_filtered = grouped[grouped >= threshold]
    others = grouped[grouped < threshold].sum()
    if others > 0:
        grouped_filtered["Outros"] = others

    labels = grouped_filtered.index
    values = grouped_filtered.values

    # Chart
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=labels,
        autopct=lambda pct: f'{pct:.1f}%\nR${pct * total / 100:.0f}',
        startangle=140,
        colors=plt.cm.tab20.colors[:len(labels)],
        textprops=dict(color="black", fontsize=9)
    )

    ax.axis('equal')
    plt.title('Distribuição de Gastos por Categoria', fontsize=12)
    plt.tight_layout()

    # File path
    output_path = 'reports/pie_chart.png'
    plt.savefig(output_path)
    plt.close()

    return output_path
