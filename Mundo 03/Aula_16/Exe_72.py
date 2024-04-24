lista = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartorze', 'quize',
        'dezesseis', 'dezessete', 'dezoite', 'dezenove', 'vinte')
n = int(input('Número: '))
if n < 0 or n > 20:
    print('Digite um número de 0 a 20.')
else:
    print(f'Você digitou o número: {lista[n]}')