# Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoa ainda não atingiram a
# maioridade e quantas já são maiores.

from datetime import date

cont = 0
cont2 = 0
for n in range(1, 8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
    idade = date.today().year - ano
    if idade >= 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
    print(idade)
print('Dessas pessoas, {} pessoas já atingiram a maioridade e {} ainda não atingiram a maioridade'.format(cont, cont2))

