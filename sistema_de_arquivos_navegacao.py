"""
Sistema de arquivos e Navegação

Para fazer uso de manipulação de arquivos do sistema operacional, precisamos importar
e fazer uso do módulo os.

os - Operating System - Sistema Operacional

# fazer import

import os

# getcwd() - pega o current work directory - diretorio de trabalho corrente
# Retorna o path (caminho absoluto)
print(os.getcwd())  #

# Para mudar o diretorio podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('/home/geek/'))

# OBS: para usuário windows, terá que ter cuidado ao verificar diretórios

print(os.path.isabs('C:\\Users\\geek/'))


# Podemos identificar o sistema operacional com o módulo os
print(os.name)  # posix ( linux/mac), nt(windows)

import sys

print(sys.platform)

# juntando os diretorios

print(os.getcwd())  #

res = os.path.join(os.getcwd(), 'geek', 'university')

os.chdir(res)

print(os.getcwd())  #

# Veja que o os.path.join() recebe dois parametros, sendo o diretorios atual e o segundo que será juntado ao atual

# Podemos listar os arquivos e diretórios com listdir()

print(len(os.listdir('C:\\')))
"""

import os

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

scanner = os.scandir()

arquivos = list(os.scandir('C:\\'))

#print(arquivos)
#print(dir(arquivos[0]))

print(arquivos[0].inode())
print(arquivos[0].is_dir())
print(arquivos[0].is_file())
print(arquivos[0].is_symlink())
print(arquivos[0].name)  # Nome do arquivo
print(arquivos[0].path)
print(arquivos[0].stat())

# OBS: Quando utilizamos a função scandir() nós precisamo fecha-la, assim quando abrimos um arquivo

scanner.close()
