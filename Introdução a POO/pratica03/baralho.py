from carta import Carta
import random


class Baralho():
    def __init__(self):
        self.NAIPES = ["Paus", "Ouro", "Copas", "Espadas"]
        self.NUMEROS = ["As", "2", "3", "4", "5", "6", "7",
                        "8", "9", "10", "Valete", "Dama", "Rei"]
        self.cartas = []
        for i in self.NAIPES:
            for j in self.NUMEROS:
                self.cartas.append(Carta(j, i))

    def embaralha(self) -> None:
        random.shuffle(self.cartas)

    def retira_carta(self) -> Carta:
        return self.cartas.pop()

    # Classe idealizada na aula, mas não é necessária para este exercício
    def adiciona_carta(self, numero: str, naipe: str) -> None:
        mensagem = ''
        if (numero in self.NUMEROS and naipe in self.NAIPES):
            carta = Carta(numero, naipe)
            if carta in self.cartas:
                self.cartas.insert(0, carta)
                mensagem = 'Carta adicionada com sucesso'
            else:
                mensagem = 'Está cartá já existe no baralho e não pode ser adicionada!'
        else:
            mensagem = 'Carta inválida!'
        print(mensagem)

    # Imprime as quatro colunas de forma ordenada quando o baralho não estiver embaralhado
    def __str__(self) -> str:
        s = ''
        for carta in range(13):  # 13 é o numero de cartas de cada naipe
            s += f'{self.cartas[carta].__str__()}\t{self.cartas[carta+13]}\t{self.cartas[carta+26].__str__()}\t{self.cartas[carta+39]}\n'
        return s
