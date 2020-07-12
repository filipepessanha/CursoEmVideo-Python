# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um
# triângulo.

m1 = float(input('Digite o tamanho da reta maior: '))
m2 = float(input('Digite a segunda reta: '))
m3 = float(input('Digite a terceira reta: '))

if m2 == m3 != m1 and m2 + m3 > m1:
    print('Essas linhas podem formar um triângulo isósceles.')
else:
    if m1 == m2 == m3 and m2 + m3 > m1:
        print('Essas linhas podem formar um triângulo equilátero.')
    else:
        if m1 != m2 != m3 and m2 + m3 > m1:
            print('Essas linhas formam um triângulo escaleno.')
        else:
            print('Essas linhas não podem formar um triângulo.')
