import pandas as pd
import matplotlib.pyplot as plt

# Jornal Nós
file_path_nos = '/content/contaperNOS.csv'
data_nos = pd.read_csv(file_path_nos, sep=';')

replace_names_nos = {
    "Lloyd Braga": "Carlos Lloyd Braga",
    "Lloyd": "Carlos Lloyd Braga",
    "Carlos Pazos": "Carlos Pazos Justo",
    "Veiga Simão": "José Veiga Simão",
    "Vítor": "Vítor Rodrigues",
    "Vítor de Carapeços": "Vítor Rodrigues",
    "Vítor**": "Vítor Rodrigues",
    "Paula": "Paula Costa"
}

exclude_names_nos = ["Orpheu", "Dona"]

data_nos['PER'] = data_nos['PER'].replace(replace_names_nos)
data_nos = data_nos[~data_nos['PER'].isin(exclude_names_nos)]

data_nos.loc[data_nos['PER'] == "Carlos Lloyd Braga", 'Oco'] = 22
data_nos.loc[data_nos['PER'] == "Lloyd Braga", 'Oco'] = 22
data_nos.loc[data_nos['PER'] == "Lloyd", 'Oco'] = 4
data_nos.loc[data_nos['PER'] == "Vítor Rodrigues", 'Oco'] += 2
data_nos.loc[data_nos['PER'] == "Paula Costa", 'Oco'] += 5

grouped_data_nos = data_nos.groupby('PER')['Oco'].sum().reset_index()

top_n = 15
grouped_data_nos = grouped_data_nos.sort_values(by='Oco', ascending=False).head(top_n)

# CorpusR
file_path_corpusr = '/content/contaperCORPUSR.csv'
data_corpusr = pd.read_csv(file_path_corpusr, sep=';')

replace_names_corpusr = {
    "L.G.": "Luís Garcia",
    "Luís Garcia": "Luís Garcia",
    "Muffin": "Maria Valada (\"Muffin\")",
    "Maria Valada": "Maria Valada (\"Muffin\")"
}

exclude_names_corpusr = [
    "Prof", "ARCUM", "FADU", "D. Pedro V", "Afonsina", "Weadapt",
    "Elisa Siquara I ComUM", "Elisa Siquara", "Marta Rodrigues | ComUM",
    "| Marta Rodrigues", "Marta Rodrigues", "Ana Marques", "Nuno Gonçalves",
    "Joana Oliveira", "Maria Francisca Barros", "Lloyd Braga"
]

data_corpusr['PER'] = data_corpusr['PER'].replace(replace_names_corpusr)
data_corpusr = data_corpusr[~data_corpusr['PER'].isin(exclude_names_corpusr)]

grouped_data_corpusr = data_corpusr.groupby('PER')['Oco'].sum().reset_index()

grouped_data_corpusr = grouped_data_corpusr.sort_values(by='Oco', ascending=False).head(top_n)

# Coloca os gráficos à beira um do outro
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# Gráfico (Jornal Nós)
axs[0].bar(grouped_data_nos['PER'], grouped_data_nos['Oco'], color='skyblue')
axs[0].set_xlabel('Nome')
axs[0].set_ylabel('Número de Ocorrências')
axs[0].set_title(f'Top {top_n} Ocorrências de Pessoas no Jornal Nós')
axs[0].set_xticklabels(grouped_data_nos['PER'], rotation=90)

# Plot Gráfico (CorpusR)
axs[1].bar(grouped_data_corpusr['PER'], grouped_data_corpusr['Oco'], color='blue')
axs[1].set_xlabel('Nome')
axs[1].set_ylabel('Número de Ocorrências')
axs[1].set_title(f'Top {top_n} Ocorrências de Pessoas no CorpusR')
axs[1].set_xticklabels(grouped_data_corpusr['PER'], rotation=90)

plt.tight_layout()
plt.show()