# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
n = float(input('Digite um número: '))
s = sin(radians(n))
c = cos(radians(n))
t = tan(radians(n))
print('Seno: {}\nCosseno: {}\nTangente {}'.format(s, c, t))
