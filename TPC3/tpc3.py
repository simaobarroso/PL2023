# TPC3: Processador de Pessoas listadas nos Róis de Confessados
# simaobarroso

import time # para debug
import re # usar regular expressions
# regex101 para validar


# tambem da para fazer por splits nesta pergunta
# splits por '-'
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

def aux(res,primeiroNome,ultimoNome):

    #print(dict)
    #time.sleep(5)

    #print(res.keys())
    if primeiroNome not in res.keys() and ultimoNome not in res.keys():
        res[primeiroNome] = 1
        res[ultimoNome] = 1
    elif primeiroNome in res.keys() and ultimoNome not in res.keys() : 
        res[primeiroNome] += 1
        res[ultimoNome] = 1
    elif primeiroNome not in res.keys() and ultimoNome in res.keys() : 
        res[ultimoNome] += 1
        res[primeiroNome] = 1
    else:
        res[primeiroNome] += 1
        res[ultimoNome] += 1

    
    
    #print(res)
    #time.sleep(3)
    return res
    #return dict(sorted(res.items()))
  



def exec2(dados):
    # int(data) // 100 +1 # -> e` assim que se calcula o seculo
    # \w+$ # regex ultimo nome
    # ^\w+ # regex primeiro nome
    # (^\w+|\w+$) # regex primeiro e ultimo nome
    # ou fazer split por espacos !!!!
    res = dict()
    for elem in dados :
        data = elem['data']
        data = re.match(r"\d+",data).group()
        seculo = int(data) // 100 + 1
        primeiroNome = re.match(r"^\w+",elem['nome']).group()
        ultimoNome = re.search(r"\w+$",elem['nome']).group()
        if seculo in res.keys():
            res[seculo] = aux(res[seculo],primeiroNome,ultimoNome)
        else:
            res[seculo] = {primeiroNome : 1, ultimoNome : 1}
        #print(res)
        """
        if seculo in res.keys() and primeiroNome in res[seculo].keys() and ultimoNome in res[seculo].keys():
            res[seculo][primeiroNome] += 1
            res[seculo][ultimoNome] += 1
        elif primeiroNome in res[seculo].keys() and ultimoNome  not in res[seculo].keys():
            res[seculo][primeiroNome] += 1
            res[seculo] = {ultimoNome : 1}
        elif primeiroNome not in res[seculo].keys() and ultimoNome in res[seculo].keys():
            res[seculo] = {primeiroNome : 1}
            res[seculo][ultimoNome] += 1
        else : # caso de nao existir primeiro 
            res[seculo] = {primeiroNome : 1}
            res[seculo] = {ultimoNome : 1}
        """
    return dict(sorted(res.items()))


    """
        if data in res.keys():
            res[seculo] += 
        else :
            res[seculo] = 
    return dict(sorted(res.items())) 
    """

def exec3(dados):
    pass 
    # basta usar regex para apanhar tudo depois da virgurla (do campo das observacoes)
    # regex 101 para confirmar 
    # 

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
        string = '|'
        comp = int((13-len(key))/2) 
        for i in range(comp):
            string += ' '
        string += key 
        for i in range(comp):
            string += ' '
        string += "|" 
        comp = 13-len(str(distribuicao[key])) 
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
        print(string+"|") 
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
            # falta validar se esta repetido ou nao os campos !!!
            # usar regex para validar campos (discord)
            dados += [trata(campos)]
    #print(dados[63])
    #print(exec2(dados))
    dass = exec2(dados)
    i = 0

    for elem in dass:
        try:
            i+= dass[elem]['Adao']             
        except: 
            pass    
    print(i)        
    
    """
    alinea = input("Alinea do exercicio : ") 
    if alinea == "ap":
        print("-----------------------------")
        print("|     Processos por ano     |")
        print("-----------------------------")
        printTable(exec1(dados))
    elif alinea == "as":
        print(exec1(dados))    
        """


if __name__=='__main__':
    main()


"""
Os valores das colunas correspondem a:
Pasta | Data | Nome | Pai | Mãe | Observações

Um dicionario para cada linha com aqueles parametros

+

Explicar no read.me

+

Fazer validacao dos dados !!!!

+

githubs

+
re.compile(r'^(?P<pasta>[0-9]+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<pai>[a-zA-Z ]+)?::(?P<mae>[a-zA-Z ,]+)?::(?P<observacoes>.+)[:]+$')


"""
