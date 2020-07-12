# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Digite a medida em metros: "))
cm = m*100
mm = m*1000

print('{:.2f} metros é igual a: {:.2f} centímetros e {:.2f} milímetros'.format(m, cm, mm))
