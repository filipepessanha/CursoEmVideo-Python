# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('Digite o valor: R$'))
d = v*0.05
vt = v-d

print('Desconto de R${:.2f}. Valor total de R${:.2f}'.format(d, vt))
