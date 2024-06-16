from jjcli import *
import re
from bs4 import BeautifulSoup as bs


ats = glob("1146-1149/Article.aspx*")  # Função glob para obter uma lista de arquivos que têm nomes que começam com "Article.aspx" no diretório "ext"
print(ats)

titles_dict = {}


def proc_article(html, output_file):
    # Processa um ficheiro Article.aspx@id=\d\d\d\d do jornal NOSuminho
    a = bs(html, features="html.parser")
    cabecalho = ""
    divisao = "---"

    # Extração dos dados do cabeçalho
    title = a.find("meta", property="og:title").get("content")
    url = a.find("meta", property="og:url").get("content")
    image = a.find("meta", property="og:image").get("content")
    site_name = a.find("meta", property="og:site_name").get("content")
    description = a.find("meta", property="og:description").get("content")
    type = a.find("meta", property="og:type").get("content")
    if type == "blog":
        type = "article"

    info_span = a.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo")
    date = ""
    author = ""
    if info_span:
        match = re.search(r'(\d{2}-\d{2}-\d{4}) \| (.+)', info_span.text)
        if match:
            date = match.group(1).strip()
            author = match.group(2).strip()

    # Dicionário com os títulos
    titles_dict[output_file] = title

    # Construir o cabeçalho
    cabecalho += f"date: {date}\n"
    cabecalho += f"author: {author}\n"
    cabecalho += f"image: {image}\n"
    cabecalho += f"title: {title}\n"
    cabecalho += f"url: {url}\n"
    cabecalho += f"site name: {site_name}\n"
    cabecalho += f"description: {description}\n"
    cabecalho += f"type: {type}\n"
    
    

    art = a.find("div", id="artigo")
    corpo = proc_art_contents(art)

    if date in corpo and author in corpo:
        corpo = corpo.replace(date, "").replace(author, "")

    conteudo = f"---\n{cabecalho}\n{divisao}\n# {title}\n{corpo}"
    conteudo = conteudo.replace("                        ", "")
    conteudo = conteudo.replace("				", "")
    conteudo = conteudo.replace("|", "")
    conteudo = conteudo.replace("	", "")

    with open(output_file, "w", encoding="utf-8") as fo:
        fo.write(conteudo)


def proc_art_contents(art):
    for tag in art.find_all("div", class_="voltar"): 
        tag.extract()
    for tag in art.find_all("div", id="slidesjs-log"): 
        tag.decompose()
    for tag in art.find_all("ul", class_="socialcount"): 
        tag.decompose()
    for tag in art.find_all("div", id="slides"):
        tag.extract()

    for tag in art.find_all("strong"):  
      
        if tag.parent.name != 'a' and not tag.find_parents('a'):
            tag.replace_with("**" + tag.text + "** ")  # sub. ** , deixa o texto, sub.**

    for tag in art.find_all(["h1", "span"], id="ctl00_ContentPlaceHolder1_LabelTitle"):
        tag.decompose()  # Elimina TAG

    finalt = art.get_text()
    finalt = re.sub(r'\n{3,}', r'\n\n', finalt)

    return finalt


for file in ats:
    with open(file, "r", encoding="utf-8") as f:
        htmlf = f.read()
        art = bs(htmlf, 'html.parser')
        proc_art_contents(art)

for file in ats:
    with open(file, "r", encoding="utf-8") as f:
        htmlf = f.read()  # lê o ficheiro
        print("A processar:", file)
        art = bs(htmlf, 'html.parser')  # cria objeto de BeautifulSoup
        article_id_match = re.search(r'id=(\d+)', file)  # Expressão regular para encontrar o ID
        if article_id_match:
            article_id = article_id_match.group(1)  # Extrai i ID
            output_file = f"output_{article_id}.md"  # Título do ficheiro
            print("Output file:", output_file)  # Imprime o ficheiro
            proc_article(htmlf, output_file)
        else:
            print("O ID não foi encontrado no artigo:", file)

