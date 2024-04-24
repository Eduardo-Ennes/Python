ficha = dict()
ficha['Nome'] = str(input('Digite o nome: '))
ficha['Nota'] = float(input('Digite a nota: '))
print('-=' * 30)
print(f'O(A) {ficha["Nome"]}')
print(f'A Nota foi {ficha["Nota"]}')
if ficha["Nota"] < 4:
    print('Situação = Reprovado')
if ficha["Nota"] >= 4 and ficha["Nota"] < 7:
    print('Situação = Recuperação')
if ficha["Nota"] > 7:
    print('Situação = Aprovado')