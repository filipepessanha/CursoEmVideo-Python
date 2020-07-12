# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
cont = soma = 0
while True:
    print('----------------------------------------')
    valor = int(input('Digite um valor: '))
    pi = str(input('Escolha par ou impar. [P/I]: ')).strip().lower()
    comp = randint(0, 10)
    soma = valor + comp
    if soma % 2 == 0:
        r = 'PAR'
        if pi == 'p':
            venc = 'Você venceu'
        else:
            venc ='Você perdeu'
    else:
        r = 'ÍMPAR'
        if pi == 'i':
            venc = 'Você venceu'
        else:
            venc = 'Você perdeu'
    print(f'\nVocê jogou {valor} e o computador {comp}.')
    print(f'Total de {soma}. DEU {r}\n')
    print(f'{venc}\n')
    if venc == 'Você venceu':
        cont += 1
        print('Jogue novamente...')
    else:
        print('----------------------------------------')
        print('Fim de jogo')
        if cont == 0:
            print('Você não ganhou nenhuma vez.')
        else:
            if cont == 1:
                x = 'vez'
            else:
                x = 'vezes'
            print(f'Você ganhou {cont} {x}.')
        break
