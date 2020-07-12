# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira
# função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os
# valores PARES sorteados pela função anterior.
from random import randint as ri
numeros = []


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        c = ri(1, 10)
        numeros.append(c)
        print(c, end=' ')
    print('PRONTO!')


def somaPar():
    print(f'Somando os valores pares de {numeros}, temos ', end='')
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(soma)


sorteia()
somaPar()



