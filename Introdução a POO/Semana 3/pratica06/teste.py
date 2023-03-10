class Aluno():
    # b) Construtor para inicializar todos os atributos
    def __init__(self, nome: str, matricula: int) -> None:
        # a) Atributo matricula, do tipo int; nome, do tipo String; notas do tipo list
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []

    # c) Métodos acessadores

    @property
    def nome(self):
        return self.__nome

    # e) Método alterador apenas para o nome, set_nome(self)
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def matricula(self):
        return self.__matricula

    # # f) Método adiciona_nota(self,nota),para adicionar uma nota à lista de notas, do aluno
    def adicionar_nota(self, nota: float):
        self.__notas.append(nota)

    # d) Método media(self) que retorna a media das notas
    def media(self) -> str:
        soma = 0
        for i in self.__notas:
            soma += i
        return soma/len(self.__notas)

    def __str__(self) -> str:
        return f'{self.__nome} - {self.__matricula}'


# TESTE
# b)
aluno = Aluno('Rafael', 20230101)
# print(aluno)
# e)
aluno.nome = 'Rafael Limeira'
# c)
print(aluno.nome)
print(aluno.matricula)
# # f)
aluno.adicionar_nota(10)
aluno.adicionar_nota(10)
aluno.adicionar_nota(10)
# # d)
print(f'Média: {aluno.media()}')
