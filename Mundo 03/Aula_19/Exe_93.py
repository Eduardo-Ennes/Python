jogador = dict()
ficha = []
jogador["Nome"] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
for c in range(0, tot):
    ficha.append(int(input(f'Quantas gols na partida {c}°: ')))
jogador["Gols"] = ficha[:]
jogador["Total"] = sum(ficha)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O Jogador {jogador["Nome"]} jogou {tot}° partidas')
for i, g in enumerate(ficha):
    print(f'   => Na {i+1}° partida marcou {g} gols')
print(f'O total de gols foi {jogador["Total"]}')