import csv

#input = 'contaorgNOS.csv'
#output = 'contaorgNOSV.csv'

input = 'contaorgCORPUSR.csv'
output = 'contaorgCORPUSRV.csv'

virgula = ','
separador = '='

# Ler o CSV
with open(input, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile, delimiter=virgula)
    rows = list(reader)

# Cria novo CSV
with open(output, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile, delimiter=separador)
    writer.writerows(rows)

print(f"Ficheiro convertido -> {output}")