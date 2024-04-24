frase = str(input('Digite uma frase:')).strip()
print('Quantas vezes a letra A aparece: {} vezes'.format(frase.upper().count('A')))
print('Qual é a primeira posição que a letra A aparece? {} posição'.format(frase.upper().find('A') + 1))
print('A última letra A aparece na: {} posição'.format(frase.upper().rfind('A') + 1))