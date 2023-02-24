# TPC2 - UC de Processamento de linguagens
# simaobarroso

# NOTA: NAO E PARA USAR REGEX (DISCORD - CURSO)

# variavel global para definir se soma ou nao
modo = 1 # 1 - on 0 - off
resultado = 0
# variaveis globais nem sepre boa ideia, ver alternativas


on = ['on','ON','oN','On']
off = ['OFF','off','Off','OFf','OfF','oFF','ofF','oFf']

"""
def trata(array):
    res = 0
    #for elem in array:
    return res

def exec1(): 
    file = open("text.txt")
    res = 0
    for line in file: # tratamos de cada linha do ficheiro
        elem = line.split(" ") #queremos tratar de casa sequencia de caracteres de cada vez
        for a in elem:
            
        #res += trata (elem) # se forem numeos adicionamos ao resultado final
    return res
"""

# VER PERGUNTAS BUGADORES ! + DISCORD
def trataString(a,res): # para resolver o caso do ```1 1=``` passo o res como parametro NAO DA PORQUE ISTO E PARA CADA STRING
    global modo
    global resultado
    r = 0
    if a in on and modo==0:
        modo = 1
        #print("foi alterado o modo para off, qualquer cena depois de on soma")
    elif (a in off) : 
        modo = 0
        #print("foi alterado o modo para off, qualquer cena depois de off nao soma")
        return 0
    elif modo == 0: return 0
    str = "0"
    i = 0
    tam = len(a)    
    for c in a:
        if c.isdigit() : 
            str += c    
        elif c != '=' and c.isdigit() == False :
            resultado += int(str)
            str = "0"
        if c=='=': 
            resultado += int(str)
            print(resultado)    
        i+=1
        if i == tam: resultado+=int(str) # ineficiente? sim
        #print(str)
    #resultado += r
# TER EM CONSIDERACAO \n e \t e cenas assim (uma ou varias ocurrencias)


def exec2(): 
    global resultado
    dados = input("Coloque aqui os dados:")
    elem = dados.split(" ")
    res = 0
    for a in elem:
        trataString(a,res) # vai escrever o resultado desta para variavel global
        #resultado += trataString(a,res) # depois rever para o igual !!!!!!! e ter em atencao que on\n conta como on (ou qualquer combinacao assim)
        # ver maneiras mais eficientes ! bigO percorrer uma vez
    #res = trata(elem)
    #return res

def main():
    #print(exec1()) # le de um ficheiro de texto e soma todos os digitos
    print("Por default esta on")
    exec2()
    #print('a'.isdigit())

if __name__=='__main__':
    main()