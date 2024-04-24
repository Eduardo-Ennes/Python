v1 = float(input('Digite o valor do produto que saira por 5% de desconto:'))
por = v1 * 0.05
val= v1 - por
print('O produto que custava R${}, com o desconto de 5% saíra por R${:.2f}'.format(v1,val))



#OUTRA FORMA
preco = float(input('Digite o valor do produto:R$'))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${} agora com 5% de desconto, irá custar R${:.2f}'.format(preco,novo))