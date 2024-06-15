import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/contalocNOS.csv'
data = pd.read_csv(file_path, sep=';')

# Substituição
replace_names = {
    "em Portugal": "Portugal",
    "Universidade de o Minho": "Universidade do Minho",
    "UMinho": "Universidade do Minho",
    "Norte": "Norte de Portugal"
}

exclude_names = ["AFUM", "NIG", "Via láctea", "Escola", "Universidade"]

data['LOC'] = data['LOC'].replace(replace_names)
data = data[~data['LOC'].isin(exclude_names)]

# Reitoria
data.loc[(data['LOC'] == "Reitoria"), 'Oco'] = 9

# Soma das ocorrências dos nomes iguais
grouped_data = data.groupby('LOC')['Oco'].sum().reset_index()

top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Criação do Gráfico
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['LOC'], grouped_data['Oco'], color='skyblue')
plt.xlabel('Local')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Locais no Jornal Nós')
plt.xticks(rotation=90)
plt.show()