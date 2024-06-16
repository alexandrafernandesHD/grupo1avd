import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
file_path = '/content/datasNOS.csv'
df = pd.read_csv(file_path)


df = df[df['DATA'] != 'none']

# Converte a coluna 'DATA' para datetime
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')

# Extrai o mês e o ano de cada data
df['Year_Month'] = df['DATA'].dt.to_period('M')

# Conta o número de artigos por mês e ano
article_counts = df['Year_Month'].value_counts().sort_index()

# Gráfico
plt.figure(figsize=(12, 6))

# Gráfico de linha
plt.plot(article_counts.index.astype(str), article_counts.values, marker='o', color='blue', linestyle='-', label='Linha')

# Gráfico de barras
article_counts.plot(kind='bar', color='orange', alpha=0.7, label='Barras')

plt.xlabel('Mês e Ano')
plt.ylabel('Quantidade de Artigos')
plt.title('Quantidade de Artigos por Mês e Ano')
plt.xticks(rotation=90)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Mostrar o gráfico
plt.show()
