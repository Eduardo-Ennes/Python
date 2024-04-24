alt = float(input('Digite a altura da parede:'))
lar = float(input('Digite a largura da parede:'))
area = alt * lar
tin = area / 2
print('Precisará de {} litro de tinta'.format(tin))
print('Sua area mede ao todo {} metros quadrados.\nDeverá ser utilizado {} listros de tinta em toda a area.'.format(area,tin))