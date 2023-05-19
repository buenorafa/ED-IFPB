# Q1. Tamanho de uma string


def recursiveLength(value: str):
    if value == "":
        return 0
    else:
        return 1 + recursiveLength(value[1:])


# print(recursiveLength('Pedro'))


# Q.2 Função que imprima na tela uma string (caractere a caractere na mesma linha)


def printStr(string: str):
    if string == "":
        print("")
    else:
        print(string[0], end="")
        printStr(string[1:])


# printStr('Rafael')

# Q.3 Inverter a string


def invertString(string: str):
    if string == "":
        return ""
    else:
        return string[-1] + str(invertString(string[:-1]))


# print(invertString('Rafael'))

# Q.4 Printar a string invertida


def printInverse(string: str):
    if string == "":
        print("")
    else:
        print(string[-1], end="")
        printInverse(string[:-1])


# printInverse('Milena')


# Q.5 Comparar duas strings -> 0: São iguais, 1: str1 > str2 ou -1: str2 > str1
def compareStr(str1, str2):
    if len(str1) == 0 or len(str2) == 0:
        if len(str1) == len(str2):
            return 0
        elif len(str1) > len(str2):
            return 1
        else:
            return -1
    return compareStr(str1[1:], str2[1:])


# print(compareStr("Rafa", "Milena"))

# Q6. Verifica se é palindromo

# O erro da primeira func é que eu não estava retornando a chamada da função

# def ispalindrome(value: str) -> bool:
#     if value[0] != value[-1]:
#         return False
#     # Quer  dizer que a primeira e a ultima letra sao iguais
#     else:
#         # se a string nao tiver vazia, a string passa a ser ela sem a primeira e a ultima letra
#         if len(value) == 0:
#             return True
#         # aqui tiro a primeira e a ultima letra
#         # value = value[1:-1]
#         # chamo novamente a funçao passando a nova string
#         ispalindrome(value[1:-1])


def ispalindrome(value: str) -> bool:
    if len(value) < 2:
        return True
    else:
        if value[0] != value[-1]:
            return False
        else:
            # Aqui :)
            return ispalindrome(value[1:-1])


# print(ispalindrome("ABBA"))


# Q.7 Func p/ retornar as somas até n
def somaAteN(num: int) -> int:
    if num == 0:
        return 0
    return num + somaAteN(num - 1)


# print(somaAteN(5))


# Q.8 recebe uma lista e um num, retorna quantos elementos da lista são menores que num
def menores_rec(lista: list, num: int) -> int:
    if len(lista) == 0:
        return 0
    else:
        if lista[0] < num:
            return 1 + menores_rec(lista[1:], num)
        else:
            return menores_rec(lista[1:], num)


# print(menores_rec([1, 2, 3], 3))


# Q.9 Decimal para binário recursivamente - Como fazer: [https://embarcados.com.br/conversao-entre-sistemas-de-numeracao/]
def dectobin(num: int) -> str:
    if num == 1:
        return "1"
    else:
        return str(dectobin(num // 2)) + str(num % 2)


# print(dectobin(12))

# Q.10 Elemento radioativo que tem meia vida de 50segundo, receber massa em gramas e calcular qto tempo leva p decair até 0.8


def invictusRec(massa: float) -> int:
    if massa < 0.8:
        return massa, 0
    else:
        t = invictusRec(massa / 2)
        return t[0], t[1] + 50


# Apenas para correção


def invictusIterativo(massa):
    tempo = 0
    while massa >= 0.8:
        tempo += 50
        massa = massa / 2
    return massa, tempo


# print(invictusIterativo(10))
# print(invictusRec(10))


# Q.11 Calcular 1/1 ... 1/n até n
def seqTermos1(num):
    if num == 1:
        return 1
    else:
        return 1 / num + seqTermos1(num - 1)


# print(seqTermos1(3))


# Q.12 (nˆ2 + 1)/(n+3) até 1
def seqTermos2(num):
    if num == 1:
        return 2 / 4
    else:
        return (num**2 + 1) / (num + 3) + seqTermos2(num - 1)


# print(seqTermos2(2))


# Q.13 Soma de um vetor de num reais
def somaVec(lista: list) -> float:
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + somaVec(lista[1:])


# print(somaVec([1.5, 2.5, 3]))


# Q.14 Encontrar o maior valor em um vetor
def maior(lista: list):
    if len(lista) == 1:
        return lista[0]
    else:
        if lista[0] < lista[-1]:
            lista = lista[1:]
        else:
            lista = lista[:-1]
        return maior(lista)


# print(maior([1, 50, 50, 4]))


# Q.15 Verificar se o vetor está em ordem crescente
def ordenado(lista: list):
    if len(lista) < 2:
        return True
    else:
        if lista[0] < lista[1]:
            return ordenado(lista[1:])
        else:
            return False


# print(ordenado([1, 2, 3]))
# print(ordenado([1, 4, 3]))
