class Aluno():
    # b) Construtor para inicializar todos os atributos
    def __init__(self, nome: str, matricula: int) -> None:
        # a) Atributo matricula, do tipo int; nome, do tipo String; notas do tipo list
        self.__nome = nome
        # :c - Verifica
        while len(str(matricula)) != 8:
            matricula = input('O tamanho da matrícula deve ter 8 digitos: ')
            if len(matricula) == 8:
                matricula = int(matricula)
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

    # e) criar o método getMatriculaFormatada(self) para devolver a matrícula no seguinte formato: '2023.1.050'
    def getMatriculaFormatada(self):
        mat = str(self.matricula)
        return f'{mat[:4]}.{mat[4]}.{mat[5:]}'

    # f) Método adiciona_nota(self,nota),para adicionar uma nota à lista de notas, do aluno
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
