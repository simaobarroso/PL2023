# tpc 4 - pl
# simao barroso
import re
import json
# abertura do ficheiro para leitura
nf = input("Nome do ficheiro:")
f = open(nf,'r')

datasetJson = []
lines = f.readlines()
#print(lines)

# NOTA TRATAR DE ERRO + OUTRAS OPERACOES

r= r"^(\w+),(\w+),(\w+)?,?(\w*)?{?(\d+)?,?(\d+)?}?:?:?(\w+)?,*$" 
# g1 = Número ; g2=Nome ; g3=Curso; g4=Notas ; g7=sum

m = re.match(r, lines[0])

#criar os dicionarios com as keys mas sem os values
ks = list()
for elem in m.groups():
    if elem:
        ks += [elem]
#print(ks)

for l in lines[1:]:
    #print(l)
    e = l.split(',')
    res = dict()
    if len(ks) == 3 :
        for i in range(0,len(e)):
            #PASSAR O NUMERO PARA INT?
            res[ks[i]]=e[i].strip('\n') 
            datasetJson += [res]
    elif len(ks) == 5:
        print("olaaa")
        for i in range(0,3):
            res[ks[i]]=e[i].strip('\n')
            datasetJson += [res] # funciona????????
        for i in range(3,len(e)):
            if (ks[3] in res.keys()):
                res[ks[3]] += [int(e[i])]
            else:
                res[ks[3]] = [int(e[i])]
        #datasetJson += [res] # funciona????????        
    elif len(ks) == 6:

        for i in range(0,3):
            res[ks[i]]=e[i].strip('\n')
            datasetJson += [res]             


print(datasetJson)

#fout = open("alunos.json","w")
#json.dump(datasetJson, fout, indent=' ')
