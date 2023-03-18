# tpc5 - 
# simaobarroso

# utilizar ply? 
# modulo re


# ver outras maneiras + melhorar regex + ply + module re !!!

# melhorar isto !

# discord + aulas teoricas
import re

def calcTroco(saldo): #suponho que o saldo venha em numero inteiro
    # saldo das moedas dado em centimos
    res = ""
    e = int (saldo / 100) # esta incorreto (dividir troco em moedas?)
    res += e +"e "
    resto = saldo % 100
    while(resto != 0):
        if resto>50:
            res += "50c "
            resto -= 50
        elif resto > 20:
            res += "20c "
            resto -= 20
        elif resto > 10:
            res += "10c "
            resto -= 10
        elif resto > 10:
            res += "10c "
            resto -= 10
        elif resto > 5:
            res += "5c "
            resto -= 5 
        else:
            res += str(resto) +"c "
            resto -= resto       
    return res


def main():
    m
    mode = 0 # 
    t = True
    saldo = 0
    while(t):
        i = input("> ")
        rgW = r'\w+' # Confirmar com testes, mas esta a funcionar
        l = re.findall(rgW,i)
        n = 0
        for e in l:
            # match (e):
            if e == "LEVANTAR":
                mode = 1
                print("maq > Introduza moedas.")
            elif e == "POUSAR":
                mode = 0
                troco = calcTroco(saldo)
                print("maq > Troco = " + troco)
                t = False # suponho que depois do pousar nao possa vir um levantar
            elif e == "T":
                pass
            elif e == "MOEDA":
                pass
            elif e == "ABORTAR":
                pass        
            n+=1

if __name__=="__main__":
    main()    