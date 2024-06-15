import pandas as pd
import matplotlib.pyplot as plt

# Jornal Nós
file_path_nos = '/content/contalocNOS.csv'
data_nos = pd.read_csv(file_path_nos, sep=';')

replace_names_nos = {
    "em Portugal": "Portugal",
    "Universidade de o Minho": "Universidade do Minho",
    "UMinho": "Universidade do Minho",
    "Norte": "Norte de Portugal"
}

exclude_names_nos = ["AFUM", "NIG", "Via láctea", "Escola", "Universidade"]

data_nos['LOC'] = data_nos['LOC'].replace(replace_names_nos)
data_nos = data_nos[~data_nos['LOC'].isin(exclude_names_nos)]

data_nos.loc[(data_nos['LOC'] == "Reitoria"), 'Oco'] = 9

grouped_data_nos = data_nos.groupby('LOC')['Oco'].sum().reset_index()

top_n = 15
grouped_data_nos = grouped_data_nos.sort_values(by='Oco', ascending=False).head(top_n)

# CorpusR
file_path_corpusr = '/content/contalocCORPUSR.csv'
data_corpusr = pd.read_csv(file_path_corpusr, sep=';')

replace_names_corpusr = {
    "Universidade de o Minho": "Universidade do Minho",
    "UMinho": "Universidade do Minho",
    "em Portugal": "Portugal"
}

exclude_names_corpusr = [
    "Universidade", "universidade", "AAUMinho", "Universidades", "FADU", "SASUM",
    "Governo", "Escola", "Ensino Superior", "Desporto", "RGA"
]

data_corpusr['LOC'] = data_corpusr['LOC'].replace(replace_names_corpusr)
data_corpusr = data_corpusr[~data_corpusr['LOC'].isin(exclude_names_corpusr)]

grouped_data_corpusr = data_corpusr.groupby('LOC')['Oco'].sum().reset_index()

grouped_data_corpusr = grouped_data_corpusr.sort_values(by='Oco', ascending=False).head(top_n)

# Criação dos Gráficos ao lado um do outro
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# Gráfico Nós
axs[0].bar(grouped_data_nos['LOC'], grouped_data_nos['Oco'], color='skyblue')
axs[0].set_xlabel('Local')
axs[0].set_ylabel('Número de Ocorrências')
axs[0].set_title(f'Top {top_n} Ocorrências de Locais no Jornal Nós')
axs[0].set_xticklabels(grouped_data_nos['LOC'], rotation=90)

# Gráfico CorpusR
axs[1].bar(grouped_data_corpusr['LOC'], grouped_data_corpusr['Oco'], color='blue')
axs[1].set_xlabel('Local')
axs[1].set_ylabel('Número de Ocorrências')
axs[1].set_title(f'Top {top_n} Ocorrências de Locais no CorpusR')
axs[1].set_xticklabels(grouped_data_corpusr['LOC'], rotation=90)

plt.tight_layout()
plt.show()