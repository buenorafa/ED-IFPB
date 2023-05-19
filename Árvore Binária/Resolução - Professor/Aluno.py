class Aluno:
    def __init__(self, matricula, nome, cre):
        self.matricula = matricula
        self.nome = nome
        self.cre = cre
    
    def __str__(self)->str:
        return f'{self.matricula}-{self.nome}:{self.cre}'

    def __eq__(self, outroAluno:'Aluno'):
        return self.matricula == outroAluno.matricula
