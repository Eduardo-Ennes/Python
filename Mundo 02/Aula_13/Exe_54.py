from datetime import date
atual = date.today().year
maior = 0
menor = 0
for pess in range (1 , 4):
    data = int(input('\nData de nascimento da {}° pessoa?'.format(pess)))
    c1 = atual - data
    if c1 >= 18:
        print(f'Quem nasceu no ano de {data} já atingiu a maioridade.')
        maior = maior + 1
        print('O número de pessoas que atingiram amaiortidade é de {} pessoa(s).'.format(maior))
    else:
        print(f'Quem nasceu no ano de {data} não atingiu a maioridade.')
        menor = menor + 1
        print('O número de pessoas que nao atingiram a maiortidade é de {} pessoa(s)'.format(menor))
print('\nAo todo tivemos. \nmaiores = {} pessoa(s)\nmenores = {} pessoa(s)'.format(maior,menor))
