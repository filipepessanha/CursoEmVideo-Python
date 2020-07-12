# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e
# mostre o comprimento da hipotenusa.

from math import hypot
c1 = float(input('Digite o cateto a: '))
c2 = float(input('Digite o cateto b: '))

print('O valor da hipotenusa é: {:.2f}'.format(hypot(c1, c2)))