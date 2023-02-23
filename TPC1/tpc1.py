# TPC1: Análise de dados: doença cardíaca



# trata de cada linha do dataset, colocando-a num array 
# se alguma linha do dataset tem valores errados, essa linha é ignorada
def trata(line):
    try:
        campos = line.split(',')
        if len(campos) != 6 : return null
        idade = int(campos[0])
        sexo = campos[1]
        tensao = int(campos[2])
        colestrol=int(campos[3])
        batimento = int(campos[4])
        temDoenca = int(campos[5])
        auxdict = [idade,sexo,tensao,colestrol,batimento,temDoenca]
        return auxdict
    except: # no caso de quando acontece um erro qualquer nos passos anteriores
        print("----------------------\nDataset formato errado\n----------------------") #debug
        return 0   



#vai encontrar o min e max de determinada categoria
def encontraMinMax(indice,dados):
    min = dados[2][indice]
    max = dados[2][indice] 
    for ids in dados.keys():
        if dados[ids][indice] < min : min = dados[ids][indice]
        elif dados[ids][indice] > max : max = dados[ids][indice]
    if (min < 1 or max > 199) and indice == 0: print("Valor invalido de idades") # debugs
    # nao faco mesmo para o colestrol ou outras categorias porque pode nao ter havido leitura, devido por exemplo ha falta de instrumentos
    return min,max


# vai servir para as distribuicoes por escaloes e de colestrol
# dicionario é o dicionario a receber, o qual vai ser populado
# min é o valor minimo daquele intervalo
# max é o valor maximo daquele intervalo
# intervalo é de quanto em quanto se quer que seja o intervalo da distribuicao
# por exemplo para a idade o intervalo é 5, para o colestrol é 10
def geradicionario(dicionario,min,max,intervalo):
    atual = min
    if min % intervalo != 0 : atual -= (min % intervalo) # o intervalo tem de comecar num multiplo de 5
    while (atual < max):
        dicionario.update({'['+str(atual) + '-' + str(atual + intervalo-1) + ']':0})
        atual += intervalo
    return dicionario





# coloca a distribuicao da doenca por sexo num dicionario onde a key é o sexo e o value é a quantidade de pessoas daquele sexo que tem a doenca
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





# distribuicao da doenca por escaloes etarios
def distIdade(dados):
    min,max = encontraMinMax(0,dados) # encontra se a idade maxima e minima
    res = geradicionario(dict(),min,max,5) #apesar do exercicio pedir escaloes dos 30 para a frente, decidi incluir os de tras
    # bastava mudar o min para 30 para ter exatamente como no exercicio
    for ids in dados.keys():
        if dados[ids][5] == 1: 
            idade = dados[ids][0] 
            if idade % 5 != 0 : idade -= idade % 5 # poderia ser feito sem o if, mas if mantem-se por questoes de facilidade de leitura
            key = '['+str(idade) + '-' + str(idade + 4) + ']' # arranjamos a key, para saber onde adicionar
            res[key] +=1

    return res        



# Basicamente o mesmo do que a distribuicao por idades, chamando as mesmas funcoes
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



def main():
    f = open("myheart.csv") # abre-se o csv dado
    dados = dict() 
    id = 1 # cada linha tem um id associado a si
    for line in f:
        if id == 1: pass # ignora-se a primeira linha do csv
        elif trata(line) : dados[id] = trata(line)
        id=id+1

    print("PL : TPC1 - Análise de dados: doença cardíaca\n")
    print("1 - Distribuição Por Sexo")
    print("2 - Distribuição Por Idade")
    print("3 - Distribuição Por Colesterol\n")

    #print(dados) 
    op = input("Insira uma opcao: ")
    if (int(op) == 1):
        print("-----------------------------")
        print("|   Distribuição Por Sexo   |")
        print("-----------------------------")
        printTable(distSexo(dados))
    if (int(op) == 2):
        print()
        print("-----------------------------")
        print("|  Distribuição Por Idade   |")
        print("-----------------------------")
        printTable(distIdade(dados))
    if (int(op) == 3):
        print()
        print("-----------------------------")
        print("|Distribuição Por Colesterol|")
        print("-----------------------------")
        printTable(distNiveisColestrol(dados))



if __name__=="__main__":
    main()
