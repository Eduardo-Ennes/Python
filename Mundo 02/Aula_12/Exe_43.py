print('Digite os números da mesma forma dos exemplos a seguir. \nPor exemplo: \nPeso = 75 \nAltura = 1.70')
peso = float(input('Digite o seu peso?'))
altura = float(input('Digite a sua altura?'))
calculo = peso / altura**2
print(f'Seu imc é {calculo}')
if calculo < 18.5:
    print('Seu peso é {}kg, sua altura {:.2f}m e o imc é de {:.2f}kg/m². Tome cuidado, você está abaixo do peso.'.format(peso,altura,calculo))
elif calculo >= 18.5 and calculo <= 25.0:
   print('Seu peso é {}kg, sua altura {:.2f}m e o imc é de {:.2f}kg/m². Que ótimo, seu peso está otimo, continue assim.'.format(peso,altura,calculo))
elif calculo > 25.0 and calculo <= 30.0:
    print('Seu peso é {}kg, sua altura {:.2f}m e o imc é de {:.2f}kg/m². Tome cuidado, sua sitiação é de sobrepeso.'.format(peso,altura,calculo))
elif calculo > 30.0 and calculo <= 40.0:
    print('Seu peso é {}kg, sua altura {:.2f}m e o imc é de {:.2f}kg/m². Tome cuidado, sua situação é de obesidade.'.format(peso,altura,calculo))
elif calculo > 40.0:
    print('Seu peso é {}kg, sua altura {:.2f}m e o imc é de {:.2f}kg/m². Tome cuidado, sua situação e de obesidade morbida.'.format(peso,altura,calculo))