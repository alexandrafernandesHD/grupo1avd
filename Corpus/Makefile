titulos.txt:
	python extrai-tit.py

# Extração do corpus
corpus-umsombraR.txt: extrai-body.py
	python extrai-body.py

corpus-nos.txt: extrai-body-nos.py
	python extrai-body.py

# Anotar usando spacy
corpusR-anotado.txt: corpus-umsombraR.txt anotaR.py
	python anotaR.py corpus-umsombraR.txt

# Anotar Nos usando spacy
corpus-nos-anotado.txt: corpus-nos.txt anota-nos.py
	python anota-nos.py corpus-nos.txt

#Calcular Nomes de Pessoa 
contaperCORPUSR.csv: corpusR-anotado.txt contaperCORPUSR.py
	python contaperCORPUSR.py corpusR-anotado.txt

contaperNOS.csv: corpus-nos-anotado.txt contaperNOS.py
	python contaperNOS.py corpus-nos-anotado.txt

#Calcular Locais

contalocCORPUSR.csv: corpusR-anotado.txt contalocCORPUSR.py
	python contalocCORPUSR.py corpusR-anotado.txt

contalocNOS.csv: corpus-nos-anotado.txt contalocNOS.py
	python contalocNOS.py corpus-nos-anotado.txt

#Calcular Organizações

contaorgCORPUSR.csv: corpusR-anotado.txt contaorgCORPUSR.py
	python contaorgCORPUSR.py corpusR-anotado.txt

contaorgNOS.csv: corpus-nos-anotado.txt contaorgNOS.py
	python contaorgNOS.py corpus-nos-anotado.txt

# Calc. freq. verbos nosso corpus
verbosCORPUSR.csv: corpusR-anotado.txt contaverbosCORPUSR.py
	python contaverbosCORPUSR.py corpusR-anotado.txt

verbosNOS.csv: corpus-nos-anotado.txt contaverbosNOS.py
	python contaverbosNOS.py corpus-nos-anotado.txt

# Datas

datasCORPUSR.txt: corpusR-anotado.txt datasCORPUS.py
	python datasCORPUS.py corpusR-anotado.txt

datasNOS.txt: corpus-nos-anotado.txt datasNOS.py
	python datasNOS.py corpus-nos-anotado.txt




