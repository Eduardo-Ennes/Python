print('Digite um número para obeservar se ele é primo.')
num = int(input('Digite um número?'))
tot = 0
for c in range (1 , num + 1):
   if num % c == 0:
       print('\033[33m', end = ' ')
       tot = tot + 1
   else:
       print('\033[31m', end = ' ')
   print('{}'.format(c), end = ' ')
print(f'\n\033[mO número {num} foi divisivel por {tot} números.')
if tot == 2:
   print(f'O {num} é primo')
else:
   print(f'O {num} não é primo')