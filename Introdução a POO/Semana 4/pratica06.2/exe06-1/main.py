from data import Data
# TESTE:
# b)
data = Data(10, 7, 1998)
print(data)  # __str__
# c) @gets e @sets
print()
data.dia = 300  # dia inválido, então a data não deve mudar
print(data.dia)
data.mes = -12  # mes inválido, então a data não deve mudar
print(data.mes)
print()
# e) setData
data.setData(22, 9, 1999)
# d)
print(data)  # __str__
