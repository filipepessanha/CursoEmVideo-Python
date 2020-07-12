a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
tup = (a, b, c, d)
print(tup)

# Quantas vezes aparece o número 9

if tup.count(9) == 0:
    print('O número 9 não foi digitado nenhuma vez.')
else:
    if tup.count(9) == 1:
        x = 'vez'
    else:
        x = 'vezes'
    print(f'O número 9 apareceu {tup.count(9)} {x}.')

# Onde o número 3 aparece pela primeira vez

if 3 not in tup:
    print('O número 3 não foi digitado.')
else:
    print(f'O número 3 está na posição {tup.index(3) + 1}.')

# Quantos números pares existem

cont = 0
for c in tup:
    if c % 2 == 0:
        cont += 1
if cont == 0:
    print('Não foi digitado nenhum número par.')
else:
    print(f'Existem {cont} números pares.')
