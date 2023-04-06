class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Fila:
    def __init__(self, capacidade=10) -> None:
        self.__capacidade = capacidade
        self.__fila = [None] * capacidade
        self.__inicio = 0
        self.__final = 0
        self.__tamanho = 0

    def estaCheia(self):
        return self.__tamanho == self.__capacidade

    def estaVazia(self):
        return self.__tamanho == 0

    def adiciona(self, value):
        if self.estaCheia():
            raise FilaException('A fila já está cheia!')
        self.__fila[self.__final] = value
        self.__final = (self.__final + 1) % self.__capacidade
        self.__tamanho += 1

    def remove(self):
        if self.estaVazia():
            raise FilaException('A fila está vazia!')
        dados = self.__fila[self.__inicio]
        self.__inicio = (self.__inicio + 1) % self.__capacidade
        self.__tamanho -= 1
        return dados

    def __str__(self) -> str:
        if self.estaVazia:
            return 'A fila está vazia!'
        resultado = 'fila: ['
        index = self.__inicio
        for i in range(self.__tamanho):
            resultado += f'{self.__fila[index]}'
            index = (index + 1) % self.__capacidade
            if index != self.__final:
                resultado += ', '
        resultado += ']'
        return resultado


# TESTES:
fila = Fila()
fila.adiciona('#1')
fila.adiciona('#2')
fila.adiciona('#3')
fila.adiciona('#4')

print(fila)

fila.remove()
fila.remove()
fila.remove()
print(fila.remove())

print(fila)

try:
    fila.remove()
except FilaException as fe:
    print(fe)
