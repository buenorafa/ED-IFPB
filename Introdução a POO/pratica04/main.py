from calculadora import Calculadora

calc = Calculadora()
while True:
    print(f'''
    +-----------------------+
                    {calc}    
    +-----------------------+
    (+) somar
    (-) subtrair
    (/) dividir
    (*) multiplicar
    (r) resetar
    (d) desfazer
    (x) sair
    --------------------------
    ''')

    op = input('Operação: ')
    if (op == '+' or op == 'somar'):
        calc.soma(int(input('Valor: ')))
    elif (op == '-' or op == 'subtrair'):
        calc.subtrai(int(input('Valor: ')))
    elif (op == '/' or op == 'dividir'):
        calc.divide(int(input('Valor: ')))
    elif (op == '*' or op == 'multiplicar'):
        calc.multiplica(int(input('Valor: ')))
    elif (op == 'r' or op == 'resetar'):
        calc.reset()
    elif (op == 'd' or op == 'desfazer'):
        calc.desfazer()
    elif (op == 'x' or op == 'sair'):
        break
    else:
        print('Operação inválida!\n\n')
