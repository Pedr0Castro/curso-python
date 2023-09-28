"""
Leitura de arquivos

Para ler o conteúdo de um arquivo em Python, utilizamos a função integrada open()

open() - a forma mais simples de utilização, nós passamos apenas um parametro de entrada,
que neste caso é o nome do arquivo a ser lido. Essa função retorna um _io.TextIOWrapper e é com ele que trabalhamos

https://docs.python.org/3/library/functions.html#open

obs: por padrão, a função open() abre o arquivo para leitura. Este arquivo deve existir,
ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

mode r - Modo de leitura r - read() - ler
"""

# Exemplo

arquivo = open('texto.txt', encoding='utf-8')

# print(arquivo)

# print(type(arquivo))

# Para ler o conteúdo de um arquivo, após a abertura, devemos utilizar a função read()

ret = arquivo.read()

print(type(ret))

print(ret)

print(arquivo.read())

# OBS: O python utiliza um recurso para trabalhar com os arquivos chamado cursor. Esse cursor,
# funciona como o cursor quando estamos escrevendo

# print(arquivo.read())

# OBS: a função read() lê todo o conteúdo do arquivo.
