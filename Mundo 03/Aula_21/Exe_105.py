def nota(*num,sit=False):
    """
    --> Função para analisar notas.
    :param num: resp está para num, aceitando varios valores.
    :param sit: forma opcional para mostrar a situação.
    :return: Dicionário com informações da turma.
    """
    ficha = dict()
    ficha['Total'] = len(num)
    ficha['Maior'] = max(num)
    ficha['Menor'] = min(num)
    ficha['Média'] = sum(num) / len(num)
    if sit:
        if ficha['Média'] < 4:
            ficha['Situação'] = 'REPROVADO'
        if 4 <= ficha['Média'] < 7:
            ficha['Situação'] = 'RECUPERAÇÃO'
        if ficha['Média'] >= 7:
            ficha['Situação'] = 'APROVADO'
    return ficha


resp = nota(9, 9.5, 8.5, 10, 9,8, sit=True)
print(resp)
help(nota)