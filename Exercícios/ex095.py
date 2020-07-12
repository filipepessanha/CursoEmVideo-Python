# Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

time = []
jog = {}
g = []
while True:
    jog.clear()
    jog['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jog["nome"]} jogou?: '))
    g.clear()
    for c in range(0, partidas):
        g.append(int(input(f'   Quantos gols na partida {c}: ')))
    jog['gols'] = g[:]
    jog['total'] = sum(g)
    time.append(jog.copy())
    while True:
        r = str(input('Quer continuar? [S/N]: ')).upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if r == 'N':
        break
print('='*30)
print('cod ', end='')
for n in jog.keys():
    print(f'{n:<15}', end='')
print()
print('-'*30)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('='*30)
