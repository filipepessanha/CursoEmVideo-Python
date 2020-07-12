import estrutura
from arquivo import *

arq = 'ex115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    estrutura.cab('\033[32mMENU PRINCIPAL\033[m')
    resposta = estrutura.menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        estrutura.cab('\033[32mPESSOAS CADASTRADAS\033[m')
        lerArquivo(arq)
    elif resposta == 2:
        estrutura.cab('\033[32mNOVO CADASTRO\033[m')
        nome = str(input('Nome: '))
        idade = estrutura.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        estrutura.cab('\033[32mSaindo do sistema... Até logo!\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
