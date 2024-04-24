lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range (0, 3):
    for c in range(0, 3):
        lista[l][c] = int(input(f'Digite um valor para [{l, c}]:'))
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        if lista[l][c] % 2 == 0:
            cont += lista[l][c]
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{lista[l][c]:^5}]', end='')
    print()
cont2 = 0
for v in lista[2]:
    cont2 += v
maior = menor = 0
for valor in lista[1]:
    if len(lista[1]) == 0:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor
print('-=' * 30)
print(f'A soma de todos os valores pares digitados é {cont}')
print(f'A 3° coluna é {lista[2]} e a soma de seu valores é [{cont2}]')
print(f'A 2° linha é {lista[1]} e o maior valor é {maior}')