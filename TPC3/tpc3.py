# TPC3: Processador de Pessoas listadas nos Róis de Confessados
# simaobarroso

import time # para debug
import re # usar regular expressions
# regex101 para validar




def trata(array):
    res = dict()
    print(array)

    if len(array) != 7 :
        """
        dict['pasta'] = array[0]
        dict['data'] = array[1]
        dict['nome'] = array[2]
        dict['pai'] = array[3]
        dict['mae'] = array[4]
        dict['observacoes'] = array[5]
        """
    return res


# Fazer uma lista de dicionarios ou um dicionarios de dicionarios ?
# Por enquanto lista de dicionarios
# ver ipynb (jupiter notebook) 

def main():
    print("Processing processos.txt ...")
    data = list()
    f = open('processos.txt')
    for line in f:
        campos = line.split("::")
        data += trata(campos)
        #print(campos)
        #time.sleep(5)
    print(data)    



if __name__=='__main__':
    main()


"""
Os valores das colunas correspondem a:
Pasta | Data | Nome | Pai | Mãe | Observações

Um dicionario para cada linha com aqueles parametros
"""
