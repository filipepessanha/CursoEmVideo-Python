# Melhore o jogo do desafio 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
print('Pensei em um número de 0 a 10')
acertou = False
cont = 0
while not acertou:
    jogador = int(input('Qual o seu palpite?: '))
    cont = cont + 1
    if jogador < 0 or jogador > 10:
        print('Número inválido, digite um número entre 0 e 10')
    if computador < jogador < 10 and jogador >= 0:
        print('Menos, tente outro número.')
    if computador > jogador >= 0 and jogador < 10:
        print('Mais, tente outro número.')
    if jogador == computador:
        acertou = True
print('Parabéns, você acertou na {}ª tentativa.!!!'.format(cont))
