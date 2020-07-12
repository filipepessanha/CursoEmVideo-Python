# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jog = {}
g = []
jog['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jog["nome"]} jogou?: '))
for c in range(0, partidas):
    g.append(int(input(f'   Quantos gols na partida {c}: ')))
jog['gols'] = g[:]
jog['total'] = sum(g)
print('='*30)

print(jog)
print('='*30)

for k, v, in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('='*30)

print(f'O jogador {jog["nome"]} jogou {jog["total"]} partidas.')
for i, v in enumerate(jog['gols']):
    print(f'    => Na partida {i}, fez {v} gols.')
print(f'Total de {jog["total"]} gols.')
