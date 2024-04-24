cont = 0
cont2 = 0
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
n3 = int(input('Digite outro número:'))
n4 = int(input('Digite outro número:'))
tupla = (n1, n2, n3, n4)
print(tupla)
print('-=' * 15)
for c in tupla:
    if c % 2 == 0:
        print(c, end=' ')
        cont += 1
print(f'Foram os valores pares.')
print(f'Temos {cont} números pares.')
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index(3) + 1}° posição.')
else:
    print('O valor 3 não foi digitado.')
print('FINAL DO PROGRAMA.')