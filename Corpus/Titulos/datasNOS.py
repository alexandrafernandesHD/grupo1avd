#!/usr/bin/env python3

from jjcli import * 
import yaml
import re

# Obter todos os arquivos markdown no diretório "Nos"
docs = glob("Nos/*.md")
print(f"Nos: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs)

# Abrir o arquivo de saída para escrita
try:
    err = open("datasNOS.txt", 'w', encoding="UTF-8")
except IOError as e:
    print(f"Erro ao abrir o arquivo datasNOS.txt: {e}")
    exit(1)

# Processar cada arquivo de texto
for txt in cl.text():
    # Capturar metadados
    for metadados in re.findall(r'---(.*)---', txt, flags=re.S):
        dicmeta = yaml.safe_load(metadados)
        if dicmeta is None:
            err.write(f'ERRO no arquivo {cl.filename()}\n')
        else:
            date = dicmeta.get('date')
            title = dicmeta.get('title')
            filename = cl.filename()
            # Escrever no arquivo de saída
            err.write(f"{date}::{title}::{filename}\n")

err.close()
print("Processamento concluído.")