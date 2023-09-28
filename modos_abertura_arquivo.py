"""
Modos de abertura de arquivos

r - Abre para leitura - padrao
w - abre para escrita - sobrescreve caso o arquivo ja exista
x - abre para escrita somente se o arquivo não existir
a - abre para escrita, adicionando o conteúdo ao final do arquivo. Com o modo a, não controlamos o cursor
+ - abre para o modo de atualização, leitura e escrita(temos o controle do cursor)

# OBS: abrindo no modo 'a' - append, se o arquvi não existir será criado, se ja existir, o novo conteúdo será adicionado
ao final
https://docs.python.org/3/library/functions.html#open

# Exemplo x
try:
    with open('university', 'x', encoding='utf-8') as arquivo:
        arquivo.write('Teste de conteúdo 2.\n')
except FileExistsError:
    print('Arquivo já existe')

# Exemplo a
with open('frutas.txt', 'a',  encoding='utf-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break

with open('outro.txt', 'r+',  encoding='utf-8') as arquivo:
   arquivo.seek(0)
   arquivo.write('Um Novo topo!\n')
   arquivo.write('Nova linha.\n')
   arquivo.write('Mais uma linha.\n')

"""

