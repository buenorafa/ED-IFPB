from pilha_encadeada import *


"""
    Utilizar uma pilha encadeada p/ auxiliar as operações do cursor

    A cada vez que o cursor mudar de posição, deve ser adicionada a mudança na pilha? 

                      ->            1
                                2       3

    Antes de realizar a mudança no cursor o estado atual do cursor deve ser salvo, por exemplo: se o cursor se encontra na posição inicial (raiz), quando for feita a operação de descer para qualquer um dos lados, deve ser salva a posição atual na pilha. 

"""


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
        self.__pilha = Pilha()

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

    # =============================================================================
    #  Cursor
    # =============================================================================
    def getCursor(self) -> any:
        if self.cursor is not None:
            return self.cursor.carga
        return None

    def descerEsq(self):
        self.__pilha.empilha(self.cursor)
        if self.cursor is not None and self.cursor.esq is not None:
            self.cursor = self.cursor.esq

    def descerDir(self):
        self.__pilha.empilha(self.cursor)
        if self.cursor is not None and self.cursor.dir is not None:
            self.cursor = self.cursor.dir

    def resetCursor(self):
        self.__pilha.empilha(self.cursor)
        self.cursor = self.raiz

    # =============================================================================
    #  Back
    # =============================================================================
    def back(self):
        if len(self.__pilha) > 0:
            self.cursor = self.__pilha.desempilha()
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


# TESTE

arv = Arvore(10)
arv.adicionaEsq("Esquerda")
arv.adicionaDir("Direita")
arv.descerDir()
arv.adicionaDir(500)
arv.adicionaEsq(500)
arv.back()
print(arv.getCursor())
arv.emordem()
