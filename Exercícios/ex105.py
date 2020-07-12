# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional)
# Adicione, também, as docstrings da função.


def notas(*n, sit=False):
    """
    > Cria um dicionário em que reune o total de notas a maior notas,
    a menor nota a média e, opcionalmente,  a situação do aluno.
    :param n: recebe as notas
    :param sit: (opcional) True para mostrar a situação (padrão False)
    :return: retorna a lista
    """
    a = dict()
    a['total'] = len(n)
    a['maior'] = max(n)
    a['menor'] = min(n)
    a['media'] = sum(n) / len(n)
    if sit:
        if a['media'] >= 7:
            a['situação'] = 'APROVADO'
        elif 5 <= a['media'] < 7:
            a['situação'] = 'RECUPERAÇÃO'
        else:
            a['situação'] = 'REPROVADO'
    return a


resp = notas(5.5, 2, 7.5, 8, 0, sit=True)
print(resp)
