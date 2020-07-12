time = ('Corinthians', 'Grêmio', 'Fortaleza', 'Vasco', 'Palmeiras', 'Athetico-PR', 'Atlético-MG', 'Bahia', 'Ceará',
         'Fluminense', 'Sport', 'São Paulo', 'Goiás', 'Botafogo', 'Internacional', 'Coritiba', 'Flamengo', 'Santos',
         'Chapecoense', 'Atlético-GO')

print(f'Os cinco primeiros colocados são: ', end='')
for c in range(0, 5):
    print(time[c], end=', ' if c < 4 else '.')

print(f'\nOs quatro últimos colocados são: ', end='')
for a in range(16, 20):
    print(time[a], end=', ' if a < 19 else '.')

print(f'\nOs times em ordem alfabética são: {sorted(time)}')

cont = 0
if 'Chapecoense' in time:
    ch = time.index('Chapecoense')
    print(f'A Chapecoense está na {ch + 1}ª posição.')
else:
    print('Não')