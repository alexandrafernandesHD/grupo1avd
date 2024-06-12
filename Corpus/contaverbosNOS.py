import spacy 
from jjcli import *
from collections import Counter

cl = clfilter("")
all_verbs = Counter()

for linha in cl.input():
    palavras = linha.split("\t")  #.split()
    if len(palavras) >= 3: 
        if palavras[2] == "VERB":
           lema = palavras[1]
           if lema[-1] != "r":   #encontrar o r
               continue
           # print(palavras[1])
           all_verbs.update([palavras[1]])


#print(all_verbs)
output  = open ("verbosNOS.csv", 'w', encoding="UTF-8")
for verbo, oco in all_verbs.items():
    print(f'{verbo}, {oco}', file = output) 