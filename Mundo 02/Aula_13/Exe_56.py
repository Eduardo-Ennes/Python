media_idade = 0
maioridade = 0
nomevelho = ''
idademulher = 0
mulheres = 0
for p in range (0,4):
   nome = str(input('Qual é o seu nome?')).strip()
   idade = int(input('Qual é a sua idade?'))
   sexo = str(input('Qual é o seu sexo (M/F)?')).capitalize().strip()
   print('____________________________')
   media_idade = media_idade + idade
   if p == 1 and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
   if sexo in 'Mm' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
   if sexo in 'Ff' and idade < 18:
        mulheres += 1
        idademulher += 1
c1 = media_idade / 4
print('A média de idade do grupo é de {} anos'.format(c1))
print('O homem mais velho tem {} e se chama {}'.format(maioridade,nomevelho))
print('No grupo á {} mulher(s) e {} tem menos de 18 anos'.format(mulheres,idademulher))