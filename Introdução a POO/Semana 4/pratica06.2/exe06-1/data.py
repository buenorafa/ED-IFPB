# 1.
class Data:
    # b) Construtor
    def __init__(self, dia: int, mes: int, ano: int = 2023) -> None:
        if type(dia) != int or type(ano) != int or type(ano) != int:
            return None
        # a) Atributos privados
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # c) Métodos modificadores
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if type(dia) == int and dia >= 1 and dia <= 31:
            self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if type(mes) == int and mes >= 1 and mes <= 12:
            self.__dia = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if type(ano) == int:
            self.__ano = ano

    def setData(self, dia: int, mes: int, ano: int):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # d) Método __str__
    def __str__(self) -> str:
        return f'{self.__dia}/{self.__mes}/{self.__ano}'
