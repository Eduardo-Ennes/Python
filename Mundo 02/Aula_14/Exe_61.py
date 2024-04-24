print('Gerador de PA')
n = int(input('Digite um número?'))
r = int(input('Digite um número?'))
cont = 1
termo = n
print(termo)
while cont <= 10:
    print('{} ->'.format(termo), end=' ')
    termo = termo + r
    cont = cont + 1