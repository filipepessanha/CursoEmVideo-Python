import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[1;31mO site Pudim não está acessível no momento.\033[0m')
else:
    print('\033[1;32mO site Pudim está funcionando normalmente.\033[0m')