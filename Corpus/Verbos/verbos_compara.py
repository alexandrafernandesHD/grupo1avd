import pandas as pd
import matplotlib.pyplot as plt

# Jornal Nós - Verbos
file_path_nos = '/content/verbosNOS.csv'
data_nos = pd.read_csv(file_path_nos, sep=';')

# Verbos a excluir
exclude_verbs_nos = ["ter", "dizer", "fazer", "haver", "ir", "dar", "ser", "vir", "estar"]

# Exclui os verbos
filtered_verbs_nos = data_nos[~data_nos['VERBOS'].isin(exclude_verbs_nos)]

grouped_verbs_nos = filtered_verbs_nos.groupby('VERBOS')['Oco'].sum().reset_index()

top_n_verbs = 20
grouped_verbs_nos = grouped_verbs_nos.sort_values(by='Oco', ascending=False).head(top_n_verbs)

# CorpusR - Verbos
file_path_corpusr = '/content/verbosCORPUSR.csv'
data_corpusr = pd.read_csv(file_path_corpusr, sep=';')

# Verbos a excluir
exclude_verbs_corpusr = ["ter", "dizer", "fazer", "haver", "ir", "dar", "ser", "vir", "estar"]

# Exclui os verbos
filtered_verbs_corpusr = data_corpusr[~data_corpusr['VERBOS'].isin(exclude_verbs_corpusr)]

grouped_verbs_corpusr = filtered_verbs_corpusr.groupby('VERBOS')['Oco'].sum().reset_index()

grouped_verbs_corpusr = grouped_verbs_corpusr.sort_values(by='Oco', ascending=False).head(top_n_verbs)

# Criação dos Gráficos ao lado um do outro
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# Gráfico Nós - Verbos
axs[0].bar(grouped_verbs_nos['VERBOS'], grouped_verbs_nos['Oco'], color='yellowgreen')
axs[0].set_xlabel('Verbo')
axs[0].set_ylabel('Número de Ocorrências')
axs[0].set_title(f'Top {top_n_verbs} Ocorrências de Verbos no Jornal Nós')
axs[0].set_xticklabels(grouped_verbs_nos['VERBOS'], rotation=90)

# Gráfico CorpusR - Verbos
axs[1].bar(grouped_verbs_corpusr['VERBOS'], grouped_verbs_corpusr['Oco'], color='darkgreen')
axs[1].set_xlabel('Verbo')
axs[1].set_ylabel('Número de Ocorrências')
axs[1].set_title(f'Top {top_n_verbs} Ocorrências de Verbos no CorpusR')
axs[1].set_xticklabels(grouped_verbs_corpusr['VERBOS'], rotation=90)

plt.tight_layout()
plt.show()