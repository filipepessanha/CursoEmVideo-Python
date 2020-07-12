# Faça um programa que receba uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu
# programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*valor):
    print('=' * 50)
    print('Analisando os valores passados...')
    m = 0
    for c in valor:
        print(c, end=' ')
        if c == 0:
            m = c
        elif c > m:
            m = c
        sleep(0.25)
    print(f'Foram informados {len(valor)} valores ao todo')
    print(f'O maior valor informado foi {m}')


maior(4, 2, 3, 8, 5, 10, -1)
maior(-1)
