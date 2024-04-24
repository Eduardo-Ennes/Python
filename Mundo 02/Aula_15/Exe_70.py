from time import sleep
maior = menor = 0
totalcompra = promil = cont = 0
maisbarato = ' '
print('-' * 15, 'LOJA DO FEFE', '-' * 15)
while True:
    produto = str(input('Digite o nome do produto?')).strip()
    preco = float(input('Digite o preço do produto?'))
    totalcompra += preco
    cont += 1
    if preco > 1000:
        promil += 1
    if cont == 1:
        menor = preco
        maisbarato = produto
    else:
        if preco < menor:
            menor = preco
            maisbarato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar?')).strip().upper()[0]
        print('-' * 30)
    if resp == 'N':
        print('O programa está se encerrando...')
        sleep(1)
        break
print(f'O valor total da compra foi R${totalcompra}')
print(f'({promil}) produtos acima de R$1000.00')
print(f'O produto mais barato é ({maisbarato}) e custa R${menor}')
print(sleep(1))
print('VOLTE SEMPRE A LOJINHA DO FEFE!')