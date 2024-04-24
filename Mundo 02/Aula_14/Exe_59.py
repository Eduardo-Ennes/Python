 n1 = int(input('Digite o 1° número?'))
 n2 = int(input('Digite o 2° número?'))
 opçao = 0
 while opçao != 5:
    print('''\n   [1] - SOMAR
    [2] - MULTIPLICAR
    [3] - MAIOR
    [4] - NOVOS NÚMEROS
    [5] - SAIR DOPROGRAMA''')
    print('Escolha uma das opções digitando o respectivo número.')
    opçao = int(input('\nDigite um número de 1 a 5?'))
    if opçao == 1:
        soma = n1 + n2
        print('\n{} + {} = {}'.format(n1, n2 , soma))
    elif opçao == 2:
        mul = n1 * n2
        print('\n{} x {} = {}'.format(n1, n2, mul))
    elif opçao == 3:
       if n1 > n2:
           print('\nO maior número é {}'.format(n1))
        elif n2 > n1:
            print('\nO maior número é {}'.format(n2))
        else:
            print('\nOs números são iguais.')
    elif opçao == 4:
        n1 = int(input('Digite o 1° número?'))
        n2 = int(input('Digite o 2e número?'))
    elif opçao == 5:
        print('\nFIM DO PROGRAMA...\nMUITO OBRIGADO!.')
    else:
       print('\nTente novamente...')