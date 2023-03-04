class Calculadora():
    def __init__(self) -> None:
        self.__registrador = 0.00
        self.__aux = 0.00

    def soma(self, value: float):
        self.__aux = self.__registrador
        self.__registrador += value

    def subtrai(self, value: float):
        self.__aux = self.__registrador
        self.__registrador -= value

    def multiplica(self, value: float):
        self.__aux = self.__registrador
        self.__registrador = self.__registrador * value

    def divide(self, value: float):
        self.__aux = self.__registrador
        self.__registrador = self.__registrador / value

    def reset(self):
        self.__aux = self.__registrador
        self.__registrador = 0

    def desfazer(self):
        self.__registrador = self.__aux

    def __str__(self) -> str:
        return f'{self.__registrador:.2f}'
