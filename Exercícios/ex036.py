# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
# da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
# ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa: R$'))
sal = float(input('Informe o salário do comprador: R$'))
prazo = int(input('Qual o prazo para pagamento em anos: '))

prazomensal = prazo * 12
vprest = casa / prazomensal

if vprest <= sal * 0.3:
    print('EMPRÉSTIMO APROVADO\n'
          'Número de prestações {}\n'
          'Valor das prestações R${:.2f}'.format(prazomensal, vprest))
else:
    print('EMPRÉSTIMO NEGADO\n'
          'As prestações ultrapassam 30% do seu salário.')
