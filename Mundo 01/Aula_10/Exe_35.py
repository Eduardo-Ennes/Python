print('Analisador de triângulos')
r1 = float(input('Digite o segmento:'))
r2 = float(input('Digite o segmento:'))
r3 = float(input('Digite o segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esses segmentos pode-se formar um triâgulo.')
else:
   print('Com esses valores não pode-se formar um triângulo.')