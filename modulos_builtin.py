"""
Trabalhando com Módulos Builtin (módulo integrados, que já vem instalados no Python)

Python|Módulos builtin

# utilizando alias (apelidos) para módulo/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *

print(random())

# Importando todo o módulo

import random

print(random.random())

# utilizando alias (apelidos) para módulo/funções

from random import  randint as rdi

print(rdi(5, 89))

"""
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)

print(random())

print(randint(3, 7))

lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)

print(choice('University'))
