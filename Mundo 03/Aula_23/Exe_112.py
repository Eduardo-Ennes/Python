import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site não está podendo ser acessado.')
else:
    print('Tudo certo!')
    print(site.read())