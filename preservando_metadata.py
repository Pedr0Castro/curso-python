"""
Preservando metadatas com wraps

Metadados -> São dados intrisecos em arquivos

wraps - são funções que envolvem elementos com diversas finalidades

# problema

def ver_log(funcao):
    def logar(*args, **Kwargs):
        # Eu sou uma função (logar) dentro de outra
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **Kwargs)
    return logar



@ver_log
def soma(a, b):
    # Soma dois números.
    return a + b

# print(soma(10, 30))

print(soma.__name__)

print(soma.__doc__)

"""

# Resolução do problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **Kwargs):
        """ Eu sou uma função (logar) dentro de outra   """
        print(f'Você está chamando {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **Kwargs)
    return logar



@ver_log
def soma(a, b):
    """Soma dois números."""
    return a + b


print(soma(10, 30))

print(soma.__name__)

print(soma.__doc__)

print(help(soma))
