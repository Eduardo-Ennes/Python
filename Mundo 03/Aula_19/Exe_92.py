from datetime import  datetime
lista = dict()
lista["Nome"] = str(input('Nome: '))
lista["Nascimento"] = int(input('Ano de nascimento: '))
lista["Idade"] = datetime.now().year - lista["Nascimento"]
lista["Carteira"] = int(input('Número da carteira de trabalha [0 não tem]: '))
if lista["Carteira"] != 0:
    lista["Contratação"] = int(input('Ano de contratação: '))
    lista["Salario"] = float(input('Salário: R$'))
    lista["Aposentadoria"] = (lista["Contratação"] - lista["Nascimento"]) + 35
print('-=' * 30)
for c, v in lista.items():
    print(f'{c} --> {v}')