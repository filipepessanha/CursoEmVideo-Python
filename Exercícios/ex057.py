# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
# peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M / F]: ')).strip().lower()
while sexo not in 'mf':
    print('--------------------------')
    print('Opção inválida')
    sexo = str(input('Informe seu sexo [M / F]: ')).strip().lower()
print('Sexo registrado com sucesso')
print('FIM')
