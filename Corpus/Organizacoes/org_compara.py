import pandas as pd
import matplotlib.pyplot as plt

# Graphic 1 - Jornal Nós
file_path_nosv = '/content/contaorgNOSV.csv'
data_nosv = pd.read_csv(file_path_nosv, sep=';')

# Substituição
replace_names_nosv = {
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

exclude_names_nosv = ["25 de abril", "Ciências de o Comunicação", "Relações Internacionais"]

data_nosv['ORG'] = data_nosv['ORG'].replace(replace_names_nosv)
data_nosv = data_nosv[~data_nosv['ORG'].isin(exclude_names_nosv)]

# Soma das ocorrências dos nomes iguais
grouped_data_nosv = data_nosv.groupby('ORG')['Oco'].sum().reset_index()

top_n = 15
grouped_data_nosv = grouped_data_nosv.sort_values(by='Oco', ascending=False).head(top_n)

# Graphic 2 - CorpusR
file_path_corpusr = '/content/contaorgCORPUSRV.csv'
data_corpusr = pd.read_csv(file_path_corpusr, sep=';')

# Substituição
replace_names_corpusr = {
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

exclude_names_corpusr = ["serviço", "Licenciatura", "Tuna", "Departamento"]

data_corpusr['ORG'] = data_corpusr['ORG'].replace(replace_names_corpusr)
data_corpusr = data_corpusr[~data_corpusr['ORG'].isin(exclude_names_corpusr)]

# Soma das ocorrências dos nomes iguais
grouped_data_corpusr = data_corpusr.groupby('ORG')['Oco'].sum().reset_index()

grouped_data_corpusr = grouped_data_corpusr.sort_values(by='Oco', ascending=False).head(top_n)

# Criação dos Gráficos lado a lado
fig, axs = plt.subplots(1, 2, figsize=(20, 8))

# Gráfico Jornal Nós
axs[0].bar(grouped_data_nosv['ORG'], grouped_data_nosv['Oco'], color='skyblue')
axs[0].set_xlabel('Organização')
axs[0].set_ylabel('Número de Ocorrências')
axs[0].set_title(f'Top {top_n} Ocorrências de Organizações no Jornal Nós')
axs[0].set_xticklabels(grouped_data_nosv['ORG'], rotation=90)

# Gráfico CorpusR
axs[1].bar(grouped_data_corpusr['ORG'], grouped_data_corpusr['Oco'], color='darkblue')
axs[1].set_xlabel('Organização')
axs[1].set_ylabel('Número de Ocorrências')
axs[1].set_title(f'Top {top_n} Ocorrências de Organizações no CorpusR')
axs[1].set_xticklabels(grouped_data_corpusr['ORG'], rotation=90)

plt.tight_layout()
plt.show()