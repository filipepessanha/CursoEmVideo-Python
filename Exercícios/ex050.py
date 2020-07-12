# Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o.

soma = 0
for n in range(1, 7):
    n = int(input('Digite o {}º número: '.format(n)))
    if n % 2 == 0:
        soma = soma + n

print('A soma de todos os números pares é {}'.format(soma))