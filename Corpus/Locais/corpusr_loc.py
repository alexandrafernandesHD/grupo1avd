import pandas as pd
import matplotlib.pyplot as plt


file_path = '/content/contalocCORPUSR.csv'
data = pd.read_csv(file_path, sep=';')

# Substituir
data['LOC'] = data['LOC'].replace({
    "Universidade de o Minho": "Universidade do Minho",
    "UMinho": "Universidade do Minho",
    "em Portugal": "Portugal"
})

# Lista de exclusão
exclude_names = [
    "Universidade", "universidade", "AAUMinho", "Universidades", "FADU", "SASUM", 
    "Governo", "Escola", "Ensino Superior", "Desporto", "RGA"
]

# Excluir
data = data[~data['LOC'].isin(exclude_names)]

# Agrupar os dados
grouped_data = data.groupby('LOC')['Oco'].sum().reset_index()


top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Gráfico
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['LOC'], grouped_data['Oco'], color='blue')
plt.xlabel('Local')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Locais no CorpusR')
plt.xticks(rotation=90)
plt.show()