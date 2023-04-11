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


class Pilha:
    def __init__(self) -> None:
        self.__topo = None
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__tamanho == 0

    def empilha(self, elemento):
        novoNo = No(elemento)
        novoNo.prox = self.__topo
        self.__topo = novoNo
        self.__tamanho += 1

    def desempilha(self):
        elemento = self.__topo
        self.__topo = self.__topo.prox
        self.__tamanho -= 1
        return elemento
    # Implementar

    def elemento(self):
        pass

    def busca(self):
        pass

    def clone(self):
        pass

    def __len__(self):
        return self.__tamanho

    def __str__(self) -> str:
        res = 'topo ->['
        cursor = self.__topo
        while (cursor != None):
            res += f'{cursor.carga}'
            if cursor.prox != None:
                res += ', '
            cursor = cursor.prox
        res += ']'
        return res
