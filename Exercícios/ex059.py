# Crie um programa que leia dois valores e mostre um estrutura na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

print('=======CALCULADORA PYTHON=======')
print('Digite dois números')
n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
op = 0
while op != 5:
    print('----------------------------')
    print('Esolha uma das opções abaixo')
    print('[1] somar')
    print('[2] multiplicar')
    print('[3] maior')
    print('[4] novos números')
    print('[5] sair do programa')
    op = int(input('Digite uma opção: '))
    if op == 1:
        soma = n1 + n2
        print('-------SOMA-------')
        print('{} + {} = {}'.format(n1, n2, soma))
    elif op == 2:
        mult = n1 * n2
        print('-------MULTIPLICAÇÃO-------')
        print('{} x {} = {}'.format(n1, n2, mult))
    elif op == 3:
        print('-------MAIOR NÚMERO-------')
        if n1 != n2:
            if n1 > n2:
                a = n1
            else:
                a = n2
            print('O maior número é {}'.format(a))
        else:
            print('Os dois números são iguais.')
    elif op == 4:
        print('----------------------------')
        print('Digite os novos números')
        n1 = int(input('1º número: '))
        n2 = int(input('2º número: '))
    if op < 1 or op > 5:
        print('----------------------------')
        print('Opção inválida, tente novamente.')


print('FIM')
