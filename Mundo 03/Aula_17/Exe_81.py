lista = []
opçao = ' '
while opçao != 'Nn':
    numero = int(input('\nDigite um número:'))
    if numero in lista:
        print('O número já foi digitado...')
    else:
        print('Adicionado com sucesso!')
        lista.append(numero)
    opçao = str(input('Deseja continuar: [S/N]'))
    if opçao in 'nN':
        break
print('-=' * 30)
print('FIM DO PROGRAMA...')
print(f'Foram digitados {len(lista)} números')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
lista.sort(reverse=True)
print(f'Assim ficou a lista de forma decrescente: {lista}')
print('MUITO OBRIGADO PELA SUA COLABORAÇÃO...')