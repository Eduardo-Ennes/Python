nome = input('Digite o seu nome?')
salario = float(input('Digite o seu salário?'))
casa = float(input('Digite o valor da casa?'))
parcela = int(input('Digite o número de anos da parcela desejada?'))
meses = parcela * 12
v1 = (casa / (parcela * 12))
p2 = (salario + (salario * 0.3)) - salario
if v1 > p2:
    print('Ola Sr(a) {}, Devido ao valor da parcela ser maior que 30% do seu salário, não poderemos realizar uma parcelar com esse valor.'.format(nome))
else:
    print('Olá Senhor(a) {}, seu parcelamento foi aprovado com parcelas no valor de R${:.2f} e com duração de {} meses'.format(nome, v1 , meses))
print('Muito obrigado pela preferência senhor(a) {}, sempre estaremos a disposição.'.format(nome))