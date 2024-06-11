#!/usr/bin/env python3

from jjcli import *
import yaml

# Glob apanhar os Arquivos
#docs = glob("ComUM/*.md")
#docs = glob("Nos/*.md")
#docs = glob("UMDICAS/*.md")
#docs = glob("Entrevistas/*.md")
#docs = glob("MPessoa/*.md")
#docs = glob("Nos/*.md") + glob("MPessoa/*.md") + glob("ComUM/*.md") + glob("UMdicas/*.md") + glob("Entrevistas/*.md")
docs = glob("MPessoa/*.md") + glob("ComUM/*.md") + glob("UMdicas/*.md") + glob("Entrevistas/*.md")

# Inicializar o clfilter
cl = clfilter("")
cl.args = sorted(docs)

# Variável para contar o número total de palavras
total_words = 0

# Iterar sobre cada arquivo, ler o conteúdo e contar as palavras
for file_path in docs:
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Ignorar linhas que começam com #
            if not line.strip().startswith('#'):
                total_words += len(line.split())

# Imprimir o número de documentos e o total de palavras
#print(f"ComUM: {len(docs)}, Total de palavras: {total_words}")
#print(f"UMDicas: {len(docs)}, Total de palavras: {total_words}")
#print(f"Nos: {len(docs)}, Total de palavras: {total_words}")
#print(f"Entrevistas: {len(docs)}, Total de palavras: {total_words}")
#print(f"MPessoa {len(docs)}, Total de palavras: {total_words}")
#print(f"Corpus UM Sombra {len(docs)}, Total de palavras: {total_words}")
print(f"CorpusR: {len(docs)}, Total de palavras: {total_words}")

