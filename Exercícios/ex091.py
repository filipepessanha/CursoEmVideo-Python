# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint as r
from operator import itemgetter as i

jogo = {}
ordem = {}
for c in range(1, 5):
    jogo[f'Jogador {c}'] = r(1, 6)
for k, v in jogo.items():
    print(f'{k}: {v}')
ordem = sorted(jogo.items(), key=i(1), reverse=True)
print()
print('RANKING')
for v, d in enumerate(ordem):
    print(f'{v + 1}° lugar: {d[0]} com valor {d[1]}')
