# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:
#       Quantas pessoas foram cadastradas
#       A média de idade do grupo
#       Uma lista com todas as mulheres
#       Uma lista com todas as pessoas com idade acima da média

todos = []
pessoa = {}
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: '))
        if pessoa['sexo'] not in 'mMfF':
            print('ERRO! Por favor, digite apenas M ou F.')
        else:
            break
    pessoa['idade'] = int(input('Idade: '))
    while True:
        r = str(input('Quer continuar? [S/N]: '))
        if r not in 'sSnN':
            print('ERRO! Digite apenas S ou N.')
        else:
            break
    todos.append(pessoa.copy())
    if r in 'nN':
        break
somaidade = 0
for p in todos:
    somaidade += p['idade']
mediaidade = somaidade / len(todos)
print('='*30)
print(f'Ao todo temos {len(todos)} pessoas.')
print(f'A média de idade é de {mediaidade} anos.')
print('As mulheres cadastradas foram ', end='')
for c in todos:
    if c['sexo'] in 'fF':
        print(c['nome'], end=' ')
print('\nLista das pessoas que estão acima da média de idade:')
for i in todos:
    if i['idade'] > mediaidade:
        print(f'    nome = {i["nome"]}; sexo = {i["sexo"]}; idade = {i["idade"]}')
