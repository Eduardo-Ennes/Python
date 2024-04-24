from random import randint
from time import sleep
lista = list()
jogos = []
print('-=' * 30)
print('JOGO DA MEGA CENA')
print('-=' * 30)
quantidade = int(input('Quantos jogos deseja sortear:'))
quant = 1
while quant <= quantidade:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    quant += 1
print('-=' * 3, 'Sorteando jogos', '-=' * 3)
for i, c in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i + 1}: {c}')