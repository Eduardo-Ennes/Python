pro = float(input('Digite o valor do produto? R$'))
print('''Selecione a forma de pagamento.
[1] dinheiro com 10% de desconto.
[2] Á vista no cartão com 5% de desconto.
[3] Em até 2x no cartão.
[4] 3x ou mais no cartão com 20% de juros.''')
cash = int(input('Digite a forma de pagamento?'))
if cash == 1:
    c1 = pro - (pro * 0.10)
    print(f'''O valor do produto é R${pro}.
   Conforme a opção de pagamento escolhida, será de R${c1} com 10% de desconto.''')
elif cash == 2:
    c2 = pro - (pro * 0.05)
    print(f'''O valor do produto é R${pro}.
    Conforme a opção de pagamento escolhida, será de R${c2} com 5% de desconto.''')
elif cash == 3:
    c3 = pro / 2
    print(f'''O valor do produto é R${pro}.
    Conforme a forma de pagamento escolhida, Será parcelado em 2x o valor de R${c3}''')
elif cash == 4:
    c4 = pro + (pro * 0.20)
    print('Logo em seguida escolha o número de parcelas, no mínimo 3x e no maximo 12x.')
    par = int(input('Digite o número de parcelas?'))
    c5 = c4 / par
    print(f'''O valor do produto é R${pro}.
    Conforme a forma de pagamento escolhida, o produto sairá com 20% de juros.
    Com o parcelamento de {par}x o valor das parcelas será de R${c5}.''')