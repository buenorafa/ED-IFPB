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

    def elemento(self, posicao: int) -> any:
        # if posicao <= 0 or posicao > self.__tamanho:
        #     raise PilhaException(
        #         f"Posicao invalida. A pilha so tem {self.__tamanho} elementos.")
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
        pilha_aux = Pilha()
        for i in range(tamanho):
            pilha_aux.empilha(self.desempilha())
        for i in range(tamanho, 0, -1):
            self.empilha(pilha_aux.elemento(i))

    def concatena(self, pilha):
        pilha_aux = Pilha()
        tamanho = len(pilha)
        for i in range(tamanho):
            pilha_aux.empilha(pilha.desempilha())
        for j in range(tamanho):
            self.empilha(pilha_aux.desempilha())

    @classmethod
    def concatenaPilhas(cls, pilha1, pilha2):
        p_res = Pilha()
        maior = max(len(pilha1), len(pilha2))
        for i in range(maior, 0, -1):
            if pilha1.elemento(i) != None:
                p_res.empilha(pilha1.elemento(i))
            if pilha2.elemento(i) != None:
                p_res.empilha(pilha2.elemento(i))
        return p_res
    # Lista 6

    def subTopo(self):
        if self.__tamanho <= 1:
            raise PilhaException('A pilha não possui subtopo.')
        return self.__topo.prox.carga

    def desempilha_n(self, num):
        if num > self.__tamanho:
            raise PilhaException('Tamanho maior que a pilha.')
        for i in range(num):
            self.desempilha()

    def obtemBase(self):
        cursor = self.__topo
        if cursor == None:
            raise PilhaException('A pilha está vazia.')
        while cursor != None:
            if cursor.prox == None:
                return cursor
            cursor = cursor.prox


# Teste

# Concatena Method
# p1 = Pilha()
# p2 = Pilha()
# # Deixo o tamanho da p2 > p1
# for i in range(5):
#     p1.empilha(i+1)
#     p2.empilha((0))
# p2.empilha(0)
# p2.empilha(0)
# # print(p1.elemento(len(p2)))
# print(Pilha.concatenaPilhas(p1, p2))


# Decimal p/ binario
# def dec2bin(num):
#     res = ''
#     pilha = Pilha()
#     while (num > 0):
#         pilha.empilha(num % 2)
#         num //= 2
#     for i in range(len(pilha)):
#         res += str(pilha.desempilha())
#     return res
# print(dec2bin(45))


# Palíndromo
# def palindromo(texto) -> bool:
#     p1 = Pilha()
#     for i in texto:
#         p1.empilha(i)
#     texto_inv = ''
#     for i in texto:
#         texto_inv += str(p1.desempilha())
#     return texto == texto_inv

# print(palindromo("a *n* a"))
# print(palindromo('alola'))

# TODO 7. Arranjo unidimensional

# # Subtopo
# p1 = Pilha()
# p1.empilha(':-)')
# p1.empilha('xD')
# print(p1.subTopo())

# # Desempilha n
# p1 = Pilha()
# p1.empilha('*_*')
# p1.empilha(':P')
# print(p1)
# p1.desempilha_n(2)
# print(p1)

# Esvazia já tem

# # Obtem a base
# p1 = Pilha()
# p1.empilha(';-;')
# print(p1.obtemBase())
