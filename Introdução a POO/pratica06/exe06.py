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

# # TESTE
# # b)
# aluno = Aluno('Rafael', 20230101, [10, 10,])
# print(aluno)
# # e)
# aluno.nome = 'Rafael Limeira'
# # c)
# print(aluno.nome)
# print(aluno.matricula)
# # f)
# aluno.adiciona_nota(10)
# # d)
# print(f'Média: {aluno.media()}')


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


# TESTE
# a)
br = País('Brasil', 'Brasília', 8516000)
# b)
print(f'Nome: {br.getNome}')
print(f'Capital: {br.getCapital}')
print(f'Dimensão: {br.getDimensao} km2')
print()
print(br.getFronteira)
# d)
br.adicionaNaFronteira('Uruguai')
br.adicionaNaFronteira('Colômbia')
br.adicionaNaFronteira('Paraguai')
# c)
print(br.getFronteira)
# e)
print(br)
