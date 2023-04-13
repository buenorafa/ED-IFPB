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

    # O elemento 1 deve ser o topo da pilha
    def elemento(self, num):
        if num > self.__tamanho:
            raise PilhaException(
                f'A pilha possui só {self.__tamanho} elementos.')
        contador = self.__tamanho
        return self.__pilha[contador - num]

    def busca(self, carga):
        for i in range(self.__tamanho):
            if carga == self.__pilha[i]:
                return self.__tamanho - i
        raise PilhaException('O elemento não está na pilha.')

    def __len__(self):
        return self.__tamanho

    def __str__(self) -> str:
        res = '['
        for i in range(self.__tamanho):
            res += f'{self.__pilha[i]}'
            if i < self.__tamanho - 1:
                res += ', '
        res += '] <- topo'
        return res
    # Métodos necessários p/ exe.05

    def topo(self):
        return self.__pilha[self.topo]

    def inverteOrdem(self):
        tamanho = self.__tamanho
        aux = []
        for i in range(tamanho):
            aux.append(self.desempilha())
        for j in range(tamanho):
            self.empilha(aux[j])

    def esvaziar(self):
        if (self.estaVazia()):
            raise PilhaException('A pilha já está vazia!')
        for i in range(self.__tamanho):
            self.desempilha()
        return self.__tamanho == 0
    # Falta terminar a concatena
    # . Percorrer todoso os elementos de cada pilha

    def concatena(self, pilha):
        pilha_aux = Pilha()
        tamanho = len(pilha)
        for i in range(tamanho):
            pilha_aux.empilha(pilha.desempilha())
        for j in range(tamanho):
            self.empilha(pilha_aux.desempilha())

# TESTE
# p1 = Pilha()
# p2 = Pilha()
# for i in range(5):
#     p1.empilha(i+1)
#     p2.empilha((i+1)*10)
# print(p2)
# p1.concatena(p2)
# print(p1)

# Inverte a ordem
# p1.inverteOrdem()
# print(p1)

# Esvazia a pilha
# try:
#     p1.esvaziar()
# except PilhaException as pe:
#     print(pe)
# print(p1)

# # Elemento
# p1 = Pilha()
# for i in range(5):
#     p1.empilha(i+1)
# try:
#     print(p1.elemento(10))
# except PilhaException as pe:
#     print(pe)

# # Busca
# p1 = Pilha()
# for i in range(5):
#     p1.empilha(i+1)
# try:
#     print(p1.busca(5))
# except PilhaException as pe:
#     print(pe)
