def leiaint(msg):
    ok = False
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            ok = True
        else:
            print('ERRO! digite apenas números inteiros.')
        if ok:
            break
    return valor


num = leiaint('Digite um número inteiro: ')
print(f'Você digitou o número {num}')