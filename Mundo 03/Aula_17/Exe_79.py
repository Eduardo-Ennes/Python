numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não será adicionado.')
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'nN':
        break
print('-=' * 25)
print(f'Você digitou os valores {numeros.sort(numeros)}')