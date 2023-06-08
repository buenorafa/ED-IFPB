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

    # ==============================================================================
    #  ELIMINAR O CURSOR
    # ==============================================================================
    # def getCursor(self) -> any:
    #     if self.cursor is not None:
    #         return self.cursor.carga
    #     return None

    # ==============================================================================
    #  GET
    # ==============================================================================
    def get(self, key: int):
        return self.__get(key, self.raiz)

    def __get(self, key: int, no: "No"):
        if no is None:
            return None
        if key == no.carga:
            return no
        # Verifica se está no lado esquerdo
        lado_esq = self.__get(key, no.esq)
        if lado_esq:  # lado_esq não for None
            return lado_esq
        else:
            return self.__get(key, no.dir)

    # TODO ADICIONA, REMOVE
    def add_dir(self, key: int, carga: int) -> bool:
        if self.get(key):
            no = self.__get(key, self.raiz)
            no.dir = No(carga)
            return True
        return False

    def add_esq(self, key: int, carga: int) -> bool:
        if self.get(key):
            no = self.__get(key, self.raiz)
            no.esq = No(carga)
            return True
        return False

    # REMOVE TODOS A PARTIR DE UM NÓ
    def remove(self, key: int):
        if self.get(key):
            no = self.__get(key, self.raiz)
            self.__remove(no)
            return True
        return False

    def __remove(self, no: "No"):
        if no is not None:
            no = self.__remove(no.esq) and self.__remove(no.dir)
        return None

    # REMOVE UM LADO
    def remove_dir(self, key) -> bool:
        if self.get(key):
            no = self.__get(key, self.raiz)
            no.dir = self.__remove(no.dir)
            return True
        return False

    def remove_esq(self, key) -> bool:
        if self.get(key):
            no = self.__get(key, self.raiz)
            no.esq = self.__remove(no.esq)
            return True
        return False

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

    def __ehFolha(self, no: "No") -> bool:
        return no.dir == no.esq == None

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


arv = Arvore(10)

arv.add_esq(10, 4.20)
arv.add_dir(10, 15)
arv.emordem()
print()
# print(arv.remove(15))   

arv.emordem()
