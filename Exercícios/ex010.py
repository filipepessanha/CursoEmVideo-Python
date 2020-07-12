# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

n = float(input('Digite o valor: R$'))
d = n/(3.27)

print('Você pode comprar US${:.2f}'.format(d))
