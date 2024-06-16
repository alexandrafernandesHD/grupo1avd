from bs4 import BeautifulSoup as bs
from jjcli import *
import yaml
import re

ats = glob("1067-1073/Article.aspx*")  # Função glob para obter uma lista de arquivos que têm nomes a começar por "Article.aspx" 
print(ats)

output_data = []

for at in ats:
    with open(at, 'r', encoding="utf-8") as f:
        html = f.read()
        a = bs(html, features="html.parser")

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

        # Construir o dicionário de dados para este artigo
        article_data = {
            "-Título": title,
            "URL": url,
            "Site": site_name,
            "Imagem": image,
            "Data": date,
            "Autor": author,
            "Sobre": description
            
        }

        output_data.append(article_data)

# Escrever os dados em formato YAML
with open("1088-1094.yaml", "w", encoding="utf-8") as file:
    yaml.dump(output_data, file, default_flow_style=False, allow_unicode=True) 