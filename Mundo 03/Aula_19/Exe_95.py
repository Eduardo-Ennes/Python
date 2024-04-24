time = list()
jogador = dict()
lista = list()
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador['Nome']} jogou: '))
    if tot != 0:
        total = 0
        for c in range(0, tot):
            lista.append(int(input(f'Quantos gols marcou na {c+1}° partida: ')))
        jogador['Gols'] = lista[:]
        jogador['Total'] = sum(lista)
        time.append(jogador.copy())
        lista.clear()
        jogador.clear()
    while True:
        op = str(input('Deseja continuar [S/N]: ')).upper()[0]
        if op in 'NS':
            break
        else:
            print('ERRO! RESPONDA APENAS S OU N!')
    if op == 'N':
        break
print('-' * 40)
for i, v in enumerate(time):
    print(f'Num = [{i}] --> {v['Nome']}\nsequência de gols {v['Gols']}\nTotal de {v['Total']} gols')
    print()
while True:
    print('-=' * 30)
    print('999 para sair.')
    ob = int(input('Mostrar dados de qual jogador:'))
    if ob == 999:
        break
    if ob >= len(time):
        print('Digito inválido, Tente novamente...')
    for i, v in enumerate(time):
        if ob == i:
            cont = 0
            print('-' * 40)
            print(f'Levantamento do(a) {v['Nome']}')
            for n in v['Gols']:
                cont += 1
                print(f'Na {cont}° partida marcou {n} gol(s)')
print('MUITO OBRIGADO!')