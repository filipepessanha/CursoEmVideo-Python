# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria de acordo com sua idade:
# -Até 9 anos: MIRIM
# -Até 14 anos: INFANTIL
# -Até 19 anos: JUNIOR
# -Até 20 anos: SÊNIOR
# -Acima: MASTER

from datetime import date
nome = str(input('Digite seu nome: '))
ano = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano

print('Olá, {}, você tem {} anos.'.format(nome, idade))

if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade <= 20:
    print('Sua categoria é SÊNIOR.')
elif idade > 20:
    print('Sua categoria é MASTER.')