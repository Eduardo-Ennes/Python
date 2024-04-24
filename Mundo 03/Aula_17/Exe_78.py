lista = list()
for c in range(0,5):
    lista.append(int(input(f'Digite o valor para a posição {c}°:')))
print('-=' * 30)
print('Você digitou os valores:', lista)
print(f'O maior número da lista é o ({max(lista)}) e a sua posição na lista é a {lista.index(max(lista)) + 1}° posição')
print(f'O menor número da lista é o ({min(lista)}) e a sua posição na lista é a {lista.index(min(lista)) + 1}° posição')