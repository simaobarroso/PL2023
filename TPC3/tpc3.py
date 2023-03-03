# TPC3: Processador de Pessoas listadas nos Róis de Confessados
# simaobarroso

import time # para debug
import re # usar regular expressions
# regex101 para validar



def exec1(dados):
    res = dict()
    regex = r"\d+"
    for elem in dados:
        data = elem['data']
        #print(re.match(regex,data).group()) # ver ipynb aula teorica
        data = re.match(regex,data).group()
        #print(data)
        if data in res.keys():
            res[data] += 1
        else :
            res[data] = 1
    return dict(sorted(res.items())) # nao era mais eficiente ir colocando organizado `a medida que vamos por no dicionario






def trata(array):
    res = dict()
    res['pasta'] = array[0] # pasta/processo
    res['data'] = array[1]
    res['nome'] = array[2]
    res['pai'] = array[3]
    res['mae'] = array[4]
    res['observacoes'] = array[5]    
    return res

# REUTILIZADA DO TPC1
# a funcao que imprime a tabela dando um dicionario
def printTable(distribuicao):
    for key in distribuicao:
        print("-----------------------------")
        string = '|' # barra do lado esquerdo
        comp = int((13-len(key))/2) # quantos espacos podemos por de modo a key ficar centralizado
        for i in range(comp):
            string += ' '
        string += key # adicionamos a key
        for i in range(comp):
            string += ' '
        string += "|" # colocar barro do meio (separacao entre a key e o valor do dict)
        comp = 13-len(str(distribuicao[key])) # o mesmo do de cima, mas para o valor da key
        if comp % 2 != 0: 
            comp = int(comp/2)
            comp1 = comp+1
        else:
            comp = int(comp/2)
            comp1 = comp
        for i in range(comp):
            string += ' '
        string += str(distribuicao[key])
        for i in range(comp1):
            string += ' '
        print(string+"|") # barra do lado direito
    print("-----------------------------")


# Fazer uma lista de dicionarios ou um dicionarios de dicionarios ?
# Por enquanto lista de dicionarios
# ver ipynb (jupiter notebook) 

def main():
    #print("Processing processos.txt ...")
    dados = list()
    f = open('processos.txt')
    for line in f:
        campos = line.split("::")
        if (len(campos)) == 7:
            dados += [trata(campos)]
    #print(dados[63])
    alinea = input("Alinea do exercicio : ") 
    if alinea == "ap":
        print("-----------------------------")
        print("|     Processos por ano     |")
        print("-----------------------------")
        printTable(exec1(dados))
    elif alinea == "as":
        print(exec1(dados))    



if __name__=='__main__':
    main()


"""
Os valores das colunas correspondem a:
Pasta | Data | Nome | Pai | Mãe | Observações

Um dicionario para cada linha com aqueles parametros
"""
