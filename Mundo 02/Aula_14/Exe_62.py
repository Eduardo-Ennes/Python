print('Gerador de PA')
n = int(input('Digite um número?'))
r = int(input('Digite um número?'))
cont = 1
termo = n
total = 0
mais = 10
print(termo)
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} ->'.format(termo), end=' ')
        termo = termo + r
        cont = cont + 1
    mais = int(input('\nQuantos termos deseja visualizar mais?'))
print('FIM!')