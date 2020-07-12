# Crie um programa que faça o computador jogar Jokenpô com você.

from random import choice
from time import sleep

print('-=-' * 10)
print('JOKENPÔ')
print('-=-' * 10)
player = int(input('Digite (1) para PEDRA, (2) para PAPEL, (3) para TESOURA: '))
print('-' * 30)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('-' * 30)
options = ['PEDRA', 'PAPEL', 'TESOURA']
computer = choice(options)

if player == 1:
    print('Você escolheu PEDRA')
    print('O computador escolheu: {}'.format(computer))
elif player == 2:
    print('Você escolheu PAPEL')
    print('O computador escolheu: {}'.format(computer))
elif player == 3:
    print('Você escolheu TESOURA')
    print('O computador escolheu: {}'.format(computer))
else:
    print('Não, seu animal... É para digitar apenas 1, 2 ou 3!!!')

print('-' * 30)

if player == 1 and computer == 'PAPEL' or player == 2 and computer == 'TESOURA' or player == 3 and computer == 'PEDRA':
    print('Computador venceu.')
elif player == 1 and computer =='PEDRA' or player == 2 and computer == 'PAPEL' or player == 3 and computer == 'TESOURA':
    print('Vocês empataram.')
elif player != 1 and player != 2 and player != 3:
    print('Jogue novamente.')
else:
    print('Parabéns, você venceu!!!')
print('-' * 30)
