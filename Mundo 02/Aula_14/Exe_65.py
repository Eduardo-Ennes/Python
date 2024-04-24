opçao = 'Ss'
soma = quantidade = media = maior = menor = 0
while opçao in 'Ss':
    numero = int(input('Digite um núemro:'))
    opçao = str(input('Você deseja continuar? (S) ou (N):'))
    quantidade += 1
    soma += numero
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
media = soma / quantidade
print(f'\nVocê digitou {quantidade} números'
    f'\nA soma dos valores {soma}'
    f'\nA média dos valores {media}'
    f'\nO maior número {maior}'
    f'\nO menor número {menor}')