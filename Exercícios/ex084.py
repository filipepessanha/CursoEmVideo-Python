# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
# 	Quantas pessoas foram cadastradas
# 	Uma listagem com as pessoas mais pesadas
# 	Uma listagem com as pessoas mais leves

cadastro = []
lista_pessoas = []
maior = menor = 0

while True:
    cadastro.append(str(input('Digite o nome: ')))
    cadastro.append(int(input('Digite o peso: ')))
    r = str(input('Deseja continuar? [S/N]: '))
    if len(lista_pessoas) == 0:
        maior = menor = cadastro[1]
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    lista_pessoas.append(cadastro[:])
    cadastro.clear()
    if r in 'Nn':
        break

print(f'Foram cadastradas {len(lista_pessoas)} pessoas')
print(f'O maior peso foi {maior}kg. Peso de: ', end='')
for c in lista_pessoas:
    if c[1] == maior:
        print(f'{c[0]}...', end='')
print()
print(f'O menor peso foi {menor}kg. Peso de: ', end='')
for c in lista_pessoas:
    if c[1] == menor:
        print(f'{c[0]}...', end='')