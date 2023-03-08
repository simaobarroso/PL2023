# TPC4:  Ficheiros CSV com listas e funções de agregação
# simaobarroso

import json
import re

# modificar isto

def exec1(f,out):
    fout = open(out,"w")
    keys = f.readline().strip('\n')
    keys = keys.split(",") # usar regex para isto porque assim nao vai haver diferenca se ficheiro e` , ou ;
    l = len(keys)
    i = 0
    res = list()
    # testar casos de erros !!
    for line in f:
        if i==0: pass # mudar isto para algo mais eficiente : https://stackoverflow.com/questions/46270638/read-a-file-starting-from-the-second-line-in-python
        else :
            linhas = line.split(",") # usar regex para isto ?? sim porque podemos ver se e` , ou ;
            aux = dict()
            aux[keys[0]] = linhas[0]
            aux[keys[1]] = linhas[1]
            aux[keys[2]] = linhas[2].strip('\n')
            res += [aux]
        i+=1    
    json.dump(res,fout)


def main():
    #ficheiro = input("Coloque o ficheiro de csv para por em JSON:")
    ficheiro = "alunos.csv"
    #out = input("nome do ficheiro de destino: ")
    #out = "alunos.json" #isto e` para o exec1
    with open(ficheiro,"r") as f:
        res = exec1(f,out)
        #print(res)



if __name__=="__main__":
    main()