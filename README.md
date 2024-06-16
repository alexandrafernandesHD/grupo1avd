# Grupo 1 Análise e Visualização de Dados

Repositório com os trabalhos finais da disciplina de Análise e Visualização de Dados 

# Repositório do Grupo 1 Projeto Sombra

Trabalho Final de Análise de Visualização de Dados e Projeto Integrado 2

## Análise e Visualização de Dados
## Projeto Integrado 2
### Mestrado em Humanidades Digitais
**Ano Letivo 2023/2024**

**16 de Junho de 2024**

**Grupo 1**
- Francisca Pimenta, PG54508
- S. Alexandra Fernandes, PG52766

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Estrutura do Repositório](#estrutura-do-repositório)
- [Autores](#autores)

## Descrição do Projeto

Neste projeto, desenvolvemos um arquivo com ficheiros relacionados com os 50 anos da Universidade do Minho, usando técnicas de web scraping, análise de documentos e entrevistas. Os dados foram tratados e analisados com ferramentas de processamento de linguagem natural e visualização de dados. Também realizamos um exercício de Análise de Sentimento com o primeiro livro da saga "Harry Potter".

## Estrutura do Repositório

### Corpus/
Esta pasta contém o corpus de textos que foi utilizado para análise. A seguir estão as subpastas e arquivos dentro desta pasta:

- **Datas/**: Scripts e dados relacionados ao tratamento de datas.
- **Locais/**: Scripts e dados para a análise de locais mencionados nos textos.
- **NomesPessoas/**: Scripts e dados relacionados ao tratamento de nomes de pessoas.
- **Organizacoes/**: Scripts e dados para análise de organizações mencionadas.
- **Titulos/**: Scripts e dados sobre títulos de documentos.
- **Verbos/**: Scripts e dados relacionados ao tratamento de verbos nos textos.

#### Arquivos principais:
- **Makefile**: Arquivo para automatizar tarefas recorrentes no projeto.
- **anota-nos.py**: Script para anotação do Jornal Nós.
- **anotaR.py**: Script para anotações do corpus.
- **contagempals.py**: Script para contagem de palavras.
- **contalocCORPUSR.py**: Script para contagem de locais no corpus.
- **contalocNOS.py**: Script para contagem de locais no Jornal Nós.
- **contanomesCORPUSR.py**: Script para contagem de nomes no corpus.
- **contanomesNOS.py**: Script para contagem de nomes no Jornal Nós.
- **contaorgCORPUSR.py**: Script para contagem de organizações no corpus.
- **contaorgNOS.py**: Script para contagem de organizações no Jornal Nós.
- **contaperCORPUSR.py**: Script para contagem de entidades no corpus.
- **contaperNOS.py**: Script para contagem de entidades no Jornal Nós.
- **contaverbosCORPUSR.py**: Script para contagem de verbos no corpus.
- **contaverbosNOS.py**: Script para contagem de verbos no Jornal Nós.
- **corpus-nos-anotado.txt**: Corpus anotado.
- **corpus-nos.txt**: Jornal Nós anotado.
- **corpus-umsombraR.txt**: Arquivo do corpus do projeto Sombra.
- **corpusR-anotado.txt**: Arquivo de corpus anotado com Spacy.
- **extrai-body-nos.py**: Script para extração do corpus do Jornal Nós.
- **extrai-body.py**: Script para extração de corpo de texto do corpus.

### Extracao/
Pasta que inclui scripts e ferramentas para extração de dados.
- **extrair.py**: Script para webscraping

### Sentilex/
Diretório que abriga os recursos para Análise de Sentimento.

- **HP.txt**: Primeiro livro do Harry Potter.
- **HPanotado.txt**: Arquivo de texto anotado com análise de sentimentos do livro Harry Potter.
- **anotacapitulos.py**: Script para anotação dos capítulos.
- **aula_2024-04-12.py**: Script utilizado em aula.
- **capitulo1.txt**: Texto do capítulo 1 para análise.
- **defnegativos_positivos.py**: Script para extração de termos negativos e positivos.
- **excel_e_anota.py**: Script para exportação para excel e anotação.
- **negativos.txt**: Arquivo de texto com termos negativos.
- **positivos.txt**: Arquivo de texto com termos positivos.
- **sentilexjj.txt**: Arquivo de texto com léxico de sentimentos.
- **sentimento_capitulos.xlsx**:  Excel com análise de sentimentos dos capítulos.
- **sentimento_capitulos1904.csv**: Arquivo CSV com análise de sentimentos dos capítulos.
- **sentimento_capitulos1904.xlsx**: Arquivo Excel com análise de sentimentos dos capítulos.
- **sentimento_capitulostpc.csv**: Arquivo CSV com análise de sentimentos dos capítulos.

### Tratamento_Corpus/
Pasta destinada ao tratamento e limpeza dos dados textuais.

#### Subpastas:
- **1tentativa/**: Scripts e arquivos da primeira tentativa de tratamento do corpus.
- **2tentativa/**: Scripts e arquivos da segunda tentativa de tratamento do corpus.
- **3tentativa/**: Scripts e arquivos da terceira tentativa de tratamento do corpus.
- **final/**: Versão final dos scripts e arquivos após o tratamento completo do corpus.

#### Arquivos principais:
- **README.md**: Este arquivo README, que fornece uma visão geral do projeto e instruções sobre como utilizá-lo.

## Autores

- **Francisca Pimenta** - PG54508
- **S. Alexandra Fernandes** - PG52766

---

Este README fornece uma visão geral clara e organizada do projeto, facilitando a compreensão e utilização do repositório por terceiros.
```

Esta versão do README agora inclui uma descrição detalhada das subpastas dentro da pasta `Tratamento_Corpus/`, o que oferece uma visão mais abrangente sobre o tratamento e limpeza dos dados textuais no projeto.
