def negativos(ficheiro):
    with open(ficheiro, 'r') as f:
        with open('negativos.txt', 'a') as file:
            for linha in f:
                if "POL:N0=-1" in linha:
                    word = linha.split(",")[0] 
                
                    file.write(word + '\n')


negativos("sentilexjj.txt")

def positivos(ficheiro):
    with open(ficheiro, 'r') as file:
        with open('positivos.txt', 'a') as file1:
            for linha in file:
                if "POL:N0=1" in linha:
                    word = linha.split(",")[0] 
                
                    file.write(word + '\n')



positivos("sentilexjj.txt")