from país import País
# TESTE
# a)
br = País('Brasil', 'Brasília', 8516000)
# b)
print(f'Nome: {br.nome}')
print(f'Capital: {br.capital}')
print(f'Dimensão: {br.dimensao} km2')
print()
# c)
br.adicionaNaFronteira('Uruguai')
br.adicionaNaFronteira('Colômbia')
br.adicionaNaFronteira('Paraguai')
print('Fronteira: ' + str(br.fronteira))
print()
# d)
print(br)
print()
# e)
print(br.fazFronteira('Japão'))
