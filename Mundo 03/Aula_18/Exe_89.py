ficha = []
while True:
    nome = str(input('Digite o nome: '))
    nota1 = float(input('Digite a nota1: '))
    nota2 = float(input('Digite a nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar: [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'{"Num.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 30)
for i,a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 30)
    print('999 interronpe o programa.')
    opc = int(input('De qual aluno deseja observar as notas?'))
    if opc == 999:
        break
    if opc <= len(ficha):
        print(f'O aluno(a) {ficha[opc][0]} são {ficha[opc][1]}')
print('\nA ESCOLINHA FEFE AGRADECE...')