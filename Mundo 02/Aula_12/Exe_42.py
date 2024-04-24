l1 = float(input('Digite um número?'))
l2 = float(input('Digite um número?'))
l3 = float(input('Digite um número?'))
if (l1 + l2 < l3) or (l1 + l3 < l2) or (l3 + l2 < l1):
    print('Não podem formar um triângulo.')
elif l1 == l2 and l3 and l2 == l3 and l1 and l3 == l2 and l1:
    print('É um triângulo equilatero.')
elif l1 != l2 != l3 != l1:
    print('é um triângulo isosceles.')
else:
    print('É um triângulo escaleno.')