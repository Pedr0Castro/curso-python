"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The zen of Python

Import this

A ideia da PEP8 é que possamos escrever códigos Python de forma pythônica.

[1] . Utilize Camel Case para nomes  de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] . Utilize nomes em minúsculo, separados por underline para funções ou variáveis;
def soma()
    pass


def soma_dois()
    pass


numero = 4

numero_impar = 5

[3] . Utilize 4 espaços para identação!

if 'a' in 'banana':
    print('tem')

[4] . linhas em branco
-  Separar funções em definições de classe com duas linhas em branco;
- Métodos dentro de uma classe devem ser separados com uma única linha em branco
[5] . Imports
- Imports devem ser sempre feitos em linhas separadas;
# import errado

import sys, os

# Import certo

import sys
import os

# não há problemas em utilizar:

from types import StringType, ListType

# caso tenha muitos imports de um mesmo pacote recomenda-se fazer:
from types import (
    StringType,
    ListType,
    SetType,
    OutroType,
)
# Imports devem ser colocados no topo do arquivos, logo depois de qualquer comentários ou docstrings e
# antes de constantes ou variáveis globais.

[6] . Espaços em expressões e instruções
# Não faça:
funcao( algo[ 1 ], { outro: 2 } )

# faça:
funcao(algo[1], {outro: 2})

# Não faça:
algo (1)

# Faça:
algo(1)
# Não faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não faça:

x        =1
y        =3

# faça:
x = 1
y = 3
[7] . Termine sempre uma instrução com uma nova linha;
"""
import this




