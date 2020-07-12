# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00 calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite seu salário: R$'))

if s > 1250:
    n = s + (s * 0.15)
else:
    n = s + (s * 0.10)

print('Seu novo salário é: R${:.2f}'.format(n))
