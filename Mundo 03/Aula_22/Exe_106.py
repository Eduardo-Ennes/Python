import numero
valor = float(input('Digite um valor: R$'))
print('-=' * 30)
print(f'A metade de {valor} é R${numero.metade(valor)}')
print(f'O dobro de {valor} é R${numero.dobro(valor)}')
print(f'Aumentando 10% é R${numero.porcento10(valor)}')