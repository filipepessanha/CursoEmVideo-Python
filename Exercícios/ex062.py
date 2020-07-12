# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando
# ele disser que quer mostrar 0 termos.

p = int(input('Digite o 1º termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 10
while cont > 0:
    print(p, end=' > ')
    p += r
    cont -= 1
    if cont == 0:
        print('PAUSA')
        cont = int(input('Quantos termos você quer mostrar a mais?: '))
print('FIM')
