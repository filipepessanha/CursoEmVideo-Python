# 108. Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
# como um valor monetário formatado.


def dobro(n=0):
    res = n * 2
    return res


def metade(n=0):
    res = n / 2
    return res


def aumentar(n=0, t=0):
    res = n + (n * t / 100)
    return res


def reduzir(n=0, t=0):
    res = n - (n * t / 100)
    return res


def moeda(n=0, r='R$'):
    res = f'{r}{n:.2f}'.replace('.', ',')
    return res
