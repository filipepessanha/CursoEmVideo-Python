# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
# se o usuário quer ou não continuar. No final, mostre:
# - quantas pessoas tem mais de 18 anos
# - quantos homens foram cadastrados
# - quantas mulheres tem menos de 20 anos

contid = conth = contm = contm20 = 0
while True:
    print('-'*40)
    print('Cadastre uma pessoa')
    print('-'*40)
    idade = int(input('Digite a idade: '))
    sexo = ''
    while sexo not in ['m', 'f']:
        sexo = str(input('Digite o sexo [F/M]: ')).strip().lower()
    if idade > 18:
        contid += 1
    if sexo == 'm':
        conth += 1
    if sexo == 'f':
        contm += 1
        if idade < 20:
            contm20 += 1
    print('-'*40)
    mais = ''
    while mais not in ['s', 'n']:
        mais = str(input('Deseja cadastrar mais um nome? [S/N]: ')).strip().lower()
        if mais not in ['s', 'n']:
            print('Opção inválida.')
    if mais == 'n':
        if contid == 1:
            print('Foi cadastrada apenas 1 pessoa com mais de 18 anos.')
        else:
            print(f'Foram cadastradas {contid} pessoas com mais de 18 anos.')
        if conth == 1:
            print('Foi cadastrada apenas 1 homem.')
        elif conth == 0:
            print('Nenhum homem foi cadastrado.')
        else:
            print(f'Foram cadastrados {conth} homens.')
        if contm == 1:
            print('Foi cadastrado apenas 1 mulher com menos de 20 anos.')
        elif contm == 0:
            print('Nenhuma mulher foi cadastrada.')
        elif contm20 == 0:
            print('Nenhuma mulher com menos de 20 anos foi cadastrada.')
        else:
            print(f'Foram cadastradas {contm20} com menos de 20 anos. ')
        break