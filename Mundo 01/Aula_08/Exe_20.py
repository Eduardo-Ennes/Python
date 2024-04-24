import random
a1 = input('Digite o nome do aluno(a)?')
a2 = input('Digite o nome do aluno(a)?')
a3 = input('Digite o nome do aluno(a)?')
a4 = input('Digite o nome do aluno(a)?')
li = [a1,a2,a3,a4]
random.shuffle(li)
print('A ordem de apresentaçaõ será:')
print(li)