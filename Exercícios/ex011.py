# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

w = float(input('Digite a largura da parede: '))
h = float(input('Digite a altura da parede: '))
a = w*h
v = a/2

print('Largura da parede: {}m'.format(w))
print('Altura da parede: {}m'.format(h))
print('Área de parede: {}m²'.format(a))
print('Volume de tinta necessária: {}l'.format(v))
