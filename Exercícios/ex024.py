# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra 'Santo'.

city = input('Digite o nome da cidade: ')
print('santo' in city.lower().split()[0])
