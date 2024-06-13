import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/contaperCORPUSR.csv'
data = pd.read_csv(file_path, sep=';')

# Substituir os nomes
data['PER'] = data['PER'].replace({
    "L.G.": "Luís Garcia",
    "Luís Garcia": "Luís Garcia",
    "Muffin": "Maria Valada (\"Muffin\")",
    "Maria Valada": "Maria Valada (\"Muffin\")"
})

# Nomes a excluir
exclude_names = [
    "Prof", "ARCUM", "FADU", "D. Pedro V", "Afonsina", "Weadapt",
    "Elisa Siquara I ComUM", "Elisa Siquara", "Marta Rodrigues | ComUM",
    "| Marta Rodrigues", "Marta Rodrigues", "Ana Marques", "Nuno Gonçalves",
    "Joana Oliveira", "Maria Francisca Barros", "Lloyd Braga"
]
data = data[~data['PER'].isin(exclude_names)]

# Agrupar os dados pelo nome e somar as ocorrências
grouped_data = data.groupby('PER')['Oco'].sum().reset_index()

# Ordenar os dados pela contagem de ocorrências
top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Criar o gráfico de Barras
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['PER'], grouped_data['Oco'], color='blue')
plt.xlabel('Nome')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Pessoas no CorpusR')
plt.xticks(rotation=90)
plt.show()