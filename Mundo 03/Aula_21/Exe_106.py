def ajuda(com):
    help(com)


def titulo(msg):
    tam = len(msg)
    print('~' * tam)
    print(f'{msg}')
    print('~' * tam)


while True:
    titulo('SISTEMA DE AJUDA PYHELP')
    print('Digite (sair) para encerrar o programa.')
    comando = str(input('Função ou Biblioteca: ')).strip()
    if comando.upper() in 'SAIR':
        break
    else:
        ajuda(comando)
titulo('\nMUITO OBRIGADO POR USAR A FERRAMENTA FEFE TIRANDO DUVIDAS.\nATÉ LOGO.')