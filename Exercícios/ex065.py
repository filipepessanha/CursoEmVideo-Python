# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
# valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar.


cont = soma = maior = menor = media = 0
final = 's'
while final == 's':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    final = str(input('Deseja continuar? [S/N]: ')).lower()
media = soma / cont
print(menor)
print('A soma dos {} números digitados é {}, a média é {:.2f} e o maior número é {}.'.format(cont, soma, media, maior))

