# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5x4x3x2x1 = 120

n = int(input('Digite um número para saber seu fatorial: '))

f = 1
c = 0
for n in range(n, -1):
    f = f * n
    c = c + 1
    print(f)
