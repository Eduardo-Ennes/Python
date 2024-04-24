km = float(input('Digite a quilometragem da viagem?'))
if km <= 200:
    v1 = km * 0.5
    print('O valor da sua viagem sairá por R${:.2f}'.format(v1))
else:
    v2 = km * 0.45
    print('O valor da sua viagem sairá por R${:.2f}'.format(v2))