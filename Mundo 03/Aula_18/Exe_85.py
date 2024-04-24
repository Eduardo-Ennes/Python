lista = [[], []]
numero = 0
for c in range(0,7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)
print('-=' * 30)
print(f'{sorted(lista[0])} temos {len(lista[0])} elementos na lista.')
print(f'{sorted(lista[1])} temos {len(lista[1])} elementos na lista.')
print('MUITO OBRIGADO!!!')