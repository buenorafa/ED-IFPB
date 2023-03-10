from contaCorrente import ContaCorrente

contas = []
# a) Escreva um programa para criar dez instâncias de ContaCorrente, armazenando-os em uma list. Os valores para inicialização dos objetos poderão ser lidos a partir do teclado ou povoados automaticamente.

# for i in range(2):
#     print(f'Cadastro do usuário #{i+1}:\n\n')
#     cc = input('Digite o numero da conta: ')
#     nome = input('Digite o nome do titular: ')
#     saldo = float(input('Digite o saldo: '))
#     print()

contas.append(ContaCorrente('001', 'Rafael', 0))
contas.append(ContaCorrente('002', 'Victor', 10000000))

# b) Após povoamento do list de contas corrente, disponibilize um menu de operações para o usuário. Em um loop, o programa ficara solicitando ao usuário, qual a operação ele deseja realizar
while True:
    print('''
Opções disponíveis:

1 - Depositar
2 - Sacar
3 - Saldo
4 - Sair

    ''')
    op = input('Digite o sua opção: ')
    if op == '1':
        cc = input('\nDigite o numero da conta: ')
        for i in contas:
            if cc == i.getConta():
                valor = float(input('\nDigite o valor a ser depositado: '))
                i.depositar(valor)
    elif op == '2':
        cc = input('\nDigite o numero da conta: ')
        v_saque = float(input('\nDigite o valor do saque: '))
        for i in contas:
            if cc == i.getConta():
                status = i.sacar(v_saque)
                print('\nSaque realizado com sucesso!') if status else print(
                    '\nSaldo insuficiente.')
    elif op == '3':
        cc = input('\nDigite o numero da conta: ')
        for i in contas:
            if cc == i.getConta():
                print(f'\n{i.getTitular()}\t-\t{i.getConta}\n\n\n{i}')
    elif op == '4':
        break
