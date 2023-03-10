from carta import Carta
from baralho import Baralho

num_jogadores = int(input('Digite o numero de jogadores (De 1 a 6): '))

if (num_jogadores < 1 or num_jogadores > 6):
    print('O programa encerrou pq tu é muito burro!')
else:
    # Cria o objeto da classe Baralho
    baralho = Baralho()
    print(f'Baralho:\n{baralho}')
    # Numero de cartas por jogador
    num_cartas = len(baralho.cartas) // num_jogadores

    for i in range(num_jogadores):
        # Chama a função de embaralhar p/ cada jogador
        baralho.embaralha()
        print(f'Jogador #{i+1}:')
        for j in range(num_cartas):
            cartas_do_jogador = baralho.retira_carta()
            print(f'\t{cartas_do_jogador.__str__()}')
        print()
