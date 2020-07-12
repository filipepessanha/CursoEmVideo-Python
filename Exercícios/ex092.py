# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um
# dicionário. Se, por acaso, a CTPS for diferente de ZERO, o dicionário receberá, também, o ano de contratação e o
# salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import date
dados = {}
dados['Nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['Idade'] = date.today().year - ano_nasc
ctps = int(input('Carteira de trabalho (0 não tem): '))
if ctps > 0:
    dados['CTPS'] = ctps
    dados['Ano de contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = dados['Ano de contratação'] - ano_nasc + 35
else:
    dados['CTPS'] = 'Não disponível'
print('='*30)
for k, v in dados.items():
    print(f'{k}: {v}')
