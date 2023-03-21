# tpc5 - cabine telefonica
# simaobarroso

import re

# soma as moedas e devolve o valor em centimos
# e` sempre mais facil para evitar erros de floating point trabalhar com ints
def somaCoins(lmoedas):
    res = 0
    lcoins = lmoedas.split(',')
    for l in lcoins:
        if e := re.fullmatch(r'(1|2)e',l):
            res+= 100*int(e.group(1))
        elif c:=re.fullmatch(r'(1|2|5|10|20|50)c',l) :
            res+= int(c.group(1))
        else: print("Moeda " + l + " no formato errado")
    return res

# ve se a chamada se pode fazer
def chamada(numero):
    custo = 0
    if re.match(r"^00\d+", numero): # numero internacionais podem ter n de digitos diferentes de 9
        custo += 150
    elif re.fullmatch(r"(0{2})?\d{9}", numero): # restantes dos numeros so podem ter 9 digitos
        if re.match(r"601", numero) or re.match(r"641", numero):
            print("Esse número não é permitido neste telefone. Escreva um novo número!")
        elif re.match(r"2", numero):
            custo += 25
        elif re.match(r"808", numero):
            custo += 10
        elif re.match(r"800", numero):
            custo += 0
        else:
            print("O número para o qual ligou não está atribuído!")
    else:
        print("O número apresentado não apresenta um formato correto! Por favor insira um novo número!")

    return custo

#devolve o saldo em euros no formato certo
def devolver(saldo):
    euros = saldo // 100
    centimos = saldo % 100
    if euros == 0:
        return "{}c".format(centimos)
    elif centimos == 0:
        return "{}e".format(euros)
    else:
        return "{}e{}c".format(euros, centimos)

# para devolver o formato com extra
def devolver2(saldo):
    qt = {'2e': 0,'1e':0,'50c':0,'20c':0,'10c':0,'5c':0,'2c':0,'1c':0}
    euros = saldo // 100
    centimos = saldo % 100
    res = ""
    while (euros > 0):
        if euros >= 2: 
            qt['2e'] +=1
            euros -= 2
        else:
            qt['1e'] +=1
            euros -= 1
    ct = [50,20,10,5,2,1]
    for c in ct:
        while(centimos>=c):
            qt[str(c)+'c'] += 1
            centimos -= c
    for el in qt:
        if(qt[el]>0): res+= str(qt[el]) + "x"+ el +" "
    return res    


def main():
    mode = 0 
    # 0 -> desligado
    # 1 -> Ligado
    t = True
    saldo = 0 #saldo em centimos
    while(t):
        i = input("> ")
        if re.fullmatch(r"\s*LEVANTAR\s*", i):
            if mode:
                print("maq: O telefone já está levantado. Insira moedas ou ligue para um número!")
            else:
                print("maq: Introduza Moedas.")
                mode = 1
        elif (numero := re.fullmatch(r"\s*T=(\d+)\s*", i)) and mode == 1:
            custo = chamada(numero.group(1))
            if custo > saldo:
                print("maq: Saldo Insuficiente! Por favor introduza mais moedas.")
            else:
                saldo -= custo
                print("maq: \"saldo="+ devolver(saldo)+"\"") 
        elif (lmoedas := re.fullmatch(r"\s*MOEDA\s([\w, ]*)\s*", i) )and mode == 1:
            saldo += somaCoins(lmoedas.group(1))
            print("maq: \"saldo="+ devolver(saldo)+"\"") 
        elif re.fullmatch(r"\s*ABORTAR\s*", i) and mode == 1:
            print("maq: \"troco="+devolver(saldo)+"; Obrigado!\"")
            print("maq: \"troco="+devolver2(saldo)+"; Volte sempre!\"")
            break
        elif re.fullmatch(r"\s*POUSAR\s*", i) and mode == 1:
            print("maq: \"troco="+devolver(saldo)+"; Obrigado!\"")
            print("maq: \"troco="+devolver2(saldo)+"; Volte sempre!\"")
            break
        else:
            print("maq: Operação Inválida")
            #break


if __name__=="__main__":
    main()    