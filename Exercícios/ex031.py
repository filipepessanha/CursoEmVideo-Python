# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50
# por cada km para viagens de até 200km e R$0,45 para viagens mais longas.

d = int(input('Distância da viagem: '))
if d <= 200:
    a = d * 0.50
    print('O valor da viagem é: R${:.2f}'.format(a))
else:
    b = d * 0.45
    print('O valor da viagem é: R${:.2f}'.format(b))
