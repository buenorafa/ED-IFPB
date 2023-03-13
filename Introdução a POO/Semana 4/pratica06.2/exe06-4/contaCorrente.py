class ContaCorrente():
    def __init__(self, numero: str, nome: str, saldo: int = 0) -> None:
        self.__conta = numero
        self.__titular = nome
        self.__saldo = saldo

    def getConta(self) -> str:
        return self.__conta

    def getTitular(self) -> str:
        return self.__titular

    def depositar(self, valor) -> None:
        self.__saldo += valor

    def sacar(self, valor) -> bool:
        if valor > self.__saldo:
            return False
        return True

    def __str__(self) -> str:
        return f'R$ {self.__saldo:.2f}'

