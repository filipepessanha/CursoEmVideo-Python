# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa
# progressão.

a = int(input('Digite um número: '))
r = int(input('Digite a razão da PA: '))

# Enésimo termo da PA se dá pela fórmula: a(termo) = a + (termo * 10) x razão

for n in range(a, a+(10-1)*r, r):
    print(n, end=' ')
