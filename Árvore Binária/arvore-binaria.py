class No:
    """
    A estrutura básica de uma árvore é o nó, ele possui apenas 3 atributos:
    - Carga: Onde o dado é guardado
    - Lados direito e esquerdo: Para fazer conexão com outros nós

    E possui apenas o método str que retorna em string o que está armazenado no nó."""

    def __init__(self, carga) -> None:
        self.carga = carga
        self.dir = None
        self.esq = None

    def __str__(self) -> str:
        return str(self.carga)


class Arvore:
    """
    A árvore possui 3 atributos:
    - Raíz: Onde armazenamos o primeiro nó da árvore
    - Cursor: Vai servir para percorrer a árvore e é necessário para fazer a inserção e remoção dos nós.
    - Tamanho: Serve apenas para retornar a quantidade de elementos na árvore, este pode ser um atributo ou um método. Nessa implementação utilizei o tamanho como atributo, então a cada inserção ou remoção o tamanho deve ser atualizado.
    """

    def __init__(self, raiz=None) -> None:
        self.tamanho = 0
        if raiz is None:
            self.raiz = raiz
        else:
            self.raiz = No(raiz)
            self.tamanho = 1
        self.cursor = self.raiz

    def estaVazia(self):
        return self.tamanho == 0

    def criaRaiz(self, carga: any) -> bool:
        if self.raiz is None:
            self.raiz = No(carga)
            self.tamanho = 1
            return True
        return False

    def getRaiz(self) -> any:
        if self.raiz is not None:
            return self.raiz.carga
        return None

    # Inserção e remoção
    """
        O cursor é necessário para qualquer operação de inserção ou remoção, a ideia é utilizar o cursor para percorrer os nós da árvore e assim inserir ou remover.

        Inserção: É feita a através dos métodos adicionaDir e adicionaEsq, no nó que o cursor está apontando. 
        Ex.:
                        50
                    /       \
                10            35
        P/ adicionar o valor 100, no lado esquerdo do nó 10, é necessário:
        - Primeiramente utilizar o método descerEsq, pois o cursor começa apontando para a raíz (50)
        - Agora que o cursor está apontando para o nó 10, podemos utilizar o método adicionaEsq.
        Res.:
                        50
                    /       \
                10            35
               /            
            100

    """

    # Retorna a posição do cursor
    def getCursor(self) -> any:
        if self.cursor is not None:
            return self.cursor.carga
        return None

    def descerEsq(self):
        if self.cursor is not None and self.cursor.esq is not None:
            self.cursor = self.cursor.esq

    def descerDir(self):
        if self.cursor is not None and self.cursor.dir is not None:
            self.cursor = self.cursor.dir

    # Cursor volta a apontar p/ raiz
    def resetCursor(self):
        self.cursor = self.raiz

    # Método retorna True quando o nó não possui filhos
    def __ehFolha(self, no: "No") -> bool:
        return no.dir == no.esq == None

    # A remoção segue a mesma lógica da inserção, porém só é possível remover um nó folha.
    def removeEsq(self):
        if self.cursor is not None and self.__ehFolha(self.cursor.esq):
            carga = self.cursor.esq.carga
            self.cursor.esq = None
            self.tamanho -= 1
            return carga
        return None

    def removeDir(self):
        if self.cursor is not None and self.__ehFolha(self.cursor.dir):
            carga = self.cursor.dir.carga
            self.cursor.dir = None
            self.tamanho -= 1
            return carga
        return None

    def adicionaEsq(self, carga) -> bool:
        if self.cursor is not None and self.cursor.esq is None:
            self.cursor.esq = No(carga)
            self.tamanho += 1
            return True
        return False

    def adicionaDir(self, carga) -> bool:
        if self.cursor is not None and self.cursor.dir is None:
            self.cursor.dir = No(carga)
            self.tamanho += 1
            return True
        return False

    """
        Perceba que a partir desta linha temos métodos com mesmo nome públicos e um privados, essa abordagem é utilizada pois os privados precisam usar os nós para percorrer a árvore. 

        Por exemplo, o método de busca tem apenas um parâmetro, o valor a ser procurado, porém é necessário percorrer árvore a partir da raiz até os nós folhas para saber se esse valor está ou não na árvore.

        Métodos público: O que o usuário quer acessar.
        Métodos privados: O ponto de partida desse método na árvore. 
    """

    # Exibe a árvore
    def preordem(self):
        self.__preordem(self.raiz)

    def __preordem(self, no: "No"):
        if no is not None:
            print(f"{no.carga}", end=" ")
            self.__preordem(no.esq)
            self.__preordem(no.dir)

    def posordem(self):
        self.__posordem(self.raiz)

    def __posordem(self, no: "No"):
        if no is not None:
            self.__posordem(no.esq)
            self.__posordem(no.dir)
            print(f"{no.carga}", end=" ")

    def emordem(self):
        self.__emordem(self.raiz)

    def __emordem(self, no: "No"):
        if no is not None:
            self.__emordem(no.esq)
            print(f"{no.carga}", end=" ")
            self.__emordem(no.dir)

    # Método recursivo para retornar o tamanho
    def __tamanho(self, no: No) -> int:
        """
        Com este método recursivo é possível eliminar o atributo tamanho da árvore.

        E funciona da seguinte forma:
        Quando o nó checado for vazio ele retorna 0, se não for vazio retorna 1 e chama o método para seu filho esquerdo e direito.
        """
        if no is None:
            return 0
        return 1 + (self.__tamanho(no.esq) + self.__tamanho(no.dir))

    def __len__(self):
        return self.__tamanho(self.raiz)

    # Utilizando o atributo tamanho
    # def __len__(self):
    #     return self.tamanho

    """
        O método de busca serve para procurar um elemento na árvore, a partir de uma carga (chave), e retornar um booleano. 
        
    """

    def busca(self, chave: any) -> bool:
        return self.__busca(chave, self.raiz)

    def __busca(self, chave: any, no: "No"):
        """
        Caso 1: Nós vazios não possuem filhos, então retornamos falso.
        Caso 2: Encontramos a chave, retorna True
        Se não está neste nó, pode estar no lado esquerdo ou direito.
        Caso 3: Verificamos do lado esquerdo e a chave foi encontrada, retorna True
        Caso 4: Se não, retorne o que tiver no lado direito.

        """
        if no is None:
            return False
        if chave == no.carga:
            return True
        if self.__busca(chave, no.esq):
            return True
        else:
            return self.__busca(chave, no.dir)

    def go(self, chave: any):
        no = self.__go(chave, self.raiz)
        if no is not None:
            return no
        else:
            return None

    def __go(self, chave, no: "No"):
        """
        O Go é parecido com a busca

        Caso 1: Se o nó for None, eu (a função recursiva 🤪) não tenho mais para onde ir, então retorno None.
        Caso 2: A chave procurada é igual a carga do nó, é retornado o nó.

        Se a chave não foi encontrada e o nó não é None, a chave pode estar do lado esquerdo ou do lado direito.
        Caso 3: Chamo novamente a função recursiva para o lado esquerdo e salvo em uma variável chamada recuperado, que pode ser None ou o nó (caso a chave seja encontrada). Se a chave for encontrada a função retorna o nó, se não retornamos o que tiver do lado direito.
        """
        if no is None:
            return None
        if chave == no.carga:
            return no
        recuperado = self.__go(chave, no.esq)
        if recuperado is not None:
            return recuperado
        else:
            return self.__go(chave, no.dir)


arv = Arvore(100)
print(len(arv))
