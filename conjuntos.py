"""
conjuntos

- conjuntos em qualquer linguagem de programação, estamos fazendo referencia à teoria dos conjuntos
da matemática.

- Aqui no Python os conjuntos são chamados de sets.

dito isto, da mesma forma que na matematica:

-Sets(conjuntos) não possuem valores duplicados;
-Sets(conjuntos) não possuem valores ordenados;
- elementos não são acessados via indice,ou seja, conjuntos não são indexados;

conjuntos são bons para se utilizar quando precisamos armazenar elementos
 mas não nos importamos com as ordenações deles. Quando não precisamos se
 preocupar com chaves, valores e itens duplicados.

Os conjuntos(sets) são referenciados em Python com chaves {}

Diferença entre conjuntos (sets) e mapas (dicionarios) em Python:

     - Um dicionario tem chave/valor;
     -um conjunto tem valor;

# Definindo um conjunto:

# Forma 1

s= set ({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare aqui, que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor ja existente, o mesmo será ignorado
# sem gerar erros e não fará parte do conjunto

# Forma 2 -  Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que além de não termos valores duplicados, não temos ordem.

# Lista aceitam valores duplicados entao temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

# tuplas aceitam valores duplicados entao temos 10 elementos
tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(lista)} elementos')

# Dicionários não aceitam valores duplicados entao temos 8 elementos
dicionario = {}.fromkeys ([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'dicionario: {dicionario} com {len(lista)} elementos')

# conjuntos não aceitam valores duplicados entao temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(lista)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com Sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu, e  os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter
# repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidade distintas, ou seja, unicas nós temos.

# O que você faria? faria um loop na lista...?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elemento em um conjunto

s= {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gerar erro, é simplesmente ignorada
print(s)

# Remover elemento em um conjunto

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # Não é indice, informamos o valor a ser removido

print(s)

# Forma 2

s.discard(2)

print(s)

# OBS: se o valor não for encontrado, nenhum erro é gerado.

# Forma 1 - Deep copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Forma 2 - Shallow copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos resolver todos os itens de um conjunto

s.clear()
print(s)

estudantes_python = {'Marcos', 'Patricia', 'Eleen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Precisamos gerar um conjunto com nome de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe  |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Métodos matemáticos de conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um
# contendo estudantes de curso Java.

# Gerar um conjunto de estudantes de um curso que não estão no outro

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)
"""

# Soma*, Valor maximo*, valor minimo*, tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

