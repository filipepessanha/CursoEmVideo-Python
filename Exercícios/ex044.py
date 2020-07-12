# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
# pagamento:
# -À vista dinheiro/cheque: 10% de desconto
# -À vista no cartão: 5% de desconto
# -Em até 2x no cartão: preço normal
# -3x ou mais no cartão: 20% de juros

print('-' * 50)
valor = float(input('Valor do produto: R$'))

# Juros e descontos
d10 = valor * 0.1
d5 = valor * 0.05
j = valor * 0.2

print('-' * 50)
print('FORMAS DE PAGAMENTO')
print('1) À vista dinheiro/cheque')
print('2) Cartão')
fdpagamento = int(input('Digite a forma de pagamento: '))

if fdpagamento == 1:
    print('-' * 50)
    print('TOTAL')
    print(f'Desconto (10%): R${d10:.2f}')
    print(f'Total: R${valor - d10:.2F}')
else:
    print('-' * 50)
    print('CONDIÇÃO DE PAGAMENTO')
    print('1) À vista')
    print('2) Parcelado')
    cond = int(input('Informe a condição de pagamento: '))
    if cond == 1:
        print('-' * 50)
        print('TOTAL')
        print(f'Desconto (5%): R${d5:.2f}')
        print(f'Total: R${valor - d5:.2F}')
    else:
        print('PARCELAMENTO')
        print('-' * 50)
        print('1) 2x sem juros')
        print('2) 3x com juros de 20%')
        print('3) 4x com juros de 20%')
        print('4) 5x com juros de 20%')
        parc = int(input('Digite a opção de parcelamento: '))
        if parc == 1:
            print('-' * 50)
            print('TOTAL')
            print('Forma de pagamento não elegível para desconto')
            print(f'Total R${valor:.2f}')
        elif parc >= 2:
            print('-' * 50)
            print('TOTAL')
            print('Juros (20%): R${}'.format(j))
            print(f'Total R${valor + j:.2f}')
