# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada km acima do limite.

vel = int(input('Digite a velocidade do carro: '))
km = (vel - 80)
multa = km * 7
if km <= 0:
    print('Boa viagem!')
else:
    print('A velocidade da via é de 80km/h\n'
          'Você passou {}km/h acima do limite permitido\n'
          'Sua multa será de R${},00\n'.format(km, multa))
