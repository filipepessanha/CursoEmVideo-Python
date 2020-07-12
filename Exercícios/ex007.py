# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Nota 1ºS: '))
n2 = float(input('Note 2ºS: '))
m = (n1+n2)/2

print('A média do aluno é: {:.1f}'.format(m))