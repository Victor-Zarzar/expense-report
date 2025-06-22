import matplotlib.pyplot as plt
import os


def generate_pie_chart(df):
    grouped = df.groupby('categoria')['valor'].sum()
    fig, ax = plt.subplots()
    ax.pie(grouped, labels=grouped.index, autopct='%1.1f%%')
    plt.title('Distribuição de Gastos por Categoria')
    output_path = 'reports/pie_chart.png'
    plt.savefig(output_path)
    plt.close()
    return output_path
