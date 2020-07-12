# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão
# conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
# três listas geradas.

lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input('Digite um número: '))
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'nN':
        break
    lista.append(num)
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print(f'A lista completa é: {lista}')
print(f'A lista com números pares é: {lista_par}')
print(f'A lista com números ímpares é: {lista_impar}')