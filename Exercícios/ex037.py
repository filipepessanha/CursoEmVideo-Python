#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# -1 para binário
# -2 para octal
# -3 para hexadecimal

n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases de conversão
[1] Binário
[2] Octal
[3] Hexadecimal''')
opt = int(input('Sua opção: '))

if opt == 1:
    print('{} em binário é igual a {}'.format(n, bin(opt)))
elif opt == 2:
    print('{} em octal é igual a {}'.format(n, oct(opt)))
elif opt == 3:
    print('{} em hexadecimal é igual a {}'.format(n, hex(opt)))
else:
    print('Opção inválida.')