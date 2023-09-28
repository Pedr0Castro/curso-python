"""
Modulo Collections - Counter (contador)

Collections -> High performance container datetypes


conter -> Recebe um iterável como parametro e cria uma objeto do tipo collections counter que é
parecido com um dicionário, contendo como chave o elemento da lista passada como parametro e como
valor a quantidade de ocorrencias desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iterável, qui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))

print(res)

# Counter({1: 5, 2: 4, 3: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrencias.

# Exemplo 2

print(Counter('Geek University'))

# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

from collections import Counter

# Exemplo 3

texto = """ O USS Massachusetts é um encouraçado da classe Indiana e o segundo navio da Marinha dos Estados Unidos 
comparável aos navios de guerra estrangeiros de seu tempo. Autorizado em 1890 e comissionado seis anos depois, era um
encouraçado de pequeno porte, embora possuísse blindagem e artilharia pesados. A classe de navios a que pertencia 
também foi pioneira no uso de uma bateria intermediária. Ele foi projetado para defesa costeira e, como resultado, seus
decks não estavam a salvo de ondas altas em mar aberto. """

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencias no texto
print(res.most_common(5))
