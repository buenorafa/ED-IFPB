# Método para esvaziar uma fila encadeada, caso o somatório dos elementos seja menor que o parâmetro (limiar)

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
        self.__frente = None
        self.__final = None
        self.__tam = 0

    @property
    def frente(self):
        return self.__frente

    @frente.setter
    def frente(self, novoNo):
        self.__frente = novoNo

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, novoNo):
        self.__final = novoNo

    @property
    def tam(self):
        return self.__tam

    @tam.setter
    def tam(self, novoTamanho):
        self.__tam = novoTamanho

class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Fila:
    def __init__(self) -> None:
        self.__head = Head()

    def estaVazia(self) -> bool:
        return self.__head.tam == 0

    def enfileira(self, value):
        novoNo = No(value) #Prox None
        if self.estaVazia():
            # Tamanho 0, Frente e Final = None
            self.__head.frente = novoNo
            self.__head.final = novoNo
        else:
            # Final.Próximo = None
            self.__head.final.prox = novoNo
            # Final.Próximo = novoNó
            self.__head.final = novoNo #prox = none
            #Final = novoNó 
        self.__head.tam += 1

 
    def desenfileira(self):
        # Verifica se ta vazio
        if self.estaVazia():
            raise FilaException('A fila está fazia.')
        # Salva o carga do nó que está na frenta fila
        elemento = self.__head.frente.carga 
        # Verifica se o tamanho = 1
        if self.__head.tam == 1:
            self.__head.final = None
        # A frente da fila passa a ser o que ta depois dela
        self.__head.frente = self.__head.frente.prox
        self.__head.tam -= 1
        return elemento

    def __len__(self) -> int:
        return self.__head.tam

    def __str__(self) -> str:
        res = 'frente -> ['
        cursor = self.__head.frente
        while (cursor != None):
            res += f'{cursor.carga}'
            if cursor.prox != None:
                res += ', '
            cursor = cursor.prox
        res += '] <- fim'
        return res
    
    # def esvaziar(self, limiar):
    #     if not self.estaVazia():
    #         tamanho = self.__head.tam
    #         cursor = self.__head.frente
    #         somatorio = 0
    #         for i in range(tamanho):
    #             somatorio += cursor.carga
    #             cursor = cursor.prox
    #         if somatorio < limiar:
    #             self.__head.frente = self.__head.final = None
    #             somatorio = 0
    #             return True
    #     return False

if __name__ == '__main__':
    # # Teste
    f1 = Fila()
    for i in range(5):
        f1.enfileira(i+1)
    print(f1)
    # print(f1.esvaziar(15))  # False
    # print(f1)
    