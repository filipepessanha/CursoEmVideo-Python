def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
    except:
        print('\033[31mERRO! Não foi possível criar o arquivo.\033[m')
    else:
        print(f'\033[36mArquivo {nome} criado com sucesso.\033[m')
        a.close()


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mERRO! Não foi possível ler o arquivo\033[m')
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mERRO! Não foi possível ler o arquivo.\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mERRO! Não foi possível registrar os dados.\033[m')
        else:
            print(f'\033[36mNovo registro de {nome} adicionado\033[m')
            a.close()
