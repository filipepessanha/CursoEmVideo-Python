# Escreva um programa que faça o computador "pensar" em um númeo inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou
# perdeu.

import random
n = int(input("Escolha um número de 0 a 5: "))
r = random.randint(0, 5)
print('Você escolheu o número {}, eu pensei no número {}'.format(n, r))
if n == r:
    print('Você acertou!')
else:
    print('Você errou, tente de novo!')
