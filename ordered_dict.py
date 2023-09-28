"""
Módulo Collections: Ordered Dict

# Em um dicionário, a ordem de inserção dos elemento não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')

OrderedDict é um dicionário, que nos garante a ordem de inserção dos elementos.

# Fazer import
from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5})

for chave, valor in dicionario.items():
    print(f'chave={chave}:valor={valor}')
"""

from collections import OrderedDict

# Entendendo a diferença entre Dict e Ordered Dict

dict1 = {'a': 1, 'b':2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2)  # Tue -> Já que a ordem dos elementos não importa para o dicionário

# Ordered Dict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2)  # False -> Já que a ordem dos elementos importa para o Ordered Dict
