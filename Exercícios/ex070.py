# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai
# continuar. No final, mostre:
# - qual é o total gasto na compra
# - quantos produtos custam mais de R$1000
# - qual é o nome do produto mais barato

contprodutos = valortotal = cont = valorbarato = 0
while True:
    produto = str(input('Informe o produto: '))
    valor = float(input('Informe o preço: R$'))
    maisprodutos = str(input('Deseja cadastrar outro produto? [S/N]: '))
    cont += 1
    valortotal += valor
    if valor > 1000:
        contprodutos += 1
    if cont == 1:
        valorbarato = valor
    else:
        if valor < valorbarato:
            valorbarato = valor
    if maisprodutos == 'n':
        print(f'O total gasto na compra foi R${valortotal}.')
        print(f'Foram {contprodutos} produtos acima de R$1000.00.')
        print(f'O produto mais barato foi {valorbarato}.')
        break
