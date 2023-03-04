# TPC3: Processador de Pessoas listadas nos Róis de Confessados
# simaobarroso

import time # para debug
import re # usar regular expressions
# regex101 para validar
import json # exercicio 4


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

def aux(res,nome):

    #print(dict)
    #time.sleep(5)

    #print(res.keys())


    if nome not in res.keys():
        res[nome] = 1
    else:
        res[nome] += 1

    
    
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
    resPN = dict()
    resUN = dict()
    for elem in dados :
        data = elem['data']
        data = re.match(r"\d+",data).group()
        seculo = (int(data) // 100) + 1
        primeiroNome = re.match(r"^\w+",elem['nome']).group()
        ultimoNome = re.search(r"\w+$",elem['nome']).group()
        if seculo in resPN.keys():
            resPN[seculo] = aux(resPN[seculo],primeiroNome)
        else:
            resPN[seculo] = {primeiroNome : 1} 
        if seculo in resUN.keys():
            resUN[seculo] = aux(resUN[seculo],ultimoNome)
        else:
            resUN[seculo] = {ultimoNome : 1}
    return dict(sorted(resPN.items())),dict(sorted(resUN.items()))


def exec3(dados):
    pass 
    # basta usar regex para apanhar tudo depois da virgurla (do campo das observacoes)
    # regex 101 para confirmar 
    # 

def exec4(dados):
    with open('exe4.json', 'w') as f:
        json.dump(dados, f)
        """
        for data in dados:
            print(data)
            json.dump(data, f)
            f.write("\n")
    #sera que temos de voltar a ler ?/ Porque 20 primeiros dados
    f.close
    """
    # mandar cena de erros try catch return tru ou false, etc

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


def top5(lista):
    list = sorted(lista.items(), key=lambda x: x[1], reverse=True)[:5]
    return dict(list)


# Fazer uma lista de dicionarios ou um dicionarios de dicionarios ?
# Por enquanto lista de dicionarios
# ver ipynb (jupiter notebook) 

def main():
    #print("Processing processos.txt ...")
    dados = list()
    f = open('processos.txt')
    for line in f:
        campos = line.split("::") # podemos usar regex em vez de split
        if (len(campos)) == 7:
            # falta validar se esta repetido ou nao os campos !!!
            # usar regex para validar campos (discord)
            dados += [trata(campos)]
    #print(dados[63])
    #print(exec2(dados))
    primeirosNome,segundosNomes = exec2(dados) # confirmar se da valores certos
    """
    sec = input("Sobre qual seculo quer o top 5 de primeuros nomes :")
    print(int(sec))
    e2 = primeirosNome[int(sec)]
    print(top5(e2))
    e3 = segundosNomes[int(sec)]
    print(top5(e3))

    printTable(top5(e2))
    """
    #exec4(dados[:20])


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
+
validar datasets
+ 
encontrar erros
+ 
ler enunciado

"""
