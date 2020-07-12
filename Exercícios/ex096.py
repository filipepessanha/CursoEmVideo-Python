# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
# comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é {a}m².')


print('Controle de Terrenos')
print('-'*20)
l = int(input('LARGURA (m): '))
c = int(input('COMPRIMENTO (m): '))
area(l, c)

