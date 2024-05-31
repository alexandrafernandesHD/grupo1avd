from jjcli import *


for n in range(1074,1081):
    comando= f'wget -r -c -l 2 "http://www.nos.uminho.pt/History.aspx?id={n}"'
    qxsystem (comando)


#for n in range(1,5):
   # comando1= f'wget -r -c -l 2 "https://www.comumonline.com/page/{n}/?s=entrevista"'
   # qxsystem (comando1)



