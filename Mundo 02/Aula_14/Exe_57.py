sexo = str(input('Digite seu sexo (M/F)?')).strip().upper() [0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido, digite novamente (M/F)?')).strip().upper() [0]
print('Fim!')