co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.1f}'.format(hi))



#OUTRA FORMA (RESOLUÇÃO DE HIPOTENUSA)/PODEMOS USAR TAMBEM 'FROM MATH IMPORT HYPOT.'
import math
co = float(input('Digite o cateto oposto:'))
ca = float(input('Digite o cateto adjacente:'))
hi = math.hypot(co,ca)
print('O valor da hipotenusa será: {:.2f}'.format(hi))