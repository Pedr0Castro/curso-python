"""
StringIO

Atenção: Para ler ou escrever dados em arquivos dos sitesmas operacional o software precisa ter
permissão:
    - Permissão de leitura para ler o arquivo.
    - permissão de escrita para escrever o arquivo


StringIo - Utilizado para ler e criar arquivos em memória.
"""

# Primeiro fazemos o import

from io import StringIO

mensagem = 'Esta é apenas uma string normal.'

# PODEMOS criar um arquivo em memória já com uma string inserida, ou mesmo vazio para inserirmos texto depois.

arquivo = StringIO(mensagem)
# arquivpo = open('arquivo.txt', 'w')


# agora tendo o arquivo, podemos utilizar tudo que ja sabemso
print(arquivo.read())

# Escrevendo outros textos
arquivo.write(' Outro texto.\n')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
