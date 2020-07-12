from random import randint

a = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))

maior = menor = cont = 0
print('Os números sorteados foram: ', end='')
for c in a:
    print(c, end=' ')
print(f'\nO maior número é {max(a)} e o menor número é {min(a)}')