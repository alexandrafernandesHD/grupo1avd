import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/contaorgCORPUSRV.csv'
data = pd.read_csv(file_path, sep=';')

# Substituição
replace_names = {
    "Fundação para Ciência e Tecnologia": "FCT",
    "Universidade?": "UMinho",
    "Academia?": "UMinho",
    "Universidade de o Minho": "UMinho",
    "Uminho-": "UMinho",
    "Academia": "UMinho",
    "Academia Minhota": "UMinho",
    "European University Sports Associety": "EUSA",
    "Gabinete de Sistemas de Informação": "GSI",
    "Gabinete de Sistemas de Informação de o Universidade de o Minho": "GSI",
    "Gabinete de Sistemas de Informação de o UMinho": "GSI",
    "Serviços de Ação Social": "SASUM",
    "SAS": "SASUM",
    "Serviços de Acção Social": "SASUM",
    "Serviços de Acção Social?": "SASUM",
    "Serviços de Acção Social de o UM": "SASUM",
    "Serviços de Ação Social de o Academia Minhota": "SASUM",
    "Serviços de Ação Social de o Universidade de o Minho": "SASUM",
    "Serviços de Acção Social de o Universidade de o Minho": "SASUM",
    "Bomboémia?": "Bomboémia",
    "Conselho Cultural de o Universidade de o Minho": "Conselho Cultural",
    "Conselho Cultural de o UMinho": "Conselho Cultural",
    "Conselho Cultural?": "Conselho Cultural",
    "conselho Cultural": "Conselho Cultural",
    "Rádio Universitária": "RUM",
    "Rádio Universitária de o Minho": "RUM",
    "Tuna Universitária de o Minho": "TUM",
    "Departamento Administrativo e Financeiro": "DAF",
    "Departamento Administrativo e financeiro de o SASUM": "DAF",
    "Conselho Geral": "CG",
    "Conselho Geral de o Universidade": "CG",
    "conselho geral": "CG",
    "Conselho Geral de o UM": "CG",
    "Conselho Geral?": "CG",
    "o Conselho Geral": "CG",
    "Departamento Alimentar de o Serviços de Acção Social de o Universidade de o Minho": "Departamento Alimentar",
    "departamento Alimentar": "Departamento Alimentar",
    "Departamento Alimentar de o Serviços de Acção Social de o UMinho": "Departamento Alimentar",
    "Conselho Fiscal e Jurisdicional de o AAUMinho": "CFJ",
    "Conselho Fiscal e Jurisdicional": "CFJ",
    "Associação Académica da Universidade do Minho": "AAUM",
    "Associação académica de o Universidade de o Minho": "AAUM",
    "Associação Académica de o Universidade de o Minho": "AAUM",
    "associação Académica": "AAUM",
    "associação académica de o Universidade de o Minho": "AAUM",
    "Associação Académica?": "AAUM",
    "Associação Académica": "AAUM",
    "associação académica de o UMinho": "AAUM",
    "Associação Académica de o UMinho": "AAUM",
    "UMinho?" : "UMinho"
}

exclude_names = [
    "serviço",
    "Licenciatura",
    "Tuna",
    "Departamento"
]

data['ORG'] = data['ORG'].replace(replace_names)
data = data[~data['ORG'].isin(exclude_names)]

# Soma das ocorrências dos nomes iguais
grouped_data = data.groupby('ORG')['Oco'].sum().reset_index()

top_n = 15
grouped_data = grouped_data.sort_values(by='Oco', ascending=False).head(top_n)

# Criação do Gráfico
plt.figure(figsize=(10, 6))
plt.bar(grouped_data['ORG'], grouped_data['Oco'], color='darkblue')
plt.xlabel('Organização')
plt.ylabel('Número de Ocorrências')
plt.title(f'Top {top_n} Ocorrências de Organizações no CorpusR')
plt.xticks(rotation=90)
plt.show()