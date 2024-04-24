maior = 0
menor = 0
for p in range (0,6):
    peso = float(input('Digite o peso da pessoa?'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}'.format(maior))
rint('O menor peso lido foi {}'.format(menor))