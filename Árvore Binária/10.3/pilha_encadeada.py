class PilhaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class No:
    def __init__(self, carga: any):
        self.__carga = carga
        self.__prox = None

    def getCarga(self):
        return self.__carga

    def getProximo(self) -> "No":
        return self.__prox

    def setProximo(self, novoProx: "No"):
        self.__prox = novoProx

    def temProximo(self) -> bool:
        return self.__prox == None

    def __str__(self):
        return f"{self.__carga}"


class Pilha:
    """A classe Pilha implementa a estrutura de dados "Pilha" utilizando a técnica encadeada.
      A classe foi desenvolvida de modo a permitir que qualquer tipo de dado seja armazenado como carga
      de um nó.

    Attributes:
       topo (No): referência para o nó que se encontra no topo da lista
       quantidade (int): número de elementos existentes na pilha
    """

    def __init__(self):
        """Construtor padrão da classe Pilha sem argumentos. Ao instanciar
        um objeto do tipo Pilha, esta iniciará vazia.
        """
        self.__topo = None
        self.__tam = 0

    def estaVazia(self) -> bool:
        """Método que verifica se a pilha está vazia .

        Returns:
            boolean: True se a pilha estiver vazia, False caso contrário.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente na pilha [10,20,30,40]<- topo
            if(p.estaVazia()):
               # instrucoes quando a pilha estiver vazia
        """
        return self.__topo == None

    def __len__(self):
        return self.__tam

    def tamanho(self) -> int:
        """Método que retorna a quantidade de elementos existentes na pilha

        Returns:
            int: um número inteiro que determina o número de elementos existentes na pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<- p
            print (p.tamanho()) # exibe 4
        """
        return self.__tam

    def elemento(self, posicao: int) -> any:
        """Método que recupera a carga armazenada em um determinado elemento da pilha

        Args:
            posicao (int): um número correpondente à ordem do elemento existente.
                           Sentido: da base em direção ao topo

        Returns:
            Any: a carga armazenada no elemento correspondente à posição indicada.

        Raises:
            PilhaException: Exceção lançada quando uma posição inválida é
                  fornecida pelo usuário. São inválidas posições que se referem a:
                  (a) números negativos
                  (b) zero
                  (c) número natural correspondente a uma posição  que excede a
                      quantidade de elementos da lista.
        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            posicao = 5
            print (p.elemento(3)) # exibe 30
        """
        if posicao <= 0 or posicao > self.tamanho():
            raise PilhaException(
                f"Posicao invalida. A pilha so tem {self.__tam} elementos."
            )

        contador = 1
        cursor = self.__topo
        while cursor != None:
            if contador == posicao:
                return cursor.getCarga()
            cursor = cursor.getProximo()
            contador += 1

    def busca(self, key: any) -> int:
        """Método que retorna a posicao ordenada, dentro da pilha, em que se
            encontra uma chave passado como argumento. No caso de haver mais de uma
            ocorrência do valor, a primeira ocorrência será retornada.
            O ordenamento que determina a posição é da base para o topo.

        Args:
            key (any): um item de dado que deseja procurar na pilha

        Returns:
            int: um número inteiro representando a posição, na pilha, em que foi
                 encontrada a chave.

        Raises:
            PilhaException: Exceção lançada quando o argumento "key"
                  não está presente na pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]<-topo
            print (p.elemento(40)) # exibe 4
        """
        contador = 1
        cursor = self.__topo
        while cursor != None:
            if key == cursor.getCarga():
                return contador
            cursor = cursor.getProximo()
            contador += 1

        raise PilhaException(f"A chave {key} não está na pilha.")

    def topo(self) -> any:
        """Método que devolve o elemento localizado no topo, sem desempilhá-lo.

        Returns:
            any: o conteúdo armazenado no elemento do topo

        Raises:
            PilhaException: Exceção lançada quando se tenta consultar o topo de uma
                   uma pilha vazia

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.topo()
            print(dado) # exibe 40
        """
        if self.__topo is None:
            raise PilhaException("Pilha Vazia")
        return self.__topo.getCarga()

    def empilha(self, carga: any):
        """Método que adiciona um novo elemento ao topo da pilha

        Args:
            carga (any): a carga que será armazenada no novo elemento do topo da pilha.

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            p.empilha(50)
            print(p)  # exibe [10,20,30,40,50]
        """
        no = No(carga)
        no.setProximo(self.__topo)
        self.__topo = no
        self.__tam += 1

    def desempilha(self) -> any:
        """Método que remove um elemento do topo da pilha e retorna
            sua carga correspondente.

        Returns:
           any: a carga armazenada no elemento removido

        Raises:
            PilhaException: Exceção lançada quando se tenta remover algo de uma pilha vazia

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a lista [10,20,30,40]
            dado = p.desemplha()
            print(p) # exibe [10,20,30]
            print(dado) # exibe 40
        """
        if self.__topo is None:
            raise PilhaException("Não há elementos para remoção. Pilha Vazia")
        carga = self.__topo.getCarga()
        self.__topo = self.__topo.getProximo()
        self.__tam -= 1
        return carga

    def imprime(self):
        """Método que exibe na tela a sequência ordenada dos elementos da pilha

        Examples:
            p = Pilha()
            ...   # considere que temos internamente a pilha [10,20,30,40]<-topo
            p.imprimir()) # exibe Lista: [10,20,30,40] <- topo
        """
        print(self.__str__())

    def __str__(self) -> str:
        """Método que retorna a ordenação atual dos elementos da pilha, do
            topo em direção à base

        Returns:
           str: a carga dos elementos da pilha, do topo até a base
        """
        s = "topo->[ "
        cursor = self.__topo
        while cursor != None:
            s += f"{cursor.getCarga()} "
            if cursor.getProximo() is not None:
                s += ", "
            cursor = cursor.getProximo()
        # s =
        # s += ' ]'
        # return s[:-2] + ' ]'
        return s + "]"
