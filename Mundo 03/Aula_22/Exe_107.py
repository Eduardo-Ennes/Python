import numero
valor = float(input('Digite um valor: R$'))
print('-=' * 30)
print(f'A metade de {numero.moeda(valor)} é {numero.metade(valor, True)}')
print(f'O dobro de {numero.moeda(valor)} é {numero.dobro(valor, True)}')
print(f'Aumentando 10% é R${numero.aumentar(valor, 10, True)}')
print(f'Diminuindo 10% é {numero.diminuir(valor, 10, True)}')