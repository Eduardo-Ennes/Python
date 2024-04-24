print('-' * 15, 'BANCO DO FEFE', '-' * 15)
dinheiro = int(input('Quanto você quer sacar? R$'))
total = dinheiro
cedula = 50
totalced = 0
while True:
    if total >= cedula:
        total -= cedula
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalced = 0
        if total == 0:
            break
print('-' * 30)
print('O BANCO FEFE AGRADECE. TENHA UM BOM DIA!')