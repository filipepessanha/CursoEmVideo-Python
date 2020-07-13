from mod.moeda import *

p = float(input('\033[32mDigite o preço: R$'))
print(f'A metade de {p} é {metade(p)}')
print(f'O dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {reduzir(p, 13)}')
