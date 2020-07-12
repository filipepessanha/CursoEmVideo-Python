# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
a = frase.replace(' ', '').replace('-', '').replace('.', '')
frase2 = a[::-1]
print(a)
print(frase2)

if a == frase2:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palindromo')
