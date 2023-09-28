"""
Sistema de arquivos - manipulação

# descobrindo se um arquivo ou diretorio existe

print(os.path.exists('arquivo.txt'))
print(os.path.exists('frutas.txt'))


# Diretorio

# path relativos
print(os.path.exists('geek'))
print(os.path.exists('geek/university'))
print(os.path.exists('outro'))

# path absoluto
print(os.path.exists('/home/geek/university'))
print(os.path.exists('C:\\Users\\phmor\\PycharmProjects\\guppe'))

# Criando arquivos

# forma 1
open('arquivo-teste.txt', 'w', encoding='utf-8').close()

# forma 2
open('arquivo-teste2.txt', 'a', encoding='utf-8').close()

# forma 3

with open('arquivo-teste3.txt', 'w', encoding='utf-8') as arquivo:
    pass


# Criando arquivos


os.mknod('C:\\Users\\phmor\\PycharmProjects\\guppe\\geek')

# Criando diretórios - unicos(um a um)

# Path Relativo
os.mkdir('templates')

# Path Absoluto

os.mkdir('C:\\Users\\phmor\\PycharmProjects\\guppe\\geek\\templates')

# OBS: a função mkdir() cria um diretório se este não existir. Caso exista, teremos FileExistError

# Criando muilti-diretórios (árvore de diretórios)
os.makedirs('tamplates/geek/univeristy')

# OBS: Se ja existir teremos um FileExistError


os.makedirs('tamplates/novo2/outro2', exist_ok=True)

# diretórios

os.rename('geek', 'geek2')

# Obs: se o diretório que queremos renomear não estiver vazio, teremos um OSerror

# Arquivos

os.rename('geek2/templates', 'geek.txt')

# Tome cuidado com os comandos de deleção. Ao deletarmos um arquivos ou diretórios, eles não vão para lixeira, eles somem.

os.remove('geek.txt')

# OBS: se estiver no windows e o arquivo que deletar estiver em uso, você terá um erro.

# caso não exista, teremos o FileNotFoundError

# OBS: se informar um diretório ao inves de arquivo, teremos um erro

# Removendo diretórios vazios

os.rmdir('tamplates')

# OBS: se o diretório tiver qualquer conteúdo teremos OSerror

# Removendo uma ávore de arquivos
for arquivo in os.scandir('geek2'):
    print(f'- {arquivo.name}')
    if arquivo.is_file():
        os.remove(arquivo.path)

import os
import tempfile

with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w', encoding='utf-8') as arquivo:
        arquivo.write('Geek University\n')
    input()

# estamos criando um diretório temporário, abrindo o mesmo dentro dele criando
# um arquivo para escrevermos um texto, no final usamos um input só para mantermos os arquivos temporários vivos dnetro do with.

"""

import os
import tempfile



