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

    def __len__(self):
        return self.__tamanho

    def __str__(self) -> str:
        res = '\n'
        cursor = self.__topo
        while (cursor != None):
            res += f'| {cursor.carga} |\n'
            cursor = cursor.prox
        return res
    # Lista 5

    def esvaziar(self):
        if self.estaVazia():
            raise PilhaException('A pilha já está vazia!')
        for i in range(self.__tamanho):
            self.desempilha()

    def inverteOrdem(self):
        tamanho = self.__tamanho
        aux = []
        for i in range(tamanho):
            aux.append(self.desempilha())
        for j in range(tamanho):
            self.empilha(aux[j])

    def concatena(self, pilha):
        pilha_aux = Pilha()
        tamanho = len(pilha)
        for i in range(tamanho):
            pilha_aux.empilha(pilha.desempilha())
        for j in range(tamanho):
            self.empilha(pilha_aux.desempilha())
    # @classmethod
    # def concatenaPilhas(cls, pilha1, pilha2):


# Teste
p1 = Pilha()
p2 = Pilha()
for i in range(5):
    p1.empilha(i+1)
    p2.empilha((i+1)*10)
print(p1)
print(p2)
p1.concatena(p2)
print(p1)
# p1.inverteOrdem()
# print(p1)
# p1.esvaziar()
# print(p1)
