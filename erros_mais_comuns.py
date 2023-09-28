"""
Erros mais comuns em Python

É importante prestar atenção e aprender a ler as saidas de erros geradas pela execução
do nosso codigo

Os erros mais comuns

SyntaxError - occore quando o pyhton encontra um erro de sintaxe

# Exemplos SyntaxError

a) def funcao:
    print('Geek university')

b)

def = 1

c)

return

2 - NameError - ocorre quando uma variavel ou função não foi definida

# Exemplos NameError

a)
print(geek)

b)
geek()

3 - TypeError - ocorre quando uma função/opreção/ação é aplicada a um tipo errado.

# Exemplos TypeError

a)
print(len(5))

b)
print('Geek' + [])

4- IndexError - ocorre quando tentamos acessar um elemento em uma lista  ou outro tipo de dado indexado utilizando
um indice invalido

# Exemplos IndexError

# a)

lista = ['Geek']
print(lista[0])

b)
# a)

lista = ['Geek']
print(lista[0][10])

5 - ValueError - ocorre quando uma função/operação Built-in (integrada) recebe um argumento  com tipo correto
mas valor inapropriado

# Exemplos ValueError

a)
print(int('Geek'))

6- KeyError - Ocorre quando tentamos acessar um dicionario com uma chave que não existe

# Exemplos KeyError

a)
dic = {'python': 'University'}
print(dic['geek'])

7- AttributeError - ocorre quando uma variavel não tem um atributo/função.

a)
tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError - ocorre quando não respeitamos a identação do Python (4 espaços)

# Exemplos IdentationError

a)
def nova():
print('Geek')

b)
for i in range(10):
i + 1

OBS: EXCEPTIONS E ERROS são sinonimos na programação

obs: importante ler e prestar atenção na saida de erro.
"""


