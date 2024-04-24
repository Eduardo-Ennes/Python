import random
a1 = input('Digite o nome do(a) aluno?')
a2 = input('Digite o nome do(a) aluno?')
a3 = input('Digite o nome do(a) aluno?')
a4 = input('Digite o nome do(a) aluno?')
lista = [a1,a2,a3,a4]
sor = random.choice(lista)
print('O sorteado(a) foi {}'.format(sor))