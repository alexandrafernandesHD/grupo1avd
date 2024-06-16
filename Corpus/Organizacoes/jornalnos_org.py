import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/contaorgNOSV.csv'
data = pd.read_csv(file_path, sep=';')

# Substituição
replace_names = {
    "Accenture": "Accenture",
    "Fundação para a Ciência e Tecnologia": "FCT",
    "Fundação para a Ciência": "FCT",
    "Instituto de Letras e Ciências Humanas": "ILCH",
    "ePsi": "EPsi",
    "Escola de Psicologia": "EPsi",
    "Escola de Psicologia de o UMinho": "EPsi",
    "Escola de psicologia": "EPsi",
    "Centro de Estudos Galegos": "CEG",
    "UMinho?": "UMinho",
    "UMinho*": "UMinho"
}

exclude_names = ["25 de abril", "Ciências de o Comunicação", "Relações Internacionais"]

data['ORG'] = data['ORG'].replace(replace_names)
data = data[~data['ORG'].isin(exclude_names)]


# Soma das ocorrências dos nomes iguais
grouped_data = data.groupby('ORG')['Oco'].sum().reset_index()

top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Criação do Gráfico
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['ORG'], grouped_data['Oco'], color='skyblue')
plt.xlabel('Organização')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Organizações no Jornal Nós')
plt.xticks(rotation=90)
plt.show()