print('Digite quantos números quiser até 999.')
numero = cont = tot = 0
while numero != 999:
    numero = int(input('Digite um número:'))
    tot += numero
    cont += 1
    if numero == 999:
        soma = tot - 999
        print('\nO programa foi encerrado...\n'
            'Você digitou {} números\n'
            'E a soma entre eles = {}'.format(cont - 1, soma))
    if numero > 999:
        print('Apenas digite núemros até 999')
print('FIM DO PROGRAMA!')