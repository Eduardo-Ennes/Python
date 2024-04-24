from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor:'))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '                                      # ---> Deve-se sempre dar um valor a str mesmo que seja um espaço
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I]')).strip().upper()
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total} =', end='')
    print(' DEU PAR' if total % 2 == 0 else ' DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
print('Vamos jogar novamente...')
print(f'GAME OVER! você venceu {v} vezes')