# Q1. Tamanho de uma string


def recursiveLength(value: str):
    if value == '':
        return 0
    else:
        return 1 + recursiveLength(value[1:])

# print(recursiveLength('Pedro'))


# Q.2 Função que imprima na tela uma string (caractere a caractere na mesma linha)


def printStr(string: str):
    if string == '':
        print('')
    else:
        print(string[0], end='')
        printStr(string[1:])

# printStr('Rafael')

# Q.3 Inverter a string


def invertString(string: str):
    if string == '':
        return ''
    else:
        return string[-1] + str(invertString(string[:-1]))

# print(invertString('Rafael'))

# Q.4 Printar a string invertida


def printInverse(string: str):
    if string == '':
        print('')
    else:
        print(string[-1], end='')
        printInverse(string[:-1])


# printInverse('Milena')

# Q.5 Comparar duas strings
# TODO

# Q6. Verifica se é palindromo


def ispalindrome(value: str) -> bool:
    if value[0] != value[-1]:
        return False
    # Quer  dizer que a primeira e a ultima letra sao iguais
    else:
        # se a string nao tiver vazia, a string passa a ser ela sem a primeira e a ultima letra
        if value == '':
            return True
        # aqui tiro a primeira e a ultima letra
        value = value[1:-1]
        # chamo novamente a funçao passando a nova string
        ispalindrome(value)


# print(ispalindrome('ABBA'))
