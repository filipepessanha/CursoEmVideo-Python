# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# 	- Quantos números foram digitados
# 	- A lista de valores ordenada de forma decrescente
# 	- Se o valor 5 foi digitado e está ou não na lista

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'nN':
        break
if len(lista) > 1:
    n = 'números'
else:
    n = 'número'
print(f'Foram digitados {len(lista)} {n}.')
lista.sort(reverse=True)
print(f'A lista em ordem descrescente é {lista}')
if 5 in lista:
    print('O número 5 está na lista.')
else:
    print('O número 5 não está na lista.')
