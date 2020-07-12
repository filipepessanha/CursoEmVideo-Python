# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.

turma = {}
turma['Nome'] = str(input('Nome: '))
turma['Média'] = float(input('Média: '))
if turma['Média'] >= 7.0:
	turma['Situação'] = 'APROVADO'
elif 5.0 <= turma['Média'] < 7.0:
	turma['Situação'] = 'RECUPERAÇÃO'
else:
	turma['Situação'] = 'REPROVADO'
print('='*30)
for k, v in turma.items():
	print(f'{k}: {v}')
