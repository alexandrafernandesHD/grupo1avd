import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/contaperNOS.csv'
data = pd.read_csv(file_path, sep=';')

# Subs. Nomes
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

# Soma
grouped_data = data.groupby('PER')['Oco'].sum().reset_index()


top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Gráfico
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['PER'], grouped_data['Oco'], color='skyblue')
plt.xlabel('Nome')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Pessoas no Jornal Nós')
plt.xticks(rotation=90)
plt.show()