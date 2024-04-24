from random import randint
adv = randint (0,10)
print('Vamos brincar de advinha!!!\nEscolha um némero de 0 á 10.')
acertou = False
jogadas = 0
while not acertou:
    n = int(input('\nQual é o seu palpite?'))
    jogadas = jogadas + 1
    if n == adv:
        print('\nVOCÊ ACERTOU, PARABÉNS!')
        acertou = True
    if n < adv:
        print('\nVocê errou, tente novamente...')
        print('É um número MAIOR!')
    if n > adv:
        print('\nVocê errou, tente novamente...')
        print('é um número MENOR!')
print('VOCÊ PRECISOU DE {} CHANCES PARA ACERTAR.'.format(jogadas))