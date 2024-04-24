n1 = int(input('Digite um número?'))
n2 = int(input('Digite um número?'))
soma = n1 + n2
if (soma%2) == 0:
    print('A soma dos números {} + {} = {} resulta em um número PAR'.format(n1,n2,soma))
else:
    print('A soma dos números {} + {} = {} resulta em um número ÍMPAR'.format(n1,n2,soma))