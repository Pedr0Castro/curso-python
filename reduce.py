"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos que importar
e utilizar essa função a partir do módulo 'functools'

Guido van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# E você tem uma função que recebe dois parametros

funcao(x, y):
    return x * y

Assim como map() e filter() a função reduce() receber dois parametros: a função e o iterável.

a função reduce(), funciona da seguinte forma:
    passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda o res.

    Isso é repetido até o final.
    passo3: res3 = f(res2, a4)
    .
    .
    .
    passo n: resn = f(resm, an)

Ou seja, em cada passo ela aplica a função, passando como primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente,poderiamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2, a3, a4, ...), an)


"""

# Como funciona na prática

# vamos utilizar a função reduce() para multiplicar todos os números de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parametros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal - preferível
res = 1
for n in dados:
    res = res * n

print(res)
