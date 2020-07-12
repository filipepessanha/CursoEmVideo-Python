# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no
# intervalo de 1 ate 500.

soma = 0
cont = 0
for impar in range(1, 501, 2):
    if impar % 3 == 0:
        soma = soma + impar
        cont = cont + 1
print('A soma de todos os {} números ímpares divisíveis por 3 é {}'.format(cont, soma))
