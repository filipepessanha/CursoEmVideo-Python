# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Calcular o preço do aluguel de um carro baseado em dias e quilometragem percorrida.
km = float(input('Quilometragem percorrida: '))
pkm = km*0.15
d = int(input('Tempo de locação em dias: '))
pd = d*60
t = pkm + pd

print('Quilômetros rodados: {:.1f}km\nDias alugados: {} dias\n'
      'Preço por km: R${:.2f}\nPreço por dia: R${:.2f}\nTotal: R${:.2f}'
      .format(km, d, pkm, pd, t))

