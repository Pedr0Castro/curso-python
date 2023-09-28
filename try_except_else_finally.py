"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

Toda entrada deve ser tratada!!

OBS: A função do usuário é destruir seu sistema

# Else - é executado somente se não ocorre o erro.

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')

# Finally

try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Você não digitou um valor válido')
else:
    print(f'Você digitou o número {num}')
finally:
    print('Executando finally')

# OBS: O bloco finally é sempre executado, independente se houve exceção ou nao.

# o finally é geralmente utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADO


def dividir(a, b):
    return a / b


num1 = int(input('Informe o primeiro número: '))

try:
    num2 = int(input('Infdorme o segundo número: '))
except ValueError:
    print('O valor precisa ser numerico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')

# Exemplo mais complexo Correto
# OBS: Você é responsavel pelas entradas das suas funções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

# Exemplo mais complexo - semi-generico
# OBS: Você é responsavel pelas entradas das suas funções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError)as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

"""

# Exemplo mais complexo - semi-generico
# OBS: Você é responsavel pelas entradas das suas funções.

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError)as err:
        return f'Ocorreu um problema: {err}'


num1 = input('Informe o primeiro número: ')
num2 = input('Informe o segundo número: ')

print(dividir(num1, num2))

