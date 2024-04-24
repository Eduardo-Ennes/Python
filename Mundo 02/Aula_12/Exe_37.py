num = int(input('Digite um número?'))
print('''Em seguida escolha entre as opções para ver a forma do número digitado.
{1} para binario
{2} para octal
{3} para hexadecimal''')
opçao = int(input('Digite uma opção?'))
if opçao == 1:
    print('A forma binária do número {} é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('A forma do número {} em octal é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('A forma hexadecimal do número {} é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente...')