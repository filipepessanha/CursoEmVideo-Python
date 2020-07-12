# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**(1/2)
# A uma exponenciação, como visto na variável 'r', pode ser escrita utilizando com a função 'pow()'.
# Isso ficaria da seguinte forma 'r = pow(n, (1/2))'

print('O número é {}.\nO dobro é {}\nO triplo é {}\nA raiz quadrada é {:.2f}'.format(n, d, t, r))
