"""
Any e All

All() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o interável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # True

print(all((1, 2, 3, 4)))  # True

print(all({1, 2, 3, 4}))  # True

print(all('Geek'))  # True


nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))

# obs: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all(letra for letra in 'eio' if letra in 'aeiou'))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any(nome[0] == 'C' for nome in nomes))

print(any(num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0))
