nome = str(input('Digite seu nome completo?')).strip()
print('Prazer em te conhecer cuzão')
div = nome.split()
print('O primeiro nome é: {}'.format(div[0]))
print('O útimo nome é {}'.format(div[len(div) - 1]))