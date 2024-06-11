#!/usr/bin/env python3

from jjcli import * 
import yaml

docs = glob("Nos/*.md") #um glob que apanha uma lista de ficheiros

# print(f"Nos: {len(docs)}")
cl = clfilter("")
cl.args = sorted(docs) 

output = open ("corpus-nos.txt",'w', encoding="UTF-8")

for txt in cl.text():
    # print(txt[:100])
    for metadados, body in re.findall(r'---(.*)---(.*)', txt, flags=re.S): #o ponto não apanha new lines, por isso o re.S 
        print (f"@{cl.filename()}*\n", body, file=output)

        