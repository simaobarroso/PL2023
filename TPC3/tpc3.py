# TPC3: Processador de Pessoas listadas nos Róis de Confessados
# simaobarroso

import time # para debug
import re # usar regular expressions
import json # exercicio 4


def exec1(dados):
    res = dict()
    regex = r"\d+"
    for elem in dados:
        data = elem['data']
        data = re.match(regex,data).group()
        if data in res.keys():
            res[data] += 1
        else :
            res[data] = 1
    return dict(sorted(res.items())) 


def aux(res,nome):
    if nome not in res.keys():
        res[nome] = 1
    else:
        res[nome] += 1
    return res


def exec2(dados):
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
    regex = r"(?<=,)[\w\s]+(?=\. Proc\.)" # aula pratica 2
    res = dict()
    for elem in dados:
        linha = elem['observacoes']
        parentesco = re.findall(regex,linha)
        for es in parentesco:
            if es in res.keys():
                res[es] += 1 
            else:
                res[es] = 1
   
    return res    


def exec4(dados):
    with open('exe4.json', 'w') as f:
        json.dump(dados, f,indent = ' ')


def printTableOLD(distribuicao):
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


def find_largest_key(dictionary):
    largest_key = ""
    for key in dictionary:
        if len(key) > len(largest_key):
            largest_key = key
    return largest_key


def printTable(dicionario,exec):
    colunas = list()
    #if exec == 1 : colunas = ["Ano","Nr processos"]
    if exec == 2 : colunas = ["Nome","Frequencia"]
    else : colunas = ["Relacao","Nr Pessoas"] 
    lentgth = len(find_largest_key(dicionario))
    print("+" + "-"*(15 + lentgth + 2) + "+")
    print("| " + colunas[0] + (lentgth - len(colunas[0]) + 5)* " " + "| " + colunas[1]+ "|")
    print("+" + "-"*(15 + lentgth + 2) + "+")
    for key in dicionario:
        string = "| "
        string += str(key)
        i = len(str(key))
        while(i<lentgth+5):
            string += " "
            i+=1
        string += "| " + str(dicionario[key])
        i = len(str(dicionario[key])) + 5
        while (i < 15):
            string += " "
            i+=1
        print(string+"|") 
    print("+" + "-"*(15 + lentgth + 2) + "+")

def top5(lista):
    list = sorted(lista.items(), key=lambda x: x[1], reverse=True)[:5]
    return dict(list)

def parser():
    
    with open("processos.txt") as file:

        estrutura = re.compile(r'^(?P<pasta>[0-9]+)::(?P<data>\d{4}-\d{2}-\d{2})::(?P<nome>[a-zA-Z ]+)::(?P<pai>[a-zA-Z ]+)?::(?P<mae>[a-zA-Z ,]+)?::(?P<observacoes>.+)[:]+$')
        lista = []
        verificacao = set()

        lines = file.readlines()
        for line in lines:
            x = estrutura.match(line)
            if x:
                chave = (x.group(3), x.group(5)) # se um elemento tiver o mesmo nome e a mesma mae ignora

                if chave not in verificacao:
                    lista.append(x.groupdict())
                    verificacao.add(chave)
    
    return lista


def main():
    dados = list()
    dados = parser()

    #print(len(dados))

    print("TPC 3 : UC de Processamento do linguagens")
    print("1 - Frequência de processos por ano")
    print("2 - Frequência de nomes próprios e apelidos por séculos e apresenta os 5 mais usados")
    print("3 - Frequência dos vários tipos de relação: irmão, sobrinho, etc.")
    print("4 - Primeiros 20 registos escritos num ficheiro em formato json")
    inp = input("Escolha o exercicio: ")
    print("")
    inp = int(inp)
    if inp == 1:
        print("-----------------------------")
        print("|     Processos por ano     |")
        print("-----------------------------")
        printTableOLD(exec1(dados))

    elif inp == 2:
        primeirosNome,segundosNomes = exec2(dados)
        sec = input("Sobre qual seculo quer o top 5 de primeiros nomes e de ultimos nomes: ")
        e2 = primeirosNome[int(sec)]
        printTable(top5(e2),2)
        print("")
        e3 = segundosNomes[int(sec)]
        printTable(top5(e3),2)
        #printTable(exec2(dados))

    elif inp == 3:
        printTable(exec3(dados),3)

    elif inp == 4:
        #print(exec4(dados[:20]))
        print("Ficheiro exe4.json")
        exec4(dados[:20])

    else:
        quit()            

        
if __name__=='__main__':
    main()
