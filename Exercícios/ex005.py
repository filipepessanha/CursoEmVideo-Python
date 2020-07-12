# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O número é {}, seu antecessor é {}, e seu sucessor é {}'.format(n, a, s))
# O programa pode ser feito sem utilizar as variáveis 'a' e 's'. Isso ficaria da seguinte forma:
# print('O número é {}, seu antecessor é {}, e seu sucessor é {}'.format(n, (n-1), (n+1)))
# O objetivo desse formato reduzido é economizar memória, porém, caso seja necessário usar essas variáveis mais para
# frente será necessário escrever os códigos como se encontram.
