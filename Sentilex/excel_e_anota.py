import re
import pandas as pd


def le_livro(nome_livro):
    with open (nome_livro, encoding="utf-8") as arquivo_livro:
        livro=arquivo_livro.read()#Carrega o conteúdo completo do livro para a variável livro
    return livro.split('#')#Quebra o conteúdo o livro por "#", utilizado para sinalizar um novo capítulo

def analisa_capitulos(capitulos):
        
    dicionario=carrega_lexico()
    dados = [] # os dados ficam neste dicionário
        
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

        total_palavras = len(capitulo.split()) #len de cada capítulo
        dados.append([n, positivas, negativas, total_palavras]) #junta os dados no dicionário

        df = pd.DataFrame(dados, columns=['Capitulo', 'Positivas', 'Negativas', 'Total de Palavras']) #cria um df
        df.to_excel('sentimento_capitulos.xlsx', index=False)  # envia os dados para o Excel o index=False para não enumerar a partir do 0


        print(f"Capitulo {n}: Positivas: {positivas} - Negativas: {negativas}")
            #print(f"{word} ({dicionario[word]}): {quantidade}")


            
def carrega_lexico():
    with open("positivos.txt", encoding="utf-8") as learquivo:
        positivos=learquivo.read().splitlines()
    with open("negativos.txt", encoding="utf-8") as learquivo:
        negativos=learquivo.read().splitlines()
            
    dicionario_lexico={x:1 for x in positivos} | {x:-1 for x in negativos}#Forma um dicionario lexico com as palavras dos arquivos positivos e negativos
        
    return(dicionario_lexico)

#HP_ler = le_livro("HP.txt")
#analisa_capitulos(HP_ler)

#capitulos=le_livro("HP.txt")
#print(len(capitulos))
#analisa_capitulos(capitulos)       

def anota (m):
    palavra = m.group(0) 
    if palavra in dicionario:
        return f'<span style="color:{"green" if dicionario[palavra] == 1 else "red"}">{palavra}</span>'
    else:
        return palavra

def anotaTexto(texto, output_file):
    with open(output_file, 'w', encoding='utf-8') as f_out:
        anotado = re.sub(r'\b\w+\b', anota, texto)  # Use \b for word boundary
        f_out.write(anotado)

        count_1 = anotado.count('<span style="color:green">')
        count_minus_1 = anotado.count('<span style="color:red">')

        # Write counts with HTML formatting to distinguish colors
        counts_html = f"<p>Count (1): <span style='color:green'>{count_1}</span></p>\n"
        counts_html += f"<p>Count (-1): <span style='color:red'>{count_minus_1}</span></p>\n"
        f_out.write(counts_html)

def le_livro(nome_livro):
    with open(nome_livro, encoding="utf-8") as arquivo_livro:
        livro = arquivo_livro.read()
    return livro

def analisa_e_anota(nome_livro, output_file):
    livro = le_livro(nome_livro)
    anotaTexto(livro, output_file)

dicionario = carrega_lexico()
nome_livro = "HP.txt"
output_file = "HP_cores.html"
analisa_e_anota(nome_livro, output_file)


"""   
    def analisa_capitulos_v0(capitulos):
        #Tentativa 3:
        #A mais 'fácil': trabalhar com um arquivo de texto para cada capítulo
        for capitulo in capitulos:
            num_capitulo=capitulo.splitlines()[0].replace(" ","")
            if not num_capitulo.isupper():
                num_capitulo="_INTRO"
            with open (f"HP-Cap_{num_capitulo}.txt", "w", encoding="utf-8") as arquivo_capitulo:
                arquivo_capitulo.write("---\n")
                arquivo_capitulo.write(capitulo)
            
            def busca_palavras(tipo):
                comando = f'rg -o -w -f {tipo}.txt HP-Cap_{num_capitulo}.txt'
                lista=subprocess.run(comando,shell=True, capture_output=True, text=True)
                resultado=(str(lista)).split()
                resultados=((resultado[7].split("'")[1])[:]).split("\\n")
                palavras_capitulo={}
                for resultado in resultados:
                    if resultado!="":
                        if resultado in palavras_capitulo:
                            palavras_capitulo[resultado]+=1
                        else:
                            palavras_capitulo[resultado]=1
                palavras_capitulo=dict(sorted(palavras_capitulo.items(), key=lambda item: item[1], reverse=True))
                with open (f"HP-Cap_{num_capitulo}.txt", "r", encoding="utf-8") as arquivo_capitulo:
                    texto_original=arquivo_capitulo.read()
                    with open (f"HP-Cap_{num_capitulo}.txt", "w", encoding="utf-8") as arquivo_capitulo:
                        arquivo_capitulo.write("---\n")
                        if tipo=="positivos":
                            arquivo_capitulo.write(f"positive:\n")
                        else:
                            arquivo_capitulo.write(f"negative:\n")
                        for palavra, quantidade in palavras_capitulo.items():
                            arquivo_capitulo.write(f"{palavra} - {quantidade}\n")
                        arquivo_capitulo.write(texto_original)

            busca_palavras("negativos")
            busca_palavras("positivos")
"""

