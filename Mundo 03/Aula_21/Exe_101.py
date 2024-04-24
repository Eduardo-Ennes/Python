def voto(num=0):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - num
    if 18 <= idade < 70:
        return f'A sua idade é de {idade} anos: VOTO OBRIGATÓRIO.'
    elif idade < 16:
        return f'A sua idade é de {idade} anos: VOTO NEGADO.'
    else:
        return f'A sua idade é de {idade} anos: VOTO OPCIONAL'


n = int(input('Digite o seu ano de nasciemento: '))
print(voto(n))