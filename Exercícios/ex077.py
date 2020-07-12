palavras = ('gato', 'cachorro', 'papagaio', 'periquito', 'andorinha', 'ra')
a = ('a', 'e', 'i', 'o', 'u')
for nome in palavras:
    print(f'Na palavra {nome.upper()} temos ', end='')
    for letra in nome:
        if letra == a[0]:
            print(letra, end=' ')
        if letra == a[1]:
            print(letra, end=' ')
        if letra == a[2]:
            print(letra, end=' ')
        if letra == a[3]:
            print(letra, end=' ')
        if letra == a[4]:
            print(letra, end=' ')
    print()
