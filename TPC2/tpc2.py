# TPC2 - UC de Processamento de linguagens
# simaobarroso

# NOTA: NAO E PARA USAR REGEX (DISCORD - CURSO)

def trata(array):
    res = 0
    for elem in array:
        x = 0
        try:
            x = int(elem)
        except:
            pass    
        res += x
    return res

def exec1(): 
    file = open("text.txt")
    res = 0
    for line in file: # tratamos de cada linha do ficheiro
        elem = line.split(" ") #queremos tratar de casa sequencia de caracteres de cada vez
        res += trata (elem) # se forem numeos adicionamos ao resultado final
    return res


def exec2(): 
    dados = input("Coloque aqui os dados:")
    elem = dados.split(" ")
    res = trata(elem)
    return res

def main():
    print(exec1()) # le de um ficheiro de texto e soma todos os digitos
    print(exec2())

if __name__=='__main__':
    main()