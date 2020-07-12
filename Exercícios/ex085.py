# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
for c in range(0, 7):
    n = int(input(f'Digite o {c+1}º número: '))
    if n % 2 == 0:
        num[0].insert(c, n)
    else:
        num[1].insert(c, n)
print(f'Os números pares são {sorted(num[0])}')
print(f'Os números ímpares são {sorted(num[1])}')

