"""
Decorators com diferentes assinaturas

# Relembrando

def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# testando


# print(saudacao('The biuga'))

print(ordenar('Picanha', 'Batata frita'))

# Para resolver utilizamos um padrão de projeto chamado Decorator Pattern

A assinatura de uma função é representada pelo seu retorno, nome e parametros de entrada

# Refatorando com a decorator Pattern


def gritar(funcao):
    def aumentar(*args, **Kwargs):
        return funcao(*args, **Kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

# testando


# print(saudacao('The biuga'))

print(ordenar('Picanha', 'Batata frita'))

@gritar
def lol():
    return 'lol'

print(lol())

# OBS: Vale lembrar que podemos utilizar parametros nomeados

print(ordenar(acompanhamento='Batata frita', principal='Picanha'))
"""

# decorator com argumentos

def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **Kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **Kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)

@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# testando

print(soma_dez(10, 12))  #22

print(soma_dez(1, 21))

print(comida_favorita('pizza', 'churrasco'))

print(comida_favorita('sanduiche', 'pizza'))
