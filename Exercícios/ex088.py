# Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
qnt = int(input('Quantos jogos você quer que eu sorteie?: '))
print()
for a in range(1, qnt+1):
	sorteio = []
	while len(sorteio) < 6:
		num = randint(1, 60)
		if num in sorteio:
			sorteio.pop()
		else:
			sorteio.append(num)
	print(f'Sorteio {a}: {sorted(sorteio)}')
	sleep(0.5)
