"""
Seek e Cursors

seek() - é utilizada para movimentar o cursor pelo arquivo

arquivo = open('texto.txt', encoding='utf-8')

print(arquivo.read())

# seek() - ela recebe um parametro que indica onde queremos colocar o cursor
# Movimentando o cursor pelo arquivo

arquivo.seek(0)

print(arquivo.read())

arquivo.seek(22)

print(arquivo.read())

# readline() - função que lê o arquivo linha a linha

ret = arquivo.readline()

print(type(ret))

print(ret)

print(ret.split(' '))

# readlines()

linhas = arquivo.readlines()

print(len(linhas))

# OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o arquivo
no disco do computador e o nosso programa. Essa conexão é chamada de streaming. Ao finalizar
os trabalhos com o arquivo, devemos fechar essa conexão. Para isso utilizamos a função close()

Passos para se trabalhar com o arquivo

1- abrir o arquivo;

2- trabalhar o arquivo;

3- fechar o arquivo;

# 1 - abrir o arquivo
arquivo = open('texto.txt', encoding='utf-8')

# 2 - trabalhar o arquivo
print(arquivo.read())

print(arquivo.closed)  # Verifica se o arquivo está aberto ou fechado


# 3 fechar o arquivo
arquivo.close()

print(arquivo.closed)

# OBS: se tentarmos manipular o arquivo após seu fechamento teremos um ValueError
"""

arquivo = open('texto.txt', encoding='utf-8')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos no arquivo
print(arquivo.read(50))


