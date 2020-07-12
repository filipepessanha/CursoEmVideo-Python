# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
# valor digitado e as suas respectivas posições na lista.

valores = []
mx = mn = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mx = mn = valores[c]
    else:
        if valores[c] > mx:
            mx = valores[c]
        if valores[c] < mn:
            mn = valores[c]

print(f'Você digitou os valores {valores}')

print(f'O maior valor digitado foi {mx} na posição: ', end='')
for pos, val in enumerate(valores):
    if val == mx:
        print(f'{pos}', end=' ')

print(f'\nO menor valor digitado foi {mn} na posição: ', end='')
for pos, val in enumerate(valores):
    if val == mn:
        print(f'{pos}', end=' ')
