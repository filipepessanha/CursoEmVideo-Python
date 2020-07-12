# Aprimore o desafio anterior, mostrando no final:
# 	A soma de todos os valores pares digitados.
# 	A soma dos valores da terceira coluna.
# 	O maior valor da segunda linha.


matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = soma_col = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input(f'Digite um numero para [{l}, {c}]: '))
        matriz[l][c] = n
        if n % 2 == 0:
            soma += n
        if c == 2:
            soma_col += n
        if l == 1:
            if c == 0:
                maior = n
            elif n > maior:
                maior = n
for l in range(0, 3):
    for c in range(0, 3):
        print(f'|{matriz[l][c]:^5}|', end='')
    print()

print(f'A soma de todos os números pares é: {soma}')
print(f'A soma dos valores da terceira coluna é: {soma_col}')
print(f'O maior número da segunda linha é: {maior}')