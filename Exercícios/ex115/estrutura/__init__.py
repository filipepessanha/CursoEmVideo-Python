def leiaInt(n):
    while True:
        try:
            a = int(input(n))
        except (ValueError, TypeError):
            print('\033[31mERRO: Digite um número inteiro válido\033[m')
            continue
        else:
            return a


def linha(tam=50):
    print('-' * tam)


def cab(txt, tam=50):
    linha(tam)
    print(txt.center(tam))
    linha(tam)


def menu(lista):
    for c, i in enumerate(lista):
        print(f'\033[32m{c+1}\033[m - \033[34m{i}\033[m')
    linha()
    op = leiaInt('\033[32mSua opção: \033[m')
    return op


def entrada(nome, idade):
    cadastro = dict()
    cadastro[nome] = idade
    print(f'Novo registro de {nome} criado.')
    print(cadastro)
