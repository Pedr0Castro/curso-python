"""
PDB - Python debugger

bug - inseto

# OBS: a utilização do print para debuggar é ruim

def dividir(a, b):
    print(f'a={a}, b={b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


print(dividir(4, 7))

# Existem formas mais profissionais, utilizando o debugger
# Em python, podemos fazer isso em diferentes IDEs

# Exemplo Pycharm

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo com pdb - Python Debugger

# Precisamos importar a biblioteca pdb e entao utilizar a função set_trace()

# Comandos básicos do pdb
# l (listar onde estamos no código)
# n ( proxima linha)
# p (imprime variavel)
# c ( continua a execução - finaliza o debuggin)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie '
import pdb; pdb.set_trace()
nome_completo = nome + '' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' Faz o curso ' + curso
print(final)

# Por que utilizar este formato
# o debug  é utilizado durante o desenvolvimento. Costumamos realizar todos os imports de bibliotecas
# no inicio do arquivo. Por isso, ao inves de colocarmos o import do pdb no incio do arquivo,
# nós colocamos somente  onde vamos debuggar, e ao finalizar  já fazemos a remoção.

# Exemplo com pdb - Python Debugger - 3

# Precisamos importar a biblioteca pdb e entao utilizar a função set_trace()

# A partir do python 3.7 não precisa mais importar a biblioteca pdb, pois o comando de debug foi incorporado

# Comandos básicos do pdb
# l (listar onde estamos no código)
# n ( proxima linha)
# p (imprime variavel)
# c ( continua a execução - finaliza o debuggin)

import pdb

nome = 'Angelina'
sobrenome = 'Jolie '
breakpoint()
nome_completo = nome + '' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + ' Faz o curso ' + curso
print(final)

# OBS: cuidado com conflitos entre nomes de variaveis e os comandos de pdb


def soma (l, n, p, c):
    breakpoint()
    return l + n + p + c


print(soma(1, 3, 5, 7))

# como os nomes das variaveis são o mesmo dos comandos, devemos utilizar o comando p pra imprimir o valor das variaveis.

# Nada de colocar nomes não representativo em variaveis. Sempre optar por nomes significativos


def soma (num1, num2, num3, num4):
    breakpoint()
    return num1 + num2 + num3 + num4

"""

