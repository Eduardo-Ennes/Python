from random import randint
computador = randint(0,5)
jogo = int(input('Digite um número?'))
if jogo == computador:
    print('Você ganhou!')
else:
    print('Voce perdeu!')
print(computador)