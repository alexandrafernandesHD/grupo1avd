import pandas as pd
import matplotlib.pyplot as plt


file_path = '/content/verbosCORPUSR.csv'
data = pd.read_csv(file_path, sep=';')

# Verbos a excluir
exclude_verbs = ["ter", "dizer", "fazer", "haver", "ir", "dar", "ser", "vir", "estar"]

# Exclui os verbos
filtered_verbs = data[~data['VERBOS'].isin(exclude_verbs)]

grouped_verbs = filtered_verbs.groupby('VERBOS')['Oco'].sum().reset_index()

top_n_verbs = 20
grouped_verbs = grouped_verbs.sort_values(by='Oco', ascending=False).head(top_n_verbs)

# Criação do Gráfico para VERBOS
plt.figure(figsize=(10, 6))
plt.bar(grouped_verbs['VERBOS'], grouped_verbs['Oco'], color='darkgreen')
plt.xlabel('Verbo')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n_verbs} Ocorrências de Verbos no CorpusR')
plt.xticks(rotation=90)
plt.show()