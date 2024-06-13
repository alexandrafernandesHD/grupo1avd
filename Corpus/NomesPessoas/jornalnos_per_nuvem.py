import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_path = '/content/contaperNOS.csv'
data = pd.read_csv(file_path, sep=';')

# Substituir os nomes
replace_names = {
    "Lloyd Braga": "Carlos Lloyd Braga",
    "Lloyd": "Carlos Lloyd Braga",
    "Carlos Pazos": "Carlos Pazos Justo",
    "Veiga Simão": "José Veiga Simão",
    "Vítor": "Vítor Rodrigues",
    "Vítor de Carapeços": "Vítor Rodrigues",
    "Vítor**": "Vítor Rodrigues",
    "Paula": "Paula Costa"
}

exclude_names = ["Orpheu", "Dona"]

data['PER'] = data['PER'].replace(replace_names)
data = data[~data['PER'].isin(exclude_names)]

# Ajuste de ocorrências
data.loc[data['PER'] == "Carlos Lloyd Braga", 'Oco'] = 22
data.loc[data['PER'] == "Lloyd Braga", 'Oco'] = 22
data.loc[data['PER'] == "Lloyd", 'Oco'] = 4
data.loc[data['PER'] == "Vítor Rodrigues", 'Oco'] += 2
data.loc[data['PER'] == "Paula Costa", 'Oco'] += 5


grouped_data = data.groupby('PER')['Oco'].sum().reset_index()

# Dicionário com os nomes e suas ocorrências
word_freq = dict(zip(grouped_data['PER'], grouped_data['Oco']))

# Criar a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)

# Nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Nuvem de Palavras dos Nomes no Jornal Nós')
plt.show()