import math
n = float(input('Digite um número:'))
co = math.cos(math.radians(n))
tan =  math.tan(math.radians(n))
se = math.sin(math.radians(n))
print('O cosseno do número {} é: {:.2f}\nA tangente do número {} é: {:.2f}\nO seno do número {} é: {:.2f}'.format(int(n),co,int(n),tan,int(n),se))