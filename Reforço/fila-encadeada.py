# Método para esvaziar uma fila encadeada, caso o somatório dos elementos seja menor que o parâmetro (limiar)

class No:
    # Metodo construtor
    def __init__(self, carga) -> None:
        #
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

# no1 = No('Rafael')
# no2 = No('Danillo')
# no1.prox = no2


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
# FIFO: Primeiro a entrar é o primeiro a sair


class Fila:
    def __init__(self) -> None:
        self.__head = Head()
        # frente, final e tamanho

    def estaVazia(self):
        return self.__head.tam == 0

    def enfileira(self, value):
        novoNo = No(value)
        if self.estaVazia():
            self.__head.frente = novoNo
            self.__head.final = novoNo
        else:
            self.__head.final.prox = novoNo
            self.__head.final = novoNo
        self.__head.tam += 1

    def desenfileira(self):
        if self.estaVazia():
            raise FilaException('A fila está fazia.')
        elemento = self.__head.frente.carga
        if self.__head.tam == 1:
            self.__head.final = None
        self.__head.frente = self.__head.frente.prox
        self.__head.tam -= 1
        return elemento

    def __len__(self):
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

    # Q1 : Método que se a soma das cargas da fila for menor limiar (param), esvazia a fila inteira
    def esvaziar(self, limiar) -> bool:
      if self.estaVazia():
        raise FilaException('A fila já está fazia.')
      # Pegar a soma de todos elementos
      soma = 0
      cursor = self.__head.frente  #primeiro nó
      while (cursor != None):
        soma += cursor.carga
        cursor = cursor.prox
      # Soma < limiar
      if soma < limiar:
        self.__head.frente = None
        self.__head.final = None
        self.__head.tam = 0
        return True
      return False
  

fila = Fila()
fila.enfileira(10)
fila.enfileira(10)
fila.enfileira(10)
# metodo esvaziar  e desenfilera -> a fila tá vazia
print(fila.esvaziar(50)) # Deve retornar True, pois o limiar é maior que a soma dos elementos