class No:
    def __init__(self, carga) -> None:
        self.carga = carga
        self.dir = None
        self.esq = None

    def __str__(self) -> str:
        return str(self.carga)

    """
    A árvore binária de busca é bem parecida com a normal, a diferença está nos métodos de inserção e remoção. 
    
    A regra da ABB é ao inserir um valor na árvore, se esse valor for menor que o nó atual, este é inserido no lado esquerdo, se não no lado direito. E ao remover qualquer elemento, essa regra deve ser mantida.

                        Valores menores < Nó > Valores maiores
    """


class ABB:
    def __init__(self, raiz=None) -> None:
        self.tamanho = 0
        if raiz is None:
            self.raiz = raiz
        else:
            self.raiz = No(raiz)
            self.tamanho = 1

    def estaVazia(self):
        return self.tamanho == 0

    def getRaiz(self) -> any:
        if self.raiz is not None:
            return self.raiz.carga
        return None

    def insere(self, valor) -> bool:
        # Primeiro elemento inserido na ABB se torna a raiz
        if self.raiz is None:
            self.raiz = No(valor)
            self.tamanho += 1
        else:
            return self.__insere(valor, self.raiz)

    def __insere(self, valor, no: "No") -> bool:
        # Caso 1: O valor que quero inserir é menor, chamo novamente a função recursiva passando o nó esquerdo este não for vazio. E se for vazio, basta inserir o nó no lado esquerdo e retornar True.
        if valor < no.carga:
            if no.esq != None:
                self.__insere(valor, no.esq)
            else:
                no.esq = No(valor)
                return True
        # Caso 2: Segue a mesma lógica do caso 1, mas neste caso o valor a ser inserido e por isso deve ir para o lado direito.
        else:
            if no.dir != None:
                self.__insere(valor, no.dir)
            else:
                no.dir = No(valor)
                return True

    def __min(self, no: No):
        if no.esq is None:
            return no
        return self.__min(no.esq)

    def remove(self, valor):
        carga = self.go(valor)
        if carga is not None:
            self.raiz = self.__remove(valor, self.raiz)
            return carga
        else:
            return None

    def __remove(self, valor, no: "No"):
        # Não há raiz
        if no is None:
            return no
        # Valor passado menor que a carga do nó, ele tem que ser encontrado no lado esquerdo da árvore
        elif valor < no.carga:
            no.esq = self.__remove(valor, no.esq)
        # E quando maior, do lado direito
        elif valor > no.carga:
            no.dir = self.__remove(valor, no.dir)
        else:  # Valor encontrado!
            # 1. Quando o nó a ser removido não tem filhos
            if no.esq == no.dir == None:
                no = None
                return no
            # 2. Quando tem um filho
            elif no.esq is None:  # Apenas o direito
                temp = no.dir
                no = None
                return temp
            elif no.dir is None:  # Apenas o esquerdo
                temp = no.esq
                no = None
                return temp
            # 3. Quando tem dois filhos: 🫠
            # salva o menor valor do lado direito (menor dos maiores 😅)
            temp = self.__min(no.dir)
            no.carga = temp.carga  # substitui a carga do nó
            no.dir = self.__remove(temp.carga, no.dir)  # e remove o nó que foi usado
        return no

    # A partir daqui, todos os métodos são os mesmos da classe Árvore Binária
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

    def __len__(self):
        return self.tamanho

    def busca(self, chave: any) -> bool:
        return self.__busca(chave, self.raiz)

    def __busca(self, chave: any, no: "No"):
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
        if no is None:
            return None
        if chave == no.carga:
            return no
        recuperado = self.__go(chave, no.esq)
        if recuperado is not None:
            return recuperado
        else:
            return self.__go(chave, no.dir)


# Testes

arv = ABB(10)
arv.insere(5)
arv.insere(15)
arv.insere(25)
arv.insere(0)


arv.remove(10)


arv.emordem()
