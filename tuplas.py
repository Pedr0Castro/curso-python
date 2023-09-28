"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas.

Existem basicamentes duas diferenças básicas:

1 - As Tuplas são representadas por parenteses ()

2- As Tuplas são imutáveis: Ao se criar uma tupla ela não muda. Toda
opreção em uma tupla gera uma nova tupla.

# Cuidado 1: as tuplas são repesentadas por parentese, mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4)  # Isso não é uma tupla!
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # isso é uma tupla!
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla5)

print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula, e não pelo uso dos parenteses.

(4) -> Não é Tupla
(4,0) -> é tupla
4, -> é tupla

# podemos gerar uma tupla dinamicamente com range(incio,fim,passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de Tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: gerar ero, ValurError se colocarmos um número diferentes para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor maximo*, valor minimo* e tamanho

# * se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # Tupla são imutáveis

print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2  # Tuplas são imutáveis mas podemos sobrescrever seus valores
print(tupla1)

# verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)

print(3 in tupla)

# Iterando sobre uma Tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

    # Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('a'))

escola = tuple('Geek University')
print(escola)

print(escola.count('e'))


# Dicas na utilização de tuplas

# Devemos utilizar tuplas sempre que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1:

meses = ('Janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro','dezembro')


# Slicing

# Tupla(Inicio:fim:passo)

print(meses[5:9])

# O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i +1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('junho'))

# OBS: caso o elemento não exista será gerado ValueError.

# Por que utilizar tuplas?

# - Tupla são mais rápidas do que listas.
# - Tupla deixam seu código mais seguro.

# * Isso por que trabalhar com elementos imutáveis traz segurança para o código.

# Copiando uma tupla para a outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra

print(nova)
print(tupla)
"""


