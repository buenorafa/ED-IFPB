from aluno import Aluno

# TESTE
aluno = Aluno('Rafael', 20231001)  # __init__

aluno.nome = 'Rafael Limeira'  # @setter
# c)
print(aluno.nome)  # get@property
print(aluno.matricula)  # get@property
print()
# getMatriculaFormatada
print(aluno.getMatriculaFormatada())
print()
# # f)
aluno.adicionar_nota(10)
aluno.adicionar_nota(10)
aluno.adicionar_nota(10)
# # d)
print(f'Média: {aluno.media()}')
