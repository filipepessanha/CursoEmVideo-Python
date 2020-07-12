# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n’)


def leiaInt(n):
    while True:
        a = input(n)
        if not a.isnumeric():
            print('ERRO! Digite um número inteiro válido.')
        else:
            break
    return a


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
