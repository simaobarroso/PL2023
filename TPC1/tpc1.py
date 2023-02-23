# tpc1 - Feito por Simao Barroso
#fazer com dicionario dentro de dicionarios

# Modelo pensado : dicionario de arrays: {id,[idade,...,temdoenca],etc}

f = open("myheart.csv")


"""
Explicar escolha das estruturas no readME.md

fazer try except para possiveis erros de leitura e possiveis erros de verificacao

melhorar codigo

whats + discord

ignorar valores baixos colestrol
 
"""

def trata(line,id):
    campos = line.split(',')
    if len(campos) != 6 : return null
    idade = int(campos[0])
    sexo = campos[1]
    tensao = int(campos[2])
    colestrol=int(campos[3]) # Pensar em potenciais erros do colestrol (por exemplo colestrol a 0)!!!!!!!!!
    batimento = int(campos[4])
    temDoenca = int(campos[5])
    auxdict = [idade,sexo,tensao,colestrol,batimento,temDoenca]
    return auxdict


dados = dict()

id = 0

# rever este codigo (otimizar + por isto em funcoes)
for line in f:
    if id == 0: pass # eliminei a primeira linha, mas melhorar isto !!
    # VER COM A CENA DA FUNCAO encontraMinMax
    else : dados[id]=trata(line,id)
    id=id+1


#print(dados)




#vai encontrar o min e max de determinada categoria
def encontraMinMax(indice,dados):
    min = dados[1][indice]
    max = dados[1][indice] 
    for ids in dados.keys():
        if dados[ids][indice] < min : min = dados[ids][indice]
        elif dados[ids][indice] > max : max = dados[ids][indice]
    if (min < 1 or max > 199) and indice == 0: print("Valor invalido de idades") # debugs
    return min,max


# vai servir para as distribuicoes por escaloes e de colestrol
# dicionario e` o dicionario a receber,
#
#
# valor e` o 
def geradicionario(dicionario,min,max,intervalo):
    atual = min
    if min % intervalo != 0 : atual -= (min % intervalo)
    while (atual < max):
        dicionario.update({'['+str(atual) + '-' + str(atual + intervalo-1) + ']':0})
        atual += intervalo
    return dicionario


# coloca a distribuicao da doenca por sexo num dicionario onde a key e` o sexo e o value e` a quantidade de pessoas daquele sexo que tem a doenca
def distSexo(dados):
    res = {'M': 0,'F' : 0} #cria-se ja com sexo masculino e feminino porque em principio devem ser os em maioria
    for ids in dados.keys():
        if dados[ids][5] == 1: #so nos interessam os casos com doenca
            if dados[ids][1] == 'M' : res['M'] += 1
            elif dados[ids][1] == 'F': res['F'] += 1
            else: #casos restantes
                if dados[ids][1] in res.keys(): res[dados[ids][1]] +=1 #se estiver nas keys adiciona-se
                else :  res.update({dados[ids][1] : 1}) #caso contrario cria-se    
    return res






def distIdade(dados):
    min,max = encontraMinMax(0,dados)
    res = geradicionario(dict(),min,max,5) # o exercicio pede escaloes do 30 para cima, dai o minimo tomar valor de 30
    # no entanto funciona para qualquer valor que se ponha de min
    for ids in dados.keys():
        if dados[ids][5] == 1: 
            idade = dados[ids][0]
            if idade % 5 != 0 : idade -= idade % 5
            key = '['+str(idade) + '-' + str(idade + 4) + ']'
            res[key] +=1

    return res        


#print(distIdade(dados))


def distNiveisColestrol(dados):
    min,max = encontraMinMax(3,dados)
    res = geradicionario(dict(),min,max,10)
    var = 0
    for ids in dados.keys():
        if dados[ids][5] == 1: 
            colestrol = dados[ids][3]
            if colestrol % 10 != 0 : colestrol -= colestrol % 10
            key = '['+str(colestrol) + '-' + str(colestrol + 9) + ']'
            res[key] +=1

    return res        

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



def main():
    print("-----------------------------")
    print("|   Distribuição Por Sexo   |")
    print("-----------------------------")
    printTable(distSexo(dados))

    print()
    print("-----------------------------")
    print("|  Distribuição Por Idade   |")
    print("-----------------------------")
    printTable(distIdade(dados))

    print()
    print("-----------------------------")
    print("|Distribuição Por Colesterol|")
    print("-----------------------------")
    printTable(distNiveisColestrol(dados))



if __name__=="__main__":
    main()
