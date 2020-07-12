# Faça um programa que tenha uma função chamada contador (), que receba três parâmetros: início, fim e passo,
# e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
#   De 1 até 10, de 1 em 1
# 	De 10 até 0, de 2 em 2
# 	Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    if inicio > fim:
        passo = passo * (-1)
    if passo == 0:
        passo = 1
    print('=' * 40)
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(1.5)
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('=' * 40)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, abs(p))
