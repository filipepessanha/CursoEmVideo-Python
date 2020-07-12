# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#   Ex: Ana Maria de Souza
# 	    primeiro = Ana
# 	    último = Souza

nome = str(input('Digite seu nome: ')).strip().split()
n = len(nome)
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[n-1]))

