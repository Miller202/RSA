import os

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']

def MDC(a, b):  # encontra o MDC entre e e phi

    while a % b != 0:
        aux = b
        b = a % b
        a = aux

    return b


def gcd(e, phi):  # verifica se o e dado é válido

    if (MDC(e, phi) == 1 and e < phi):
        return True

    else:
        return False


def inverse(e, phi):
    d = 0
    while (int((d * e) % phi) != 1):
        d += 1
    return d


def encriptar(text, e, n):
    end = len(text)
    crypt_msg = ""
    for i in range(end):
        msg = text[i]
        index = alfabeto.index(msg) + 2
        crypt_msg += str((pow(index, e, n)))
        if (i + 1 < end):
            crypt_msg += ' '

    crypt_file = open("encrypt_file.txt", "w")
    crypt_file.write(crypt_msg)
    crypt_file.close()


def desencriptar(crypt_msg, d, n):  # em construção...
    i = 0
    end = len(crypt_msg)
    decrypt_msg = ""
    while i < end:
        aux = ""
        while i < end and crypt_msg[i] != ' ':
            aux += crypt_msg[i]
            i += 1
        i += 1
        aux = int(aux)
        decrypt_msg += alfabeto[(pow(aux, d, n)) - 2]

    decrypt_file = open("decrypt_file.txt", "w")
    decrypt_file.write(decrypt_msg)
    decrypt_file.close()


def gerarChavePublica(e, n):  # gera a chave publica (duh!)

    # A chave publica é (e,n)
    print("\nSua chave publica:  (", e, ",", n, ")\n")

    # gera o arquivo com a chave publica
    arquivo = open('public_key.txt', 'w')
    arquivo.write("Sua chave publica:  (" + str(e) + "," + str(n) + ")\n")
    arquivo.close()


def verificaPrimo(p):  # Verifica se o numero é primo pelo algoritmo de Euclides

    divs = 0

    for i in range(1, p + 1):
        if p % i == 0:
            divs += 1

    return (divs == 2)


################inicio##############


def main():
    p = 0
    q = 0
    e = 0
    phi = 0

    while (True):

        print('''      >>>>>>RSA MENU<<<<<<

            [1] Gerar Chave Pública
            [2] Encriptar
            [3] Desencriptar
            [4] Sair do Programa

             ''')
        opcao = int(input(">>Informe a opção desejada: "))

        if opcao == 1:
            # Lê um numero p
            p = int(input("Digite o P: "))
            # verifica se o p dado é mesmo primo
            while (verificaPrimo(p) == False):
                print("P informado nao valido\n")
                p = int(input("Digite o P: "))

            # Lê um numero q
            q = int(input("Digite o Q: "))
            # verifica se o q dado é mesmo primo
            while (verificaPrimo(q) == False or p == q):
                print("Q informado nao valido")
                q = int(input("Digite o Q: "))

            # calcula n
            n = p * q

            # calcula o phi
            phi = int((p - 1) * (q - 1))

            # lê um numero e
            e = int(input("Digite o e: "))
            # verifica se o e dado é válido
            while (gcd(e, phi) == False):
                print("E invalido, o valor de E deve ser co-primo com o produto phi = (p-1)*(q-1)")
                e = int(input("Digite o e: "))

            gerarChavePublica(e, n)
            print("\nChave publica gerada com sucesso")

        elif opcao == 2:
            n = p * q
            phi = int((p - 1) * (q - 1))

            path = input("Digite o diretorio do arquivo que deseja criptografar: ")
            file = open(path, "r")
            text = file.read().upper()
            file.close()
            e = input("Digite o [e] da chave publica: ")
            n = input("Digite o [n] da chave publica: ")
            e = int(e)
            n = int(n)
            encriptar(text, e, n)
            print('criptografado com sucesso')

        elif opcao == 3:

            p = int(input("Digite o P da chave privada: "))
            q = int(input("Digite o Q da chave privada: "))
            e = int(input("Digite o e da chave privada: "))

            phi = int((p - 1) * (q - 1))
            n = p * q
            d = inverse(e, phi)

            new_path = input("Digite o diretorio do arquivo que deseja descriptografar:")
            file = open(new_path, "r")
            crypt_msg = file.read()
            file.close()
            desencriptar(crypt_msg, d, n)
            print('descriptografado com sucesso')

        elif opcao == 4:
            break
        else:
            print("Opçao invalida!")


main()
