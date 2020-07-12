# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.


def fatorial(num, show=True):
    """
    -> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (Opcional) Mostra o calculo realizado.
    :return: Retorna o resultado do cálculo.
    """
    f = 1
    print('=' * 50)
    for c in range(num, 0, -1):
        if show:
            print(c, 'x' if c > 1 else '=', end=' ')
        f *= c
    return f


print(fatorial(10, show=True))
help(fatorial)
