"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)

print(f'Média: {media}')

# OBS: assim como a fução map, a filter recebe dois parametros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))

print(f'Novamente: {list(res)}')

# OBS: Assim como, na função map após serem utilizados o dados de filter, eles são exluidos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)

res = filter(None, paises)

print(list(res))

# A diferença entre map e filter é :

# map - recebe dois parametros, uma função e um iteravel e retorna um objeto mapeando a função para cada elemento do iterável

# filter - recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando apenas os elementos de acordo com a função.

# Exemplo mais complexo

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "dogo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)

# Filtrar os usuários que estão inativos no twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""

# Combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))

print(lista)
