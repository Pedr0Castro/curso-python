"""
Levantando os próprios erros com raise

raise -> Lança exceções

obs: raise não é uma função, é uma palavra reservada, assim como ref ou qualquer outra em Pyhton

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    print(f'O Texto {texto} será impresso na cor {cor}')


colore('Geek', 4)

# Exemplo real - REFATORADO


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre: {cores}')
    print(f'O Texto {texto} será impresso na cor {cor}')


colore('Geek University', 'preto')

OBS: o raise assim como o return finaliza a função, nada após o raise será executado
"""


