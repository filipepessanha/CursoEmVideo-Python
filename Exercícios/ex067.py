# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O
# programa será interrompido quando o número solicitado for negativo.

cont = mult = n = 0
while True:
    print('-' * 20)
    n = int(input('Digite um número: '))
    print('-' * 20)
    if n < 0:
        break
    while cont < 10:
        cont += 1
        mult = n * cont
        print(f'{n} x {cont} = {mult}')
    cont = 0
