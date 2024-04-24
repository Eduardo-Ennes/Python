from Aula_22 import numero
while True:
    try:
        n = int(input('Digite um número inteiro: '))
    except:
        print('Digite apenas número inteiro.')
        print()
    else:
        # número.inteiro(n)
        break

while True:
    try:
        num = float(input('Digite um número real: '))
    except:
        print('Apenas digite número real.')
        print()
    else:
        # número.real(num)
        break
print(f'\nO valor inteiro foi = {n}')
print(f'O valor real foi = {num}')



# OUTRA FORMA
def inteiro(msg):
    while True:
        try:
            valor = int(input(msg))
        except:
            print('Digitr apenas números inteiros.')
        else:
            return valor


def real(n):
    while True:
        try:
            valor = float(input(n))
        except:
            print('Digite apenas números reais. ')
        else:
            return valor


n = inteiro('Digite um valor inteiro: ')
num = real('Digite um número real: ')
print('-=' * 30)
print(f'Inteiro = {n}')
print(f'Real = {num}')