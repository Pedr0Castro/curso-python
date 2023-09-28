"""
Reversed

Obs: Não confunda com a função reverse() que estudamos nas listas.

A função reverse() só funciona em listas, já a função reversed() funciona com qualquer iterável

Sua função é inverter o iterável.

A função reversed retorna um iterável chamado list_reverseiterator

"""

# Exemplso

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# podemos converter o elemento retornado para um lista, tupla ou conjuntos

# LISTA
print(list(reversed(lista)))

# TUPLA
print(tuple(reversed(lista)))

# Em conjuntos, não definimos a ordem dos elementos
# Conjunto
print(set(reversed(lista)))

# Podemos iterar sobre o reversed

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')

# Podemos fzer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais facil com o slice de strings
print('Geek University'[::-1])

# Podemos também utilizar o reversed() ppara fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)

# apesar que também ja vimos como fazer isso utilizando o proprio range
for n in range(9, -1, -1):
    print(n)

