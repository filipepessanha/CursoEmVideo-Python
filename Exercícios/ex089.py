# Crie um programa que leia nome e as notas de vários alunos e guarde tudo em uma lista composta. No final,
# mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

boletim = []
aluno = []
while True:
    aluno.append(str(input('Aluno: ')))
    aluno.append(float(input('Nota 1: ')))
    aluno.append(float(input('Nota 2: ')))
    aluno.append((aluno[1] + aluno[2]) / 2)
    boletim.append(aluno[:])
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
    aluno.clear()
for c in range(0, len(boletim)):
    print(f'{c:<3}', end=' ')
    print(f'{boletim[c][0]:}', end=' ')
    print(f'{boletim[c][3]:}')
while True:
    n = int(input('Mostrar nota de qual aluno? (999 interompe): '))
    if n == 999:
        break
    else:
        print(f'Notas de {boletim[n][0]}: {boletim[n][1:3]}')
