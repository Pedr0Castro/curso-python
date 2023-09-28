"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional:

# Exemplo de função onde a passagem de parâmetro seja opcional
print('Geek University')

print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado())

def exponencial(numero=4, potencia=2):
    return numero ** potencia

print(exponencial(2,3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3))   # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva a potencia informada pelo usuário

# OBS: se o usuário passar somente um parâmetro, este será atribuído ao parâmetro numero, e será calculado o quadrado deste numero;
# Se o usuário passar 2 arugumentos, o primeiro será atribuído ao parametro numeoro e o segundo ao parametro potencia. Então será
# calculada essa potência.

print(exponencial())

# OBS: Em funções Python os parametros com valores default devem sempre estar ao final da declaração.

# ERROR!
def teste(num=2, potencia):
    return num ** potencia

print(teste(6))

# outros exemplos
def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))  #TypeError
print(soma())  # TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))  # True
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Pedro'))

# Por que utilizar parâmetros com valores default?

- Nos permite ser mais flexiveis nas funçoes;
- Evita erros com parametros incorretos;
- nos permite trabalhar com exemplos mais legiveis de codigo;

# Quais tipos de dados podemos utilizar como valores defaut para parâmetros?

- qualquer tipo de dados:
    - numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funções e etc;

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

instrutor = 'Geek'  # Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferencia.

def diz_oi():
    prof = 'Geek'
    return f'Olá {prof}'

print(diz_oi())
print(prof)  # NameError

# Atenção com variáveis globais (se puder evitar, evite)

def incrementa():
    total = total + 1  # A variável local está sendo utilizada para processamento sem ter sido inicializada
    return total


print(incrementa())

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global

    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e também tem uma forma especial de escopo de variável

def fora():
    contador = 0
    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())

print(dentro())  # NameError
