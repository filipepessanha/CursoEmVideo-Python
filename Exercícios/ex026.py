# Faça um programa que leia uma frase pelo teclado e mostre:
# -Quantas vezes aparece a letra 'A';
# -Em que posição ela aparece a primeira vez;
# -Em que posição ela aparece a última vez.

nome = str(input('Digite um nome: ')).strip().lower()
letra = str(input('Digite uma letra para analisar: ')).strip().lower()

print('A letra "{}" aparece {} vezes'.format(letra, nome.count(letra)))
print('A letra "{}" encontra-se pela primeira vez na posição {}'.format(letra, nome.find(letra)+1))
print('A letra "{}" encontra-se pela última vez na posição {}'.format(letra, nome.rfind(letra)+1))
