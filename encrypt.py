import os

def menu():
    print('''      >>>>>>MENU<<<<<<
    
    [1] Gerar Chave Pública
    [2] Encriptar
    [3] Desencriptar
    [4] Sair do Programa
        
     ''')
    opção = int(input(">>Informe a opção desejada: "))

    return opção


def MDC(a, b):#encontra o MDC entre e e phi

    while a % b != 0:
        aux = b
        b = a % b 
        a = aux

    return b    


def verificaE(e, phi):#verifica se o e dado é válido

    if (MDC(e, phi) == 1 and  e < phi):
         return True

    else:
        return False


def encriptar():#em construção...
    pass



def desencriptar():#em construção...
    pass


def gerarChavePublica():#gera a chave publica (duh!)

    #Lê um numero p 
    p = int(input("Digite o P: "))

    #verifica se o p dado é mesmo primo
    if (verificaPrimo(p) == False):
        print("P informado não é válido\n")

    #Lê um numero q 
    q = int(input("Digite o Q: "))

    #verifica se o q dado é mesmo primo
    if (verificaPrimo(q) == False or p == q):
        print("Q informado não é válido")

    #calcula n
    n = p * q

    #calcula o phi
    phi = (p - 1) * (q - 1)

    #lê um numero e
    e = int(input("Digite o e: "))

    #verifica se o e dado é válido
    if (verificaE(e, phi) == False):
        print("E informado não é válido")


    #A chave publica é (e,n)
    print ("\nSua chave pública é:  (", e, ",", n,")\n")
    
    #gera o arquivo com a chave publica
    arquivo = open('Public_Key.txt','w')
    arquivo.write("Sua chave pública é:  (" + str(e) + "," + str(n) + ")\n")
 


def verificaPrimo(p):#Verifica se o numero é primo pelo algoritmo de Euclides

    divs = 0

    for i in range(1, p + 1 ):
        if p % i == 0:
            divs += 1

    return (divs == 2)



################inicio##############


os.system("clear") #se estiver usando Linux altere "cls" para "clear"

#chama menu  e guarda a opção informada pelo usuário
opção = 0

while opção != 4:


    opção = menu()

    
    if opção == 1:
        gerarChavePublica()

    elif opção == 2:
        encriptar()

    elif opção == 3:
        desencriptar()

    elif opção == 4:
        break
    else:
        print("Opção inválida!")

