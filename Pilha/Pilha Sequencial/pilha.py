class PilhaException(Exception):
    def __init__(self, mensagem) -> None:
        super().__init__(mensagem)


class Pilha:
    def __init__(self, capacidade=10) -> None:
        self.__capacidade = capacidade
        self.__pilha = [None]*self.__capacidade
        self.__topo = -1
        self.__tamanho = 0

    def estaVazia(self) -> bool:
        return self.__tamanho == 0

    def estaCheia(self) -> bool:
        return self.__tamanho == self.__capacidade

    def tamanho(self) -> int:
        return self.__tamanho

    def empilha(self, elem):
        if self.estaCheia():
            raise PilhaException('A pilha está cheia.')
        self.__topo += 1
        self.__pilha[self.__topo] = elem
        self.__tamanho += 1

    def desempilha(self):
        if self.estaVazia():
            raise PilhaException('A pilha está vazia.')
        elem = self.__pilha[self.__topo]
        self.__topo -= 1
        self.__tamanho -= 1
        return elem
    
    def concatena(self, pilha):
        

    def __len__(self):
        return self.__tamanho

    def __str__(self) -> str:
        res = 'pilha -> ['
        for i in range(self.__tamanho):
            res += f'{self.__pilha[i]}'
            if i < self.__tamanho - 1:
                res += ', '
        res += ']'
        return res

#   =============================================================   #
#                              TESTE
#   =============================================================   #

# p = Pilha()
# print(p.estaVazia())    # True
# p.empilha(20)
# p.empilha(30)
# p.empilha(40)
# print(p.estaVazia())    # False
# print(p)    # [20, 30, 40]
# p.desempilha()
# print(p)    # [20, 30]
