"""
Generator Expression

Em aulas anteriores nós estudamos:
 - List comprehension;
 - Dictionary comprehension;
 - Set comprehension;

Não Vimos:
 - Tuple Comprehension... porque ela se chamam Generators

 nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa]

print(any([nome[0] == 'C' for nome in nomes])

# Poderiamos ter feito usando Generator

nomes = ['Carlos', 'Camila', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# List Comprehension

res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# Qual é a utilizadade de getsizeof()? Retorna a quantidade de bytes em memória do elemento passado como parâmetro.
from sys import getsizeof

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupa
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(921321423432))

print(getsizeof(True))

from sys import getsizeof

# Gerando uma lista de números com list comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando um lista de numeros com Set comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória:')
print(f'Lista comprehension: {list_comp} bytes')
print(f'Lista comprehension: {set_comp} bytes')
print(f'Lista comprehension: {dic_comp} bytes')
print(f'Lista comprehension: {gen} bytes')
"""

# Iterando

gen = (x + 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)


