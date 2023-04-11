class No:
    # Metodo construtor
    def __init__(self, carga) -> None:
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga

    @property
    def prox(self) -> 'No':
        return self.__prox

    @prox.setter
    def prox(self, no) -> None:
        self.__prox = no

    def temProx(self) -> bool:
        return self.__prox != None

    def __str__(self) -> str:
        return str(self.__carga)


class Head:
    def __init__(self) -> None:
        self.__inicio = None
        self.__final = None
        self.__tamanho = 0

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, novoNo):
        self.__inicio = novoNo

    @property
    def final(self):
        return self.__final

    @inicio.setter
    def final(self, novoNo):
        self.__final = novoNo

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho


class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Fila:
    def __init__(self) -> None:
        self.__head = Head()

    def estaVazia(self):
        return self.__head.tamanho == 0

    def adiciona(self, value):
        novoNo = No(value)
        if self.estaVazia():
            self.__head.inicio = self.__head.final = novoNo
        else:
            self.__head.final.prox = novoNo
            self.__head.final = novoNo
        self.__head.tamanho += 1

    def remove(self):
        if self.estaVazia():
            raise FilaException('A fila está fazia.')
        elemento = self.__head.inicio.carga
        if self.__head.tamanho == 1:
            self.__head.final = None
        self.__head.inicio = self.__head.inicio.prox
        self.__head.tamanho -= 1
        return elemento

    def __len__(self):
        return self.__head.tamanho

    def __str__(self) -> str:
        res = 'inicio -> ['
        cursor = self.__head.inicio
        while cursor != None:
            res += f'{cursor.carga}'
            if cursor.prox != None:
                res += ', '
            cursor = cursor.prox
        res += '] <- fim'
        return res


# Teste
f1 = Fila()
f1.adiciona(1)
f1.adiciona(2)
print(f1)
print(f1.remove())
print(f1.remove())
