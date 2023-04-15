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

# Marcação de consulta


class Paciente:
    def __init__(self, nome: str, tempo_atendimento_minutos: int, especialidade: str):
        self.__nome = nome
        self.__tempo_atendimento_minutos = tempo_atendimento_minutos
        self.__especialidade = especialidade

    @property
    def nome(self):
        return self.__nome

    @property
    def tempo(self):
        return self.__tempo_atendimento_minutos

    @property
    def especialidade(self):
        return self.__especialidade

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nTempo: {self.tempo}\nEspecialidade: {self.especialidade}'


class Marcacao:
    def __init__(self, tempo_max: int):
        self.fila = Fila()
        self.tempo_max = tempo_max  # em minutos
        self.tempo_total = 0

    def addPaciente(self, paciente: Paciente) -> bool:
        if self.tempo_total < self.tempo_max:
            # nome = input('Nome: ')
            # tempo = int(input('Tempo: '))
            # especialidade = input('Especialidade: ')
            # novoPaciente = Paciente(nome, tempo, especialidade)
            self.fila.enfileira(paciente)
            self.tempo_total += paciente.tempo
            return True
        return False

    def cancelarAgendamento(self, especialidade: str):
        for i in range(len(self.fila)):
            pcte = self.fila.desenfileira()
            self.tempo_total -= pcte.tempo
            if pcte.especialidade != especialidade:
                self.addPaciente(pcte)


# # Teste
# # pcte = Paciente('Rafael', 20, 'CG')
# # print(pcte)
# fila_marc = Marcacao(60)
# print(fila_marc.addPaciente(Paciente('Rafael', 20, 'Psiquiatra')))
# print(fila_marc.addPaciente(Paciente('Milena', 20, 'Psiquiatra')))
# print(fila_marc.addPaciente(Paciente('Lola', 20, 'CG')))
# print(fila_marc.tempo_total)
# fila_marc.cancelarAgendamento('Psiquiatra')
# print(fila_marc.tempo_total)
