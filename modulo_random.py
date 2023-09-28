"""
Módulo Random e o que são módulos

- Em Python módulo nada mais são do que outros arquivos Python.

Módulo Random - possui varias funções para geração de números pseudo-aleatório.

# OBS: existem duas formas de utilizar um módulo ou funão deste

# Forma 1 - todo o módulo(não recomendado)

import random

# random() -> gera um número real pseudo-aleatório entre 0 e 1.

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# dentro do módulo ficarão disponiveis(ficarão em memória). Caso você saiba quais funções voce precisa utilizar
# deste módulo, então esta não seria a forma ideal de utilização

print(random.random())

# Veja  que para utilizar a função random() do pacote random, nós colocamos o nome do pacote e o nome da função,
# separados  por ponto.

# Não confunda a função random com o pacote random. a função random() é apenas uma função dentro do módulo random

# Forma 2 - importando uma função especifica do módulo

from random import random

# No import acima, estamos falando: do módulo random importe a função random

for n in range(10):
    print(random())

# uniform() -> Gerar um número real pseudo-aleaório entre os valores estabelecidos.

from random import uniform

for n in range(10):
    print(uniform(3, 7))  # 7 não é incluido

# randint() -> Gera valores pseudo-aleatorios entre os valores estabelecidos
from random import  randint
# Gerador de apostas para a mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # Começa em 1 e vai até 61

# choice() -> mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']

print(choice(jogadas))
"""
from random import shuffle
# shuffle() -> Tem a função de embaralhar dados

cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)

shuffle(cartas)

print(cartas[0])
