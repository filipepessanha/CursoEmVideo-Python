# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o
# valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


def dobro(n=0, form=False):
    res = n * 2
    return res if not form else moeda(res)


def metade(n=0, form=False):
    res = n / 2
    return res if not form else moeda(res)


def aumentar(n=0, t=0, form=False):
    res = n + (n * t / 100)
    return res if not form else moeda(res)


def reduzir(n=0, t=0, form=False):
    res = n - (n * t / 100)
    return res if not form else moeda(res)


def moeda(n=0, r='R$'):
    res = f'{r}{n:.2f}'.replace('.', ',')
    return res


def resumo(n=0, aum=10, red=5):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    formatar('Preço analisado:', moeda(n))
    formatar('Dobro do preço:', dobro(n, True))
    formatar('Metade do preço:', metade(n, True))
    formatar(f'{aum}% de aumento:', aumentar(n, aum, True))
    formatar(f'{red}% de redução:', reduzir(n, red, True))
    print('-' * 30)


def formatar(n, f):
    print(f'{n:<20} {f}')
