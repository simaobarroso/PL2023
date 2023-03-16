# tpc 4 - pl
# simao barroso
import re
import json
import statistics
# abrir e guardar o ficheiro
nf = input("Nome do ficheiro:")
f = open(nf,'r')
datasetJson = []
lines = f.readlines()
# expreg para os diferentes tipos de primeiras linhas que podem exitir
r= r"^(\w+),(\w+),(\w+)?,?(\w*)?{?(\d+)?,?(\d+)?}?:?:?(\w+)?,*$" 
# g1 = Número ; g2=Nome ; g3=Curso; g4=Notas ; g7=sum,etc...
# match com a primeira linha do csv
m = re.match(r, lines[0])
# coloca os elementos do match numa lista de keys
ks = list()
for elem in m.groups():
    if elem:
        ks += [elem]
#print(ks)
# vamos percorrer as linhas restantes do csv e colocar  num dicionario
for l in lines[1:]:
    #print(l)
    e = l.split(',') # csv logo divide-se por , (ou ; mas nao neste caso)
    res = dict() # cada linha vai ser traduzida para um dicionario (json <=>lista de dicionarios)
    if len(ks) == 3 : # primeiro caso, o alunos1.csv
        for i in range(0,len(e)):
            #PASSAR O NUMERO PARA INT?
            res[ks[i]]=e[i].strip('\n') 
            datasetJson += [res]
    elif len(ks) == 5: # alunos2.csv
        for i in range(0,3):
            res[ks[i]]=e[i].strip('\n') 
        for i in range(3,len(e)):
            if (ks[3] in res.keys()):
                res[ks[3]] += [int(e[i])]
            else:
                res[ks[3]] = [int(e[i])]
        datasetJson += [res]    
    elif len(ks) == 6 and int(ks[4]) <= len(e)-3 and int(ks[5]) >= len(e)-3: # alunos3.csv
        #mais condicoes porque caso a linha temos menos ou mais notas do que as aceitaveis e` descartada
        for i in range(0,3):
            res[ks[i]]=e[i].strip('\n')
        for i in range(3,len(e)):
            if e[i] != '\n' and e[i] != '':
                if (ks[3] in res.keys()):
                    res[ks[3]] += [int(e[i])]
                else:
                    res[ks[3]] = [int(e[i])]
        datasetJson += [res] 
    elif len(ks) == 7 and int(ks[5]) >= len(e)-3 and int(ks[4]) <= len(e)-3: #alunos4.csv para a frente
        for i in range(0,3):
            res[ks[i]]=e[i].strip('\n') #primeiras 3 parametros de cada linha e` igual independentemente do metodo
        match(ks[-1]):  # switch ou match case para cada caso
            case "sum":
                for i in range(3,len(e)):
                    if e[i] != '\n' and e[i] != '':
                        if (ks[3]+'_sum' in res.keys()):
                            res[ks[3]+'_sum'] += int(e[i])
                        else:
                            res[ks[3]+'_sum'] = int(e[i])
                datasetJson += [res] 
            case "media":
                total = 0
                for i in range(3,len(e)):
                    if e[i] != '\n' and e[i] != '':
                        total +=1
                        if (ks[3]+'_media' in res.keys()):
                            res[ks[3]+'_media'] += int(e[i])
                        else:
                            res[ks[3]+'_media'] = int(e[i])
                #print(res[ks[3]+'_media'])
                #print(total)
                res[ks[3]+'_media'] /= total    
                datasetJson += [res]    
            case "produto":
                 for i in range(3,len(e)):
                    if e[i] != '\n' and e[i] != '':
                        if (ks[3]+'_produto' in res.keys()):
                            res[ks[3]+'_produto'] *= int(e[i])
                        else:
                            res[ks[3]+'_produto'] = int(e[i])
                    datasetJson += [res] 
            case "mediana": #median
                lista = list()
                for i in range(3,len(e)):
                    if e[i] != '\n' and e[i] != '':
                        lista += [int(e[i])]
                #print(lista)    
                res[ks[3]+'_mediana'] = statistics.median(lista)         
                datasetJson += [res] 
            case "moda":
                lista = list()
                for i in range(3,len(e)):
                    if e[i] != '\n' and e[i] != '':
                        lista += [int(e[i])]
                #print(lista)    
                res[ks[3]+'_moda'] = statistics.mode(lista)         
                datasetJson += [res]                                                     

# Fazer mais casos + situcao de erro!!

print(datasetJson)

fout = open("alunos.json","w")
json.dump(datasetJson, fout, indent=' ')
