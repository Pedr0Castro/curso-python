"""
Entendendo o *args

- O args é um parâmetro como outro qualquer, isso significa que poderá chamar de qualquer coisa
desde que comece com asteristico.

Exemplo:

*xis

mas por converção, utilizamos *args para defini-lo

O parâmetro *args utilizado em uma função, coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

# Exemplos

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))

# Exemplos

def soma_todos_numeros(nome, email, *args):
    return sum(args)


print(soma_todos_numeros('Pedro', 'Castro'))
print(soma_todos_numeros('Pedro', 'Castro', 1))
print(soma_todos_numeros('Pedro', 'Castro', 2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))
print(soma_todos_numeros(23.5, 13.9))

# Outro exemplo de utilização do *args

def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem vindo Geek'
    return 'Eu não tenho certeza de quem você é ...'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(1, 'University', 3.145)
"""


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador

print(soma_todos_numeros(*numeros))

# OBS: o asteristico serve para que informemos o Python que estamos
# passando como argumento uma coleçao de dados. Desta forma, ele saberá
# que precisará desempacotar esses dados



