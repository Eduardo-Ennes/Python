lista = ('lapís', 10.00,
        'caneta', 15.00,
        'mochila', 150.00,
        'bagagem', 300.00,
        'cachicol', 45.00,
        'chocolate', 5.00)
print('-' * 30)
print('LISTA DE PREÇOS DA LOJA DO FEFE')
print('-' * 30)
for pos, c in enumerate(lista):
    if pos % 2 == 0:
        print(f'{c}', end='')
        print('.' * 15, end='R$ ')
    if pos % 2 != 0:
        print(f'{c}')