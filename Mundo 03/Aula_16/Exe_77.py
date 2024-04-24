print('-='*30)
print('EXERCICIO DE VOGAIS')
print('-='*30)
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'grátis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro',)
for p in palavras:
    print(f'\nNa palavra ({p}) temos -->', end=' ')
    for letra in p:
        if letra.lower() in 'aáeiou':
            print(letra, end=' ')
print('\n\nFIM DO PROGRAMA...')