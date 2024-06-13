import pandas as pd
from wordcloud import WordCloud
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

# Corrigir o número de ocorrências para "LLoyd Braga"
if 'LLoyd Braga' in data['PER'].values:
    total_lloyd_occurrences = data.loc[data['PER'] == 'LLoyd Braga', 'Oco'].sum()
    data = data[data['PER'] != 'LLoyd Braga']
    data = data.append({'PER': 'LLoyd Braga', 'Oco': 8}, ignore_index=True)

# Agrupar os dados pelo nome
grouped_data = data.groupby('PER')['Oco'].sum().reset_index()

# Dicionário com os nomes e suas ocorrências
word_freq = dict(zip(grouped_data['PER'], grouped_data['Oco']))

# Criar a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras dos Nomes em CorpusR')
plt.show()