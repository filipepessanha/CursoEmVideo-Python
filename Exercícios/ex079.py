# Crie um programa onde o usuário possa digitar vários valores númericos e cadastre-os em uma lista. Caso o número já
# exista lá dentro, ele não será adicionado. No final serão exibidos todos os valores únicos digitados,
# em ordem crescente.

valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    if valores.count(v) > 1:
        print(f'O número {v} já está lista.')
        valores.pop()
    r = str(input('Deseja digitar outro valor? [S/N]: ')).lower()
    if r == 'n':
        break
print(f'Você digitou os valores {sorted(valores)}.')
