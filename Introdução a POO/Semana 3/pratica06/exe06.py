# 1.
class Data():
    # b) Construtor
    def __init__(self, dia: int, mes: int, ano: int = 2023) -> None:
        # a) Atributos privados
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # c) Métodos modificadores
    def setData(self, dia: int, mes: int, ano=2023):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    # d) Método __str__
    def __str__(self) -> str:
        return f'{self.__dia}/{self.__mes}/{self.__ano}'

# # TESTE:
# # b)
# data = Data(10, 7, 1998)
# print(data)
# # a, c)
# data.setData(22, 9, 1999)
# # d)
# print(data)


# 2.
class Aluno():
    # b) Construtor para inicializar todos os atributos
    def __init__(self, nome: str, matricula: int, notas: list) -> None:
        # a) Atributo matricula, do tipo int; nome, do tipo String; notas do tipo list
        self.nome = nome
        self.matricula = matricula
        if len(notas) > 3:
            self.notas = []
        self.notas = notas

    # c) Métodos acessadores
    @property
    def nome(self):
        return self._nome

    # e) Método alterador apenas para o nome, set_nome(self)
    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

    def get_matricula(self):
        return f'{self.matricula}'

    # d) Método media(self) que retorna a media das notas
    def media(self) -> str:
        if len(self.notas) < 3:
            return 'O aluno não possui média formada.'
        soma = 0
        for i in self.notas:
            soma += i
        return f'{soma/3}'

    # f) Método adiciona_nota(self,nota),para adicionar uma nota à lista de notas, do aluno
    def adiciona_nota(self, nota: int):
        if len(self.notas) < 3:
            self.notas.append(nota)

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula}'


# TESTE
# b)
aluno = Aluno('Rafael', 20230101, [10, 10,])
print(aluno)
# e)
aluno.nome = 'Rafael Limeira'
# c)
print(aluno.nome)
print(aluno.matricula)
# f)
aluno.adiciona_nota(10)
# d)
print(f'Média: {aluno.media()}')


# 3.
class País():
    # a) Construtor que inicialize o nome, capital e a dimensão do país
    def __init__(self, nome: str, capital: str, dimensao: float) -> None:
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteira = []

    # b) Métodos de acesso para os atributos indicados no item (a)
    def getNome(self) -> str:
        return f'{self.__nome}'

    def getCapital(self) -> str:
        return f'{self.__capital}'

    def getDimensao(self) -> float:
        return f'{self.__dimensao}'
    # c) Método que retorne a lista de países que fazem fronteira

    def getFronteira(self) -> list:
        return self.__fronteira

    # d) Método que adiciona o nome de país, a lista de fronteiras(verificar se o nome já existe na lista)
    def adicionaNaFronteira(self, nome: str) -> None:
        if nome not in self.__fronteira:
            self.__fronteira.append(nome)

    # e) Método __str__(self)
    def __str__(self) -> str:
        return f'País: {self.__nome}\nCapital: {self.__capital}\nDimensão: {self.__dimensao} km2\nPaíses na fronteira: {self.__fronteira}'

# # TESTE
# # a)
# br = País('Brasil', 'Brasília', 8516000)
# # b)
# print(f'Nome: {br.getNome()}')
# print(f'Capital: {br.getCapital()}')
# print(f'Dimensão: {br.getDimensao()} km2')
# print('Fronteira: ' + br.getFronteira())
# # d)
# br.adicionaNaFronteira('Uruguai')
# br.adicionaNaFronteira('Colômbia')
# br.adicionaNaFronteira('Paraguai')
# # c)
# print(br.getFronteira())
# # e)
# print(br)


# 4.
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


# # TESTE
# contas = []
# for i in range(2):
#     print(f'Cadastro do usuário #{i+1}:\n\n')
#     cc = input('Digite o numero da conta: ')
#     nome = input('Digite o nome do titular: ')
#     saldo = float(input('Digite o saldo: '))
#     print()
#     contas.append(ContaCorrente(cc, nome, saldo))

# while True:
#     print('''
# Opções disponíveis:

# 1 - Depositar
# 2 - Sacar
# 3 - Saldo
# 4 - Sair

#     ''')
#     op = input('Digite o sua opção: ')
#     if op == '1':
#         cc = input('\nDigite o numero da conta: ')
#         for i in contas:
#             if cc == i.getConta():
#                 valor = float(input('\nDigite o valor a ser depositado: '))
#                 i.depositar(valor)
#     elif op == '2':
#         cc = input('\nDigite o numero da conta: ')
#         v_saque = float(input('\nDigite o valor do saque: '))
#         for i in contas:
#             if cc == i.getConta():
#                 status = i.sacar(v_saque)
#                 print('\nSaque realizado com sucesso!') if status else print(
#                     '\nSaldo insuficiente.')
#     elif op == '3':
#         cc = input('\nDigite o numero da conta: ')
#         for i in contas:
#             if cc == i.getConta():
#                 print(f'\n{i.getTitular()}\t-\t{i.getConta}\n\n\n{i}')
#     elif op == '4':
#         break
