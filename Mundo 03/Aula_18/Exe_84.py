lista = list()
pes = list()
maior = menor = 0
while True:
    pes.append(str(input('Digite um nome:')))
    pes.append(float(input('Digite um peso:')))
    if len(lista) == 0:
        maior = menor = pes[1]
    else:
        if pes[1] > maior:
            maior = pes[1]
        if pes[1] < menor:
            menor = pes[1]
    lista.append(pes[:])
    pes.clear()
    op = str(input('deseja continuar: [S/N]'))
    if op in 'Nn':
        break
print('\n-=' * 30)
print(f'Foram {len(lista)} pessoas cadastradas')
print(f'O maior peso foi {maior}kg --> ',end='')
for p in lista:
    if p[1] == maior:
        print(f'{p[0]} ',end=', ')
print()
print(f'O menor peso foi {menor}kg --> ',end='')
for p in lista:
    if p[1] == menor:
        print(f'{p[0]}',end=', ')