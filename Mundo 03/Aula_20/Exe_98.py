def num3(i, f, p):
    if p == 0:
        p = 1
    for c in range(i, f, p):
        print(c, end=' ')
    print()
    if i > f:
        for c in range(i, f, -p):
            print(c, end=' ')
        print()


num3(1, 11, 1)
num3(10, 0, 2)
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
num3(ini, fim, pas)