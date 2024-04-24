from math import factorial
print('Digite o número para descobrir o seu fatorial.')
n = int(input('Digite um número?'))
fac = factorial(n)
print('O fatorial de {} é {}'.format(n,fac))



#OUTRA FORMA
from math import factorial
n = int(input('Digite um número para ver o seu fatorial?'))
c = n
print('Calculando o fatorial de {}!'.format(n))
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ' , end = ' ')
    f = factorial(n)
    c = c - 1
print('{}'.format(f))