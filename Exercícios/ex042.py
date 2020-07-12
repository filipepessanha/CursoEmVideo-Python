# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# -Equilátero: todos os lados iguais
# -Isósceles: dois lados iguais
# -Escaleno: todos os lados diferentes

m1 = float(input('Primeiro segmento: '))
m2 = float(input('Segundo segmento: '))
m3 = float(input('Terceiro segmento: '))

if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Esses segmentos podem formar um triângulo', end=' ')
    if m1 == m2 == m3:
        print('EQUILÁTERO.')
    elif m1 != m2 != m3 != m1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Essas linhas não podem formar um triângulo.')