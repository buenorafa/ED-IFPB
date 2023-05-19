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

    # TODO pre, pos e in, fazer depois de criar o add e o remove
    def preordem(self):
        pass

    def __preordem(self, no: "No"):
        if no is not None:
            pass

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
