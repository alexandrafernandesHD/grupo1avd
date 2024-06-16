from jjcli import * 
from bs4 import BeautifulSoup as bs


ats = glob("nos_1067_1073/Article.aspx*")
print(ats)

fo = open ("saida1.txt", 'w', encoding="UTF-8")

def proc_article (html):
    print(len(html))
    a = bs(html)
    cabecalho = ""
    for meta in a.find_all("meta"):
        p = meta.get("property")
        if p is None:
            continue
        p = p.replace("og:", "")
        cabecalho += f"{p}:{meta.get('content')}\n"
        #print(p,":", meta.get("content"))
    art =  a.find("div", id="artigo")
    print("==========\n", cabecalho, art.get_text(), file = fo ) #get_text() invoca a função se não pusermos () ficamos com as tags


for file in ats:
    with open(file, encoding="UTF-8") as f: 
        html = f.read()
        proc_article(html)





