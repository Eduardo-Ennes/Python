v1 = float(input('Digite o valor do salário:'))
por = v1 * 0.15
aum = v1 + por
print('O saláro com aumento de 15% fica:R$',aum)



#OUTRA FORMA
salario = float(input('Digite o salario:R$'))
aumento = salario + (salario * 15 / 100)
print('O salario que era R${:.3f} com o aumento de 15% passa a ser R${:.3f}'.format(salario,aumento))