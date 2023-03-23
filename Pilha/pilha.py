class Pilha:
    def __init__(self) -> None:
        self.__pilha = []

    def estaVazia(self) -> bool:
        return len(self.__pilha) == 0

    def tamanho(self) -> int:
        return len(self.__pilha)

    def imprime(self) -> str:
        return str(self.__pilha)[1:-1]

    def empilha(self, elem):
        self.__pilha.append(elem)

    def desempilha(self):
        self.__pilha.pop()

    def __str__(self) -> str:
        return f'{self.__pilha}'

#   =============================================================   #
#   TESTE
#   =============================================================   #


p = Pilha()
print(p.estaVazia())    # True
p.empilha(20)
p.empilha(30)
p.empilha(40)
print(p.imprime())  # 40,30,20
print(p.estaVazia())    # False
print(p)    # [20, 30, 40]
p.desempilha()
print(p)    # [20, 30]
