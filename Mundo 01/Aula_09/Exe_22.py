nome = str(input("Digite um nome?")).strip()
print('O nome em letras minúscilas é: {}'.format(nome.lower()))    
print('O nome em letras maiúsculas é: {}'.format(nome.upper()))    
print('O nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))    
print('O primeiro nome tem {} letras'.format(nome.find(' ')))      