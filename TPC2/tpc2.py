# TPC2 - UC de Processamento de linguagens
# simaobarroso

import sys

# variavel global para definir se soma ou nao
modo = 1 # 1 - on 0 - off
resultado = 0



# none conta como on 
# proffessor conta como off
def checkOnOff(string): #verifica se a string tem um on off e =
    res = -1
    fase = 0
    for char in string:
        if char == 'o' or char == 'O':
            fase = 1
        if (char == 'n' or char == 'N') and fase ==1:
            res = 1
        elif (char == 'f' or char == 'F') and fase == 1:
            fase = 2
        elif (char == 'f' or char == 'F') and fase == 2:
            res = 0 
    return res            

# eficiencia nao, mas leitura facilitada
def trataString(a):
    global modo
    global resultado
    r = checkOnOff(a)
    if r==1:
        modo = 1
    elif (r==0) : 
        modo = 0
    str = "0"
    i = 0
    tam = len(a)    
    for c in a:
        if c.isdigit() and modo != 0 :
            str += c    
        elif c != '=' and c.isdigit() == False and modo != 0:
            resultado += int(str)
            str = "0"
        if c=='=': 
            resultado += int(str)
            str = "0"
            print(resultado)
        i+=1
        if i == tam and modo != 0: resultado+=int(str) # ineficiente? sim


# Notas:
# Como apenas contam sequencias de digitos para somar ignora-se o - nos numeros negativos
# ou seja  -55 fica 55
# isto e` facilmente resolvido com (mais uma) condicao na funcao acima.
# uma vez que a func int do python tambem passa numeros negativos dai era so verficar que se fosse - adicionava-se a string str


def exec1():
    f = open("text.txt")
    for line in f:
        elem = line.split(" ")
        for a in elem:
            trataString(a)

def exec2(): 
    global resultado
    print("Coloque aqui os dados:")
    while (True):
        dados  = input()
        elem = dados.split(" ")
        for a in elem:
            trataString(a)




def main():
    m = input("Quer ler do ficheiro text.txt (1) ou do terminal (2) : ")    
    if m == '1' : exec1()
    else : exec2()

if __name__=='__main__':
    main()