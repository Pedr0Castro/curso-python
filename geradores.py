"""
Geradores

- Geradores são iteradores :
obs: ao contrario não é verdadeiro, ou seja, nem todo iterator é um generator.

- generators podem ser criados com funções geradoras;
- funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões geradoras;

Diferenças entre funções e generators functions(funções geradoras)

------------------------------------------------------------------------------------
| Funções                                 | Generators Functions                   |
------------------------------------------------------------------------------------
|utilizam return                          | utilizam yield                         |
------------------------------------------------------------------------------------
| retorna uma vez                         | podem utilizar yield mútilplas vezes   |
------------------------------------------------------------------------------------
| quando executada, retorna valor         | quando executada, retorna um generator |
------------------------------------------------------------------------------------

gen = conta_ate(5)

for num in gen:
    print(num)

# print(type(gen))

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))  # 1

print('Geek')

for num in gen:
    print(num)
"""

# Exemplo de Generator function

def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador = contador + 1

# obs: uma Generator function não é generator. Ela gera um generator


# Gerar todos de uma vez

gen = list(conta_ate(10))

print(gen)


