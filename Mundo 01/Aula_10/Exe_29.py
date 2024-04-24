vel = float(input('Digite a velocidade?'))
multa = (vel - 80) * 7
if vel > 80:
    print('Você passou do limite permitido de 80km/h, sua velocidade foi {}km/h.'.format(vel))
    print('A multa custa R$7,00 por quilometro, você irá pagar uma multa de: R${:.2f}'.format(multa))
else:
    print('Tenha um boa dia e dirija com cuidado!')