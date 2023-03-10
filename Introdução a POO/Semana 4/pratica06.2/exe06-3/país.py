# 3.
class País:
    # a) Fornecer um construtor que receba o nome, capital e a dimensão do país em Km2
    def __init__(self, nome: str, capital: str, dimensao: float) -> None:
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteira = []

    # b) Disponibilize métodos get e set para os atributos que considerar convenientes
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def capital(self):
        return self.__capital

    @capital.setter
    def capital(self, capital: str):
        self.__capital = capital

    @property
    def dimensao(self):
        return self.__dimensao

    @dimensao.setter
    def nome(self, dimensao: int):
        self.__dimensao = dimensao

    @property
    def fronteira(self):
        return self.__fronteira

    # c) Implementar um método que adiciona o nome de um país que faz fronteira com o país que representa o objeto. O método não deve permitir duplicidade de países e não deve diferenciar maiúscula de minúscula.
    def adicionaNaFronteira(self, nome: str) -> None:
        if nome.title() not in self.__fronteira:
            self.__fronteira.append(nome.title())

    # d) Adicionar o método __str__ para retornar as informações do país da seguinte forma:“Brasil, capital Distrito Federal, 8516000 km2”
    def __str__(self) -> str:
        return f'País: {self.__nome}\nCapital: {self.__capital}\nDimensão: {self.__dimensao} km2\nPaíses na fronteira: {self.__fronteira}'

    # e) Implemente um método que ao receber um objeto que representa outro país, informe se ambos possuem fronteira (ou não).
    def fazFronteira(self, nome: str) -> bool:
        if nome in self.__fronteira:
            return True
        return False
