
def fatorial(n):
    '''
        Essa função retorna o fatorial de um número.
    '''
    valor = 1
    for c in range(n, 0, -1):
        print(f'{c}', end='')
        if c > 1:
            print(' x ', end='')
        else:
            print(' = ', end='')
        valor *= c
    return valor



def moeda(n=0, moeda='R$'):
    '''
        Essa função retorna valores no nosso padrão da moeda real.
    '''
    return f'{moeda}{n:.2f}'.replace('.',',')



def aumento(n=0, taxa=0, forma=False):
    '''
        Aumenta um valor na porcentagem desejada.
    '''
    res = n + (taxa/100 * n)
    return res if forma is False else moeda(res)



def desconto(n=0, taxa=0, forma=False):
    '''
        Diminui um valor na porcentagem desejada.
    '''
    res = n - (taxa/100 * n)
    return res if forma is False else moeda(res)



def metade(x, forma=False):
    res = x / 2
    return res if forma is False else moeda(res)



def dobro(x, forma=False):
    res = x * 2
    return res if forma is False else moeda(res)



def resumo(n=0, t1 = 0, t2=0):
    print('-' * 30)
    print('Resumo do Valor'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{moeda(n)}')
    print(f'O dobro do preço: \t{dobro(n, True)}')
    print(f'A metade do preço: \t{metade(n, True)}')
    print(f'Aumento de {t1}%: \t{aumento(n, t1, True)}')
    print(f'Desconto de {t2}%: \t{desconto(n, t2, True)}')
    print(f'-' * 30)



def leiavalor(msg):
    indice = False
    while not indice:
        valor = str(input(msg)).strip().replace(',','.')
        if valor.isalpha() or valor == '':
            print(f'ERRO! {valor} é um número inválido!')
        else:
            indice = True
            return float(valor)



def inteiro(msg):
    '''
        Le apenas números inteiros
    '''
    while True:
        try:
            valor = int(input(msg))
        except:
            print('Digite apenas números inteiros.')
        else:
            return valor



def real(n):
    '''
        Le apenas núemros reais.
    '''
    while True:
        try:
            valor = float(input(n))
        except:
            print('Digite apenas números reais. ')
        else:
            return valor



def menu (msg):
    lista = []
    for v, item in enumerate(msg):
        print(f'[{v + 1}] - {item}')
    while True:
        opc = inteiro('\nDigite a opção: ')
        if opc == 1:
            lista.append(input('Adicione algo: '))
            print('Adicionado com sucesso!')
        if opc == 2:
            print()
            print('Sua lista está assim:')
            for n, c in enumerate(lista):
                print(f'{n + 1} -> {c}')
            print()
        if opc == 3:
            print('\nSEU PROGRAMA ENCERROU, MUITO OBRIGADO!')
            break
        if opc == 0 or opc >= 4:
            print('Digite uma opção válida.')



def linha(tam=42):
    return '-' * tam



def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())



def menu(msg):
    cabeçalho('Analisando sistemas')
    for v, item in enumerate(msg):
        print(f'[{v + 1}] - {item}.')
    print()
    opc = inteiro('Qual a sua opção: ')
    return opc



def duplicados(msg):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in msg:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        numeros_checados.add(numero)
    return primeiro_duplicado