class No:
    def __init__(self, carga) -> None:
        self.carga = carga
        self.dir = None
        self.esq = None

    def __str__(self) -> str:
        return str(self.carga)


class Arvore:
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

    def getCursor(self) -> any:
        if self.cursor is not None:
            return self.cursor.carga
        return None

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

    def descerEsq(self):
        if self.cursor is not None and self.cursor.esq is not None:
            self.cursor = self.cursor.esq

    def descerDir(self):
        if self.cursor is not None and self.cursor.dir is not None:
            self.cursor = self.cursor.dir

    def resetCursor(self):
        self.cursor = self.raiz

    def __ehFolha(self, no: "No") -> bool:
        return no.dir == no.esq == None

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

    def __len__(self):
        return self.tamanho

    # TODO BUSCA E GO
    def busca(self, chave: any) -> bool:
        return self.__busca(chave, self.raiz)

    def __busca(self, chave: any, no: "No"):
        if no is None:
            return False
        if chave == no.carga:
            return True
        # print(no.carga)
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

    # Exercícios
    # ---------------------------------------------------------------------------- #
    # INVERTE ARVORE
    def inverte(self):
        return self.__inverte(self.raiz)

    def __inverte(self, no: "No"):
        if no is not None:
            self.__inverte(no.esq)
            self.__inverte(no.dir)
            aux = no.dir
            no.dir = no.esq
            no.esq = aux

    # QTD. DE NÓS NA ARV
    def elementos(self):
        return self.__elementos(self.raiz)

    def __elementos(self, no: "No"):
        if no is None:
            return 0
        return 1 + ((self.__elementos(no.esq) + self.__elementos(no.dir)))

    def altura(self):
        if self.raiz is None:
            return None
        return self.__altura(self.raiz)

    def __altura(self, no: "No"):
        if no is None:
            return 0
        return 1 + (
            self.__altura(no.esq)
            if self.__altura(no.esq) > self.__altura(no.dir)
            else self.__altura(no.dir)
        )

    # leafs
    def leafs(self):
        return self.__leafs(self.raiz)

    def __leafs(self, no: "No"):
        if no is not None:
            if self.__ehFolha(no):
                return 1
            return self.__leafs(no.dir) + self.__leafs(no.esq)
        return 0

    # DUVIDA
    # def getLevel(self, key: int) -> int:
    #     if self.busca(key):
    #         return self.__getLevel(key, self.raiz)
    #     return None

    # def __getLevel(self, key, no: "No"):
    #     if no is None:
    #         return -1
    #     if key == no.carga:
    #         return 0

    """
    condições de parada:
        se no for none tem que parar de percorrer 
        se encontrar a chave
    """

    # TODO PEGAR O MAIOR VALOR DE UMA ARV
    def maior(self):
        if self.raiz is not None:
            maior = self.__maior(self.raiz)
            return maior
        return None

    def __maior(self, no: "No"):
        if no is None:
            return float("-inf")
        maior = no.carga
        # Testa o lado esquerdo e direito
        maior_esq = self.__maior(no.esq)
        maior_dir = self.__maior(no.dir)
        if maior < maior_esq:
            maior = maior_esq
        if maior < maior_dir:
            maior = maior_dir
        # return o maior
        return maior

    # TODO Libera
    def libera(self, key):
        if self.busca(key):
            no = self.__go(key, self.raiz)
            if no is not None:
                self.__libera(no)
        return None

    def __libera(self, no: "No"):
        if no is not None:
            no.dir = self.__libera(no.dir)
            no.esq = self.__libera(no.esq)
        return None


#
# TESTES
#
arv = Arvore(1)
arv.adicionaEsq(2)
arv.adicionaDir(3)
arv.descerEsq()
arv.adicionaEsq(4)
arv.resetCursor()
# arv.descerDir()
# arv.adicionaEsq(5)
# arv.adicionaDir(7)
# arv.descerEsq()
# arv.adicionaDir(6)
# arv.resetCursor()
# arv.descerDir()
# arv.descerDir()
# arv.adicionaDir(8)
# arv.descerDir()
# arv.adicionaEsq(9)

# print(arv.leafs())
arv.emordem()
# arv.inverte()
# arv.libera(1)
print()
# arv.emordem()
print(arv.altura())
print(arv.getLevel(4))
# print(arv.altura())
