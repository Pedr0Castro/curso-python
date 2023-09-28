"""
Funções de Maior Grandeza - Higher Order Functions - HOF

- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam
outras funções como resultado ou mesmo que podemos passar funções como argumentos para outras funções e
até mesmo criar variáveis do tipo de funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos  isso.

Em Python as funções são Cidadãos

# Exemplo - definindo as funções


def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))

# Nested Functions - Funções Aninhadas


# Em Python podemos também ter funções dentro de funções, que são conhecidas por Nested functions
# ou também Inner Functions (funções internas

from random import choice

def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma Daqui ', 'Gosto Muito de Você '))
    return humor() + pessoa

# TESTANDO


print(cumprimento('Pedro'))

print(cumprimento('Carlos'))

# Retornando funções de outras funções

from random import choice


def faz_me_rir():
    def rir():
        return choice(('hahahahahahaha', 'kkkkkkkkkkkkkk', 'yayayayayayaya'))
    return rir

# testando


rindo = faz_me_rir()
print(rindo())
"""

# Inner Functions Podem acessar o escopo de funções mais externas.

from random import choice


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lololololo', 'kkkkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())

print(rindo())

print(rindo())