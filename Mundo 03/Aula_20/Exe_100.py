import random
def sorteia(lista):
    for cont in range(0, 5):
        lista.append(random.randint(0, 10))
    print(f'Sorteando {len(lista)} números na lista {lista}')
def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares = {soma}')

numeros = list()
sorteia(numeros)
somapar(numeros)