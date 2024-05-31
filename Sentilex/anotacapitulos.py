import re


def le_livro(nome_livro):
    with open (nome_livro, encoding="utf-8") as arquivo_livro:
        livro=arquivo_livro.read()#Carrega o conteúdo completo do livro para a variável livro
    return livro.split('#')#Quebra o conteúdo o livro por "#", utilizado para sinalizar um novo capítulo

def analisa_capitulos(capitulos):
        
    dicionario=carrega_lexico()
        
    for n,capitulo in enumerate(capitulos):
        positivas=0
        negativas=0
        
        print("-"*50)
        for word in dicionario:
            quantidade=len(re.findall(word,capitulo))
            if dicionario[word]>0:
                positivas+=quantidade
            else:
                negativas+=quantidade
        print(f"Capitulo {n}: Positivas: {positivas} - Negativas: {negativas}")
            #print(f"{word} ({dicionario[word]}): {quantidade}")
            
            
def carrega_lexico():
    with open("positivos.txt", encoding="utf-8") as learquivo:
        positivos=learquivo.read().splitlines()
    with open("negativos.txt", encoding="utf-8") as learquivo:
        negativos=learquivo.read().splitlines()
            
    dicionario_lexico={x:1 for x in positivos} | {x:-1 for x in negativos}#Forma um dicionario lexico com as palavras dos arquivos positivos e negativos
        
    return(dicionario_lexico)


#capitulos=le_livro("HP.txt")
#print(len(capitulos))
#analisa_capitulos(capitulos)       

def anota (m):#devolve a palavra com a anotação, ou então só a palavra caso não esteja no dici
    palavra = m[0] #O 0 é a string inteira que foi apanhada, 1 é o 1º grupo de captura
    if palavra in dicionario:
        return f'[{palavra}]({dicionario[palavra]})'  
    else:
       return palavra

def anotaTexto(texto):
    with open("HP.txt", encoding="utf-8") as arquivo:
        texto = arquivo.read()
    anotado = re.sub(r'\w+', anota, texto)
    
    with open("HPanotado.txt", "w", encoding="utf-8") as arquivo_anotado:
        arquivo_anotado.write(anotado)
    
    print("Annotated text written to HPanotado.txt")
    print(anotado)
    print(anotado.count("(1)"))
    print(anotado.count("(-1)"))

dicionario=carrega_lexico()
#print(anota("jogo"))
#print(anota("linda"))
anotaTexto ("HP.txt")

            