#!/usr/bin/env python3

from jjcli import * 
import yaml
import re

# Obter todos os arquivos markdown nos diretórios especificados
docs = glob("MPessoa/*.md") + glob("ComUM/*.md") + glob("UMdicas/*.md") + glob("Entrevistas/*.md")
print(f"Total de documentos: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs)

# Abrir o arquivo de saída para escrita
try:
    err = open("datasCorpusR.txt", 'w', encoding="UTF-8")
except IOError as e:
    print(f"Erro ao abrir o arquivo datasCorpusR.txt: {e}")
    exit(1)

# Processar cada arquivo de texto
for txt in cl.text():
    # Capturar metadados
    for metadados in re.findall(r'---(.*?)---', txt, flags=re.S):
        try:
            # Processar múltiplos documentos YAML
            for dicmeta in yaml.safe_load_all(metadados):
                if isinstance(dicmeta, dict):  # Verificar se dicmeta é um dicionário
                    date = dicmeta.get('date')
                    title = dicmeta.get('title')
                    filename = cl.filename()
                    # Escrever no arquivo de saída
                    err.write(f"{date}::{title}::{filename}\n")
                else:
                    err.write(f'ERRO no arquivo {cl.filename()}: metadados não são um dicionário\n')
        except yaml.YAMLError as e:
            err.write(f'Erro de YAML no arquivo {cl.filename()}: {e}\n')

err.close()
print("Processamento concluído.")