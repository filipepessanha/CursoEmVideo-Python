# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.

from time import sleep

for cregr in range(10, 0, -1):
    print(cregr)
    sleep(1)
print('BOOM!!!')