# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número
# de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


"""A exceção 'KeyboardInterrupt' não estava funcionando na ocasião em que este exercício foi feito e,
por esse motivo, não foi inserido no programa """


def leiaInt(n):
    while True:
        try:
            a = int(input(n))
        except (ValueError, TypeError):
            print('ERRO: Digite um número inteiro válido')
            continue
        else:
            return a


def leiaFloat(n):
    while True:
        try:
            a = float(input(n))
        except (ValueError, TypeError):
            print('ERRO: Digite um número real válido')
            continue
        else:
            return a


i = leiaInt('Digite um número Inteiro: ')
r = leiaFloat('Digite um número Real: ')
print(f'O número inteiro é {i} e o real é {r}.')

