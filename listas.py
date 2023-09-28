"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferança
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
        - Possuem tamanho e tipo de dado fixo;
         ou seja, nessas linguagens se você criar um arra do tipo int e com tamanho 5, este array
         será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Pyhton:

- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado;

As lista em Python são representadas por colchetes: []

Listas são mutáveis, ou seja, elas podem mudar constantemnte.

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elemnentos em listas

Para adicionar elementos em listas, utilizamos a função append

print(lista1)
lista1.append(42)
print(lista1)

# OBS: Com o append, nós só conseguimos adionar um elemento por vez
#  lista1.append(12, 34, 56)  #ERROR

lista1.append([8, 3, 1])  # Coloca a lista como elemento único(sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo valor')
print(lista1)

# Podemos facilmente juntar duas listas.

lista1 = lista1 + lista2
#  lista1.extend(lista2)
print(lista1)

# Forma 1
lista1.reverse()
lista2. reverse()

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista

print(len(lista1))

# Podemos remover facilmente o último elemento de uma lista
# OBS: O pop() não somente remove o último elemento, mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice
# OBS: os elemento a direita desse índice serão deslocados para a esquerda.
# OBS: se não houver elemento no índice informado, teremos o erro: IndexError.
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos, ou seja, zerar a lista
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo1

curso = 'Programação em Python essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: por padrão, o split() serpara os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python:','Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6 , coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6 , coloca o cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer dados em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 45678781]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 -> Utilizando for

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 -> Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada
#           0         1        2          3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento está ligado ao início da lista

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5])  # erro, pois não existe indice -5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes, mas também, úteis.

# Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual índice está o valor 6
print(numeros.index(6))

# Em qual indice está o valor 9
print(numeros.index(9))

# print(numeros.index(19)) gera ValueError
# OBS: caso não tenha esse valor na lista, será aprensentado erro ValueError

# OBS:Retorna o índice do primeiro elemento encontrado
print(numeros.index(5))

# Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1))  # buscando a partir do indice 1
print(numeros.index(5, 2))  # buscando a partir do indice 2
print(numeros.index(5, 3))  # buscando a partir do indice 3
# print(numeros.index(5, 4))  # buscando a partir do indice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(8, 3, 6))  # Buscar o indice do valor 8 entre os indices de valor de 3 a 6

# Revisão de slicing

# lista[inicio:fim:passo]

# range[inicio:fim:passo]

# Trabalhando com slicing de lista com parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:])  # Iniciando no indice 1 e pegando todos os elementos  restantes

# Trabalhando com slicing de lista com parâmetro 'fim'

print(lista[:2])  # começa em 0, pega até o indice 2 - 1

print(lista[:4])  # começa em 0, pega até o indice 4 -1

print(lista[1:3])  # começa em 1, pega até o indice 3 -1

# Trabalhando com slice de lista com parâmetro 'passo'

print(lista[1::2])  # Começa em 1, vai até o final de 2 em 2

print(lista[0::2])  # Começa em 0, vai até o final de 2 em 2

# Invertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nomes.reverse()
print(nomes)


# Soma*, valor maximo*, valor minimo*, tamanho

# * Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista))  # soma
print(max(lista))  # máximo valor
print(min(lista))  # mínimo valor
print(len(lista))  # tamanho da lista

# Tramsformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desenpacotamento de lista

lista =[1, 2, 3, 4]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: se tivermos um numero diferente de elementos na lista ou variáveis para receber os dados, teremos ValueError.

# Copiando uma lista para outra(Shallow copy e Deep copy)

# Forma1

lista =[1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos list.copy, copiamos dados de uma lista para um nova lista mas elas ficaram totalmente independentes,
# ou seja, modificando uma lista,não afeta a outra, isso em python é chamado de Deep copy (copia profunda).

# Forma 2 - Shallow copy

lista =[1, 2, 3]
print(lista)

nova = lista  # copia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a copia via atribuição, e copiamos os dados da lista para a nova lista, mas após realizar
# modificação em uma das listas, essa modificação se refletiu em ambas as lista, isso em Python é chamado de
# Shallow copy.
"""