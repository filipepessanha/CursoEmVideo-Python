# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura em ºC: '))
f = c * 1.8 + 32
print('A temperatura é: {:.1f}ºF'.format(f))
