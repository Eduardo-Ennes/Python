print('Digite 0 para encerrar o programa!')
while True:
    numero = int(input('Digite um número para observar a sua tabuada:'))
    print('-' * 30)
    if numero == 0:
        break
    for indice in range(1, 11):
        print('{} x {} = {}'.format(indice, numero, indice * numero))
    print('-' * 30)
print('FIM DO PROGRAMA, MUITO OBRIGADO.')