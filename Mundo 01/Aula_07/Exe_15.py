km = float(input('Digite a quilometragem percorrida?'))
dia = int(input('Digite o quantidade de dias que ficou com carro?'))
v1 = 0.15 * km
v2 = 60 * dia
v3 = v1 + v2
print('Os respectivos valores a serem cobrados por rodar {:.1f}km e {} dias, será: R${:.2f}'.format(km,dia,v3))



#OUTRA FORMA
dias = int(input('Digite o número de dias?'))
km = float(input('Digite o número de km?'))
pagar = (dias * 60) + (km * 0.15)
print('Com os respectivos gastos em {}km e {:.1f} dias, o valor do aluguel do carro custará: R${:.2f}'.format(km,dias,pagar))