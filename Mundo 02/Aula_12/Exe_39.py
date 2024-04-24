from datetime import datetime
ano = int(input('Digite seu ano de nascimento?'))
c1 = datetime.now().year - ano
c2 = c1 - 18
if c1 == 18:
    print('Quem nasceu no ano {} deve-se alistar imediatamente!'.format(ano))
elif c1 > 18:
    print('Quem nasceu no ano de {} ja devería ter se alistado a {} ano(s).'.format(ano, c2))
else:
    print('Só se alistaram pessoas com idade superior ou igual a 18 anos.')