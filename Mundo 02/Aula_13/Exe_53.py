nome = input('Digite um nome ou uma frase?').strip().upper()
s = nome.split()
junto =''.join(palavras)
inverso = ''
for letra in rangepalavra (len(junto)-1 , -1 , -1):
    print(junto[letra])
    inverso = inverso + junto[letra]
if inverso == junto:
    print('Ele é um palindromo!')
else:
    print('Não é um palindromo!')