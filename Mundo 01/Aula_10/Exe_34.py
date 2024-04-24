s = float(input('Digite um valor?'))
if s <= 5000:
    r1 = (s * 0.10) + s
    print('Seu salário que era R${:.2f} passou a ser R${:.2f} com o reajuste de 10%'.format(s,r1))
else:
    r2 = (s * 0.05) + s
    print('Seu salário que era R${:.3f} passou a ser R${:.3f} com o reajuste de 5%'.format(s,r2))