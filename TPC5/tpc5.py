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
    res1 = ""
    res2 = ""
    e = int (saldo / 100) # esta incorreto (dividir troco em moedas?)
    res1 += e +"e "
    resto = saldo % 100
    res1 += resto + "c"
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

    return res1,res2


def main():
    m
    mode = 0 
    # 0 -> desligado
    # 1 -> Ligado
    # 2 -> ligado e vai receber um numero
    # 3 -> ligado e vai receber moedas
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
                print("maq > Troco = " + troco) # mudar isto
                t = False # suponho que depois do pousar nao possa vir um levantar
            elif e == "T":
                mode = 2
                pass
            elif e == "MOEDA":
                mode = 3
            elif e == "ABORTAR":
                pass
            elif re.match(r"\d+",e) and mode == 2:      
                # numero de telemovel 
                mode = 1

            n+=1

if __name__=="__main__":
    main()    