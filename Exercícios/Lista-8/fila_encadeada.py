class No:
    # Metodo construtor
    def __init__(self, carga) -> None:
        self.__carga = carga
        self.__prox = None

    @property
    def carga(self):
        return self.__carga

    @property
    def prox(self) -> 'No':
        return self.__prox

    @prox.setter
    def prox(self, no) -> None:
        self.__prox = no

    def temProx(self) -> bool:
        return self.__prox != None

    def __str__(self) -> str:
        return str(self.__carga)


class Head:
    def __init__(self) -> None:
        self.__inicio = None
        self.__final = None
        self.__tamanho = 0

    @property
    def inicio(self):
        return self.__inicio

    @inicio.setter
    def inicio(self, novoNo):
        self.__inicio = novoNo

    @property
    def final(self):
        return self.__final

    @final.setter
    def final(self, novoNo):
        self.__final = novoNo

    @property
    def tamanho(self):
        return self.__tamanho

    @tamanho.setter
    def tamanho(self, novoTamanho):
        self.__tamanho = novoTamanho


class FilaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)


class Fila:
    def __init__(self) -> None:
        self.__head = Head()

    def estaVazia(self):
        return self.__head.tamanho == 0

    def enfileira(self, value):
        novoNo = No(value)
        if self.estaVazia():
            self.__head.inicio = self.__head.final = novoNo
        else:
            self.__head.final.prox = novoNo
            self.__head.final = novoNo
        self.__head.tamanho += 1

    def desenfileira(self):
        if self.estaVazia():
            raise FilaException('A fila está fazia.')
        elemento = self.__head.inicio.carga
        if self.__head.tamanho == 1:
            self.__head.final = None
        self.__head.inicio = self.__head.inicio.prox
        self.__head.tamanho -= 1
        return elemento

    def busca(self, elem):
        index = self.__head.inicio
        contador = 1
        while index != None:
            if index.carga == elem:
                return contador
            index = index.prox
            contador += 1
        if index == None:
            raise FilaException('Elemento não existe na fila.')

    def elemento(self, num):
        if self.__head.tamanho < num or num <= 0:
            raise FilaException('Posição inválida.')
        contador = 1
        cursor = self.__head.inicio
        while cursor != None:
            if contador == num:
                return cursor.carga
            cursor = cursor.prox
            contador += 1

    def __len__(self):
        return self.__head.tamanho

    def __str__(self) -> str:
        res = 'inicio -> ['
        cursor = self.__head.inicio
        while cursor != None:
            res += f'{cursor.carga}'
            if cursor.prox != None:
                res += ', '
            cursor = cursor.prox
        res += '] <- fim'
        return res
    # COMBINA SEM REMOVER OS ELEMENTOS
    # @classmethod
    # def combina(cls, f_res, f1, f2) -> None:
    #     tamanho = max(len(f1), len(f2))
    #     contador = 1
    #     while contador <= tamanho:
    #         if f1.elemento(contador) != None:
    #             f_res.enfileira(f1.elemento(contador))
    #         if f2.elemento(contador) != None:
    #             f_res.enfileira(f2.elemento(contador))
    #         contador += 1

    # # COMBINA REMOVENDO TODOS OS ELEMENTOS
    # @classmethod
    # def combina(cls, f_res, f1, f2):
    #     tamanho = max(len(f1), len(f2))
    #     for i in range(tamanho):
    #         try:
    #             f_res.enfileira(f1.desenfileira())
    #             f_res.enfileira(f2.desenfileira())
    #         except FilaException:
    #             continue
    @classmethod
    def combina(cls, f_res, f1, f2):
        tamanho = max(len(f1), len(f2))
        for i in range(tamanho):
            if not f1.estaVazia():
                f_res.enfileira(f1.desenfileira())
            if not f2.estaVazia():
                f_res.enfileira(f2.desenfileira())


# Testes

f1 = Fila()
f1.enfileira(1)
f1.enfileira('Oi')
f1.enfileira(':P')
f1.enfileira(':)')
print(f1)

# # Encontra elemento
# print(f1.elemento(1))

# Busca na fila
# print(f1.busca('Faz o L'))
# print(f1.busca('Oi'))

# Combina método de classe
f2 = Fila()
f2.enfileira(2)
f2.enfileira('Tchau')
f_res = Fila()
f_res.enfileira(1)
Fila.combina(f_res, f1, f2)
print(f_res)
print(f1)
print(f2)

# # Clinica médica
# fila_de_espera = Fila()
# atendidos = 0
# while True:
#     print('''
# Clinica Medica - Atendimento
# =============
# 1. Incluir paciente
# 2. Realizar chamada
# 3. Consultar a posição atual
# 4. Listar a quantidade de pacientes atendidos
# 5. Sair
#     ''')
#     op = input('')
#     if op == '1':
#         pcte = input('Nome: ')
#         fila_de_espera.enfileira(pcte)
#     elif op == '2':
#         try:
#             fila_de_espera.desenfileira()
#             atendidos += 1
#         except FilaException as fe:
#             print(fe)
#     elif op == '3':
#         consulta = input('Nome: ')
#         try:
#             print(f'Posição: {fila_de_espera.busca(consulta)}')
#         except FilaException:
#             print('Paciente não está na fila.')
#     elif op == '4':
#         print(f'Atendidos: {atendidos}')
#     else:
#         break

# # Rei do mocotó (Nessa eu nem utilizei try catch, mas a ideia geral é essa)
# pedidos = Fila()
# pagamento = Fila()
# retirada = Fila()
# atendidos = 0
# while True:
#     print(f'''
#     Rei do Mocotó
#     =============
#     A. Inserir na fila de pedidos
#     B. Remover da fila de pedidos
#     C. Remover da fila de pagamento
#     D. Remover da fila de retirada
#     X. Sair


#     Pedidos: {pedidos}
#     Pagamento: {pagamento}
#     Retirada: {retirada}
#     Atendidos = {atendidos}

#         ''')
#     op = input('')
#     if op == 'a' or op == 'A':
#         nome = input('Nome: ')
#         pedidos.enfileira(nome)
#     elif op == 'b' or op == 'B':
#         pagamento.enfileira(pedidos.desenfileira())
#     elif op == 'c' or op == 'C':
#         retirada.enfileira(pagamento.desenfileira())
#     elif op == 'd' or op == 'D':
#         retirada.desenfileira()
#         atendidos += 1
#     else:
#         break

# 4.
# a) Fila
# b) Pilha
# c) Fila
