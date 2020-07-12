# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se
# a expressão passada está com os parênteses abertos e fechados na ordem correta.

lista = []
lista.extend(str(input('Digite: ')))
cont_abrindo = cont_fechando = 0
if lista[0] == ')' or lista[-1] == '(':
        print('Sua expressão está errada.')
else:
    for c in lista:
        if c in '(':
            cont_abrindo += 1
        if c in ')':
            cont_fechando += 1
    if cont_abrindo == cont_fechando:
        print('Sua expressão está correta.')
    else:
        print('Sua expresão está errada.')