dic = dict()
lista = []
op = ' '
tot = quant = 0
while op not in 'Nn':
    dic.clear()
    dic['Nome'] = str(input('Digite o nome: '))
    dic['Idade'] = int(input('Digite a idade: '))
    quant += 1
    tot += dic['Idade']
    while True:
        dic['Sexo'] = str(input('Digite o sexo [M/F]: ')).upper()[0]
        if dic['Sexo'] in 'MF':
            break
        else:
            print('Digite apenas M ou F.')
    lista.append(dic.copy())
    while True:
        op = str(input('Deseja continuar [S/N]: ')).upper()[0]
        if op in 'NS':
            break
        else:
            print('Digito inváligo. Tente novamente.')
media = tot / quant
print('-=' * 30)
print(f'A) Foram cadastradas {len(lista)} pessoas')
print(f'B) A média de idade do grupo é {media:.2f}')
print('C) A mulheres cadastradas foram: ', end=' ')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p['Nome']}', end=', ')
print()
print('D) As pessoas com idade a cima da media são:')
for i in lista:
    if i['Idade'] > media:
        for m, k in i.items():
            print(f'{m} = {k}: ', end='')
        print()
print('>>>ENCERRADO<<<')