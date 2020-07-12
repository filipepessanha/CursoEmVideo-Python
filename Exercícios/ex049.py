# Refaça o desafio 009 mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço 'for'.

n = int(input('Digite um número: '))

for tab in range(1, 11):
    print('{} x {} = {}'.format(n, tab, n * tab))