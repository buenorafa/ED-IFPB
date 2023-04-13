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


class PilhaException(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)


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

    def elemento(self, posicao: int) -> any:
        if posicao <= 0 or posicao > self.__tamanho:
            raise PilhaException(
                f"Posicao invalida. A pilha so tem {self.__tamanho} elementos.")
        contador = 1
        cursor = self.__topo
        while (cursor != None):
            if contador == posicao:
                return cursor.carga
            cursor = cursor.prox
            contador += 1

    def busca(self, key: any) -> int:
        contador = 1
        cursor = self.__topo
        while (cursor != None):
            if key == cursor.carga:
                return contador
            cursor = cursor.proxprox
            contador += 1
        raise PilhaException(f"A chave {key} não está na pilha.")

    def clone(self) -> 'Pilha':
        p_res = Pilha()
        for i in range(self.__tamanho, 0, -1):
            p_res.empilha(self.elemento(i))
        return p_res

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


# Testes
# # Clone
# p1 = Pilha()
# for i in range(5):
#     p1.empilha(i+1)
# print(f'P1: {p1}')
# p2 = p1.clone()
# print(f'P2: {p2}')
# p2.desempilha()
# print(f'P2: {p2}')
