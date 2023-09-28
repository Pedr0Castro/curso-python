"""
Sorted

OBS: não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort() só
funciona em lista.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

OBS: o sorted() sempre retorna uma lista com os elementos do iterável ordenados

# Exemplo

numeros = {6, 1, 8, 2}
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = [6, 1, 8, 2]
print(numeros)

print(tuple(sorted(numeros)))
# Adicionando parametros ao sorted()

print(sorted(numeros, reverse=True))  # ordena do maior para o menor

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": [], "cor": "amarelo"},
    {"username": "dogo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], "cor": "preto", "musica": "rock"}
]

print(usuarios)

# Ordenando pelo username
print(sorted(usuarios, key=lambda usuario: usuario["username"]))

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario["tweets"])))
"""

# Ultimo exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead skin mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll", "tocou": 32}
]

# Ordena da menos do cada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais do cada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
