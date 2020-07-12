# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print('Forma 1')

for n in range(1, 51):
    if n % 2 == 0:
        print(n, end=' ')

# Apenas para passar para outra linha

print()
print('-' * 50)

# Pode ser feito dessa outra forma
print('Forma 2')

for n2 in range(2, 51, 2):
    print(n2, end=' ')
