# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número para saber se ele é primo: '))
total = 0
for c in range(1, n+1):
    if n % c == 0:
        total = total + 1

if total == 2:
    print('{} é número primo'.format(n))
else:
    print('{} não é número primo'.format(n))
