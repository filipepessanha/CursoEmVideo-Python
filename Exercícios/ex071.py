# Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o
# valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# Considere que o caixa possui cédulas de R$50, R$20, R$10, e R$1.

print('='*30)
print('BANCO CEV')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
c1 = int(valor / 50)
r1 = (valor % 50)
c2 = int(r1 / 20)
r2 = (r1 % 20)
c3 = int(r2 / 10)
r3 = (r2 % 10)
c4 = r3
if c1 > 0:
    print(f'Total de {c1} notas de R$50')
if c2 > 0:
    print(f'Total de {c2} notas de R$20')
if c3 > 0:
    print(f'Total de {c3} notas de R$10')
if c4 > 0:
    print(f'Total de {c4} notas de R$1')
print('='*30)
print('Volte sempre ao banco CEV! Tenha um bom dia!')