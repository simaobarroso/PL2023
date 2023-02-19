# tpc1 - Feito por Simao Barroso
#fazer com dicionario dentro de dicionarios

# Modelo pensado : dicionario de arrays: {id,[idade,...,temdoenca],etc}


#

f = open("myheart.csv")

def trata(line,id):
    campos = line.split(',')
    if id == 0: return campos
    if len(campos) != 6 : return null
    # nota verificar erros com possiveis campos - anormalias de dados
    #idade = ('idade',int(campos[0]))
    idade = int(campos[0])
    sexo = campos[1]
    #sexo = ('sexo',campos[1])
    tensao = int(campos[2])
    #tensao = ('tensao',int(campos[2]))
    colestrol=int(campos[3]) # Pensar em potenciais erros do colestrol (por exemplo colestrol a 0)!!!!!!!!!
    #colestrol = ('colestrol',int(campos[3]))
    batimento = int(campos[4])
    #batimento = ('batimento',int(campos[4]))
    temDoenca = int(campos[5])
    #temDoenca = ('temDoenca',int(campos[5]))
    auxdict = [idade,sexo,tensao,colestrol,batimento,temDoenca]
    return auxdict


dados = dict()

id = 0

# rever este codigo (otimizar + por isto em funcoes)
for line in f:
    if id == 0: pass # eliminei a primeira linha, mas melhorar isto
    else : dados[id]=trata(line,id)
    id=id+1


print(dados)

def doencaPorSexo(dados):
    homem = 0
    mulher = 0
    outrx= 0
    for ids in dados.keys():
        if dados[ids][1] == 'M' and dados[ids][5] == 1: homem = homem +1
        elif dados[ids][1] == 'F'  and dados[ids][5] == 1: mulher = mulher +1
        elif dados[ids][5] == 1 : outrx = outrx +1 # rever a cena dos outros generos !!!     
    return (homem,mulher,outrx)



#print(doencaPorSexo(dados)) # usar o matplotlib para graficos disto

#optar por quando se le tratar se j]a das funcoes pedidas

# fazer main disto !!!! 
# pedir no terminal o que queres executar 
# ver casos de excecao

def distIdade(dados):
    res = [0]*30 # n = 150 #maxidade
    for n in dados.keys():
        #print(dados[n][0]/5)
        if dados[n][5] == 1 : res[int(dados[n][0]/5)] = res[int(dados[n][0]/5)] + 1        
    return res
#melhorar e otimizar
#ver discord curso e tp 




#print(distIdade(dados))

#acabar
def drawdistIdades(dados):
    res = distIdade(dados)
    #utilizar matplotlib

def distNiveisColestrol(dados):
    res = [0] * 61
    for n in dados.keys():
        print(int(dados[n][3]/10))
        # print(dados[n][3]/10)
        if dados[n][5] == 1 : res[int(dados[n][3]/10)] = res[int(dados[n][3]/10)] + 1        
    return res

# int(5.5) = 5 !

print(distNiveisColestrol(dados))






# Notas: Fazer um ficheiro readMe.md a explicar ?
#        Melhorar codigo e comentarios
#        Tutorial de python (aula1 + net) 







