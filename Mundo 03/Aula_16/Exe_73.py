tabela = ('botafogo', 'palmeiras', 'bragrantino', 'grêmio', 'flamengo', 'atlético-mg',
        'atlético-pr', 'fluminense', 'fortaleza', 'cuiaba', 'são paulo', 'internacional',
        'cruzeiro', 'corinthians', 'bahia', 'santos', 'goias',
        'vasco', 'coritiba', 'america-mg')
opção = ' '
while opção != 'N':
    print('-' * 30)
    print(f'Os times do g4 são ({tabela[0:4]})')
    print('-' * 30)
    print((f'Os times que estão na zona de rebaixamento são ({tabela[-4:]})'))
    print('-' * 30)
    print(f'Times em ordem alfabéticas ({sorted(tabela)})')
    print('-' * 30)
    posição = int(input('Digite a colocação:'))
    print(f'O time que ocupa a {posição}° colocação é o {tabela[posição - 1]}')
    print('-' * 30)
    print('Digite o nome do time para observar sua colocação na tabela.')
    time = str(input('Digite o time:'))
    print(f'O {time} está na {tabela.index(time) + 1}° colocação')
    opção = str(input('Deseja continuar?')).strip().upper()[0]
print('O PROGRAMA SE ENCERROU...')