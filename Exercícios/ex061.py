# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

primtermo = int(input('Digite o 1º termo da PA: '))
razao = int(input('Digite a razão da PA: '))

cont = 0
pa = 0
while cont < 10:
    cont += 1
    pa = primtermo + (cont - 1) * razao
    print(pa, end=' > ')
print('FIM')
