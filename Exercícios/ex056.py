# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# -A média de idade do grupo
# -Qual é o nome do homem mais velho
# -Quantas mulheres têm menos de 20 anos.

cont = 0
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''

for grupo in range(1, 5):
    print('-----{}ª PESSOA-----'.format(grupo))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (F/M): ')).strip().lower()

# o mais velho
    if grupo == 1 and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome

    elif idade > maioridadehomem and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome

# mulheres com menos de 20 anos
    if sexo == 'f' and idade < 20:
        cont = cont + 1

# media de idade
    somaidade += idade

mediaidade = somaidade / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('O homem mais velho é: {}'.format(nomevelho))
if cont > 0:
    print('A quantidade de mulheres abaixo de 20 anos é: {}'.format(cont))
else:
    print('Não temos mulheres abaixo de 20 anos.')
