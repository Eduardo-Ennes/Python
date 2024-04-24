print('Digite apenas números de 0 á 999.')
print('Digite 999 para o programa se encerrar.')
cont = soma = 0
while True:
    numero = int(input('Digite um número:'))
    if numero == 999:
        break
    elif numero > 999:
        soma -= numero
        cont -= 1
        print('Digito inválido...')
    soma += numero
    cont += 1
print(f'Foram digitados {cont} números e a soma entre eles é {soma}.')
print('FIM!')