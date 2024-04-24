print('Digite valores diferentes!')
a = int(input('Digite um valor?'))
b = int(input('Digite um valor?'))
c = int(input('Digite um valor?'))
maior = b
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('O maior número é {}.'.format(maior))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O menor número é {}.'.format(menor))