from jjcli import glob
import re
from bs4 import BeautifulSoup as bs


ats = glob("1067-1073/Article.aspx*")
print(ats)

def proc_article(html, output_file):
    # Processa artigo
    a = bs(html, features="html.parser")
    cabecalho = ""
    divisao = "---"

    # Extrair os metadados
    title = a.find("meta", property="og:title").get("content")
    url = a.find("meta", property="og:url").get("content")
    image = a.find("meta", property="og:image").get("content")
    site_name = a.find("meta", property="og:site_name").get("content")
    description = a.find("meta", property="og:description").get("content")

    # Extrair data e autor
    info_span = a.find("span", id="ctl00_ContentPlaceHolder1_LabelInfo")
    date = ""
    author = ""
    if info_span:
        match = re.search(r'(\d{2}-\d{2}-\d{4}) \| (.+)', info_span.text)
        if match:
            date = match.group(1).strip()
            author = match.group(2).strip()

    # Cabeçalho
    cabecalho += f"title: {title}\n"
    cabecalho += f"url: {url}\n"
    cabecalho += f"image: {image}\n"
    cabecalho += f"site name: {site_name}\n"
    cabecalho += f"description: {description}\n"
    cabecalho += f"date: {date}\n"
    cabecalho += f"author: {author}\n"

    art = a.find("div", id="artigo")
    corpo = proc_art_contents(art)

    with open(output_file, "w", encoding="utf-8") as fo:
        print("==========\n", cabecalho, divisao, corpo, file=fo)

def proc_art_contents(art):
    for tag in art.find_all("div", class_="voltar"): tag.extract()
    for tag in art.find_all("div", id="slidesjs-log"): tag.decompose()
    for tag in art.find_all("ul", class_="socialcount"): tag.decompose()
    for tag in art.find_all("div", id="slides"):
        slides = tag.extract()
    for tag in art.find_all("table"):
        tag.insert(0, "\n## TABELA")
    for tag in art.find_all("strong"):  
        tag.replace_with("**" + tag.text + "** ")  # sub. **, texto, sub. **
    for tag in art.find_all("div", class_="title"):
        sem_espacos = tag.get_text().strip()
        tag.replace_with("# " + sem_espacos)
    finalt = art.get_text()
    finalt = re.sub(r'\n{3,}', r'\n\n', finalt)
    return finalt

for file in ats:
    with open(file, "r", encoding="utf-8") as f:
        html = f.read()  # lê o ficheiro
        print("A processar:", file)
        art = bs(html, 'html.parser')  # cria objeto BeautifulSoup 
        article_id_match = re.search(r'id=(\d+)', file)  # expressões regulares para encontrar o ID
        if article_id_match:
            article_id = article_id_match.group(1)  # extrai o ID
            output_file = f"output_{article_id}.md"  # título do output
            print("Output file:", output_file)  # imprime o output
            proc_article(html, output_file)