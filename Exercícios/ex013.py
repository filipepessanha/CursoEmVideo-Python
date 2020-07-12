# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

s = float(input('Digite seu salário: R$'))
a = s*0.15
st = s+a

print('Aumento de R${:.2f} no seu salário, totalizando R${:.2f}'.format(a, st))
