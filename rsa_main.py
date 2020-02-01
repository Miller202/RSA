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

def inverse(e, phi) :
    d = 0
    aux = int((d * e) % phi)
    while(aux != 1):
        d += 1
    return d

def encriptar():

    end = len(text)
    crypt_msg = ""
    for i in range(end):
        msg = text[i]
        #fórmula para criptografar a mensagem
        crypt_msg += str((alfa.index(msg) ** e) % n)
        if(i+1 < end):
            crypt_msg += ',' 
            
    crypt_file = open("encrypt_file.txt", "w")
    crypt_file.write(crypt_msg)
    crypt_file.close()



def desencriptar():#em construção...
    pass


def gerarChavePublica(e, n):#gera a chave publica (duh!)
    
    #A chave publica é (e,n)
    print ("\nSua chave pública é:  (", e, ",", n,")\n")

    #gera o arquivo com a chave publica
    arquivo = open('public_key.txt','w')
    arquivo.write("Sua chave pública é:  (" + str(e) + "," + str(n) + ")\n")
    arquivo.close()
 


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

    p = 0
    q = 0
    e = 0
    phi = 0
    
    if opção == 1:
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

        gerarChavePublica(e, n)
        print ("\nChave pública gerada com sucesso")

    elif opção == 2:
        n = p * q
        path = input("Digite o diretório do arquivo que deseja criptografar: ")
        file = open(path, "r")
        text = file.read()
        encriptar(file, text, e, n)
        file.close()

    elif opção == 3:
        n = p * q
        phi = (p - 1) * (q - 1)
        d = inverse(e, phi)

        path = input("Digite o diretório do arquivo que deseja descriptografar:")
        file = open(path, "r")
        crypt_msg = file.read()
        desencriptar(crypt_msg, d, n)
        file.close()

    elif opção == 4:
        break
    else:
        print("Opção inválida!")

