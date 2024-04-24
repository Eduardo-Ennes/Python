from random import randint
from operator import itemgetter
lista = {'Jogador 1': randint(1 , 6),
        'Jogador 2': randint(1 , 6),
        'Jogador 3': randint(1 , 6),
        'Jogador 4': randint(1 , 6)}
print(lista)
ranking = list()
for c, v in lista.items():
    print(f'{c} --> {v}')
print('-=' * 10, 'RANKING DOS VENCEDORES', '-=' * 10)
ranking = sorted(lista.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° colocado --> {v[0]} = {v[1]}')