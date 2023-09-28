"""
O block try/except
Utilizamos o bloco try/except para tratar erros que podem ocorrer no nosso codigo,
prevenindo assim que o programa pare de funcionar e o usuario receba mensagem de erros inesperados.

A forma geral mais simples é:

try:
    //execução problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro generico

try:
    geek()
except:
    print('Deu algum problema')

# tente executar a função geek(), caso voce encontre erros, imprima a mensagem erro.

# Exemplo 2 - Tratando um erro generico

try:
    len(5)
except:
    print('Deu algum problema')

# tente executar a função geek(), caso voce encontre erros, imprima a mensagem erro.

OBS: tratar erro de forma generica, não é a melhor forma de tratamento de erros, o ideal é sempre tratar de forma
específica

# Exemplo 3 - Tratando um erro específico

try:
    geek()
except NameError:
    print('Você está utilizando uma função inexistente')

# Exemplo 4 - Tratando um erro específico

try:
    len()
except TypeError:
    print('Você está utilizando uma função inexistente')

# Exemplo 5 - Tratando um erro específico com detalhes do erro

try:
    len()
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')

# Podemos efetuar diversos tratamentos de erros de uma vez.

try:
    geek()
except NameError as erra:
    print(f'Deu NameError: {erra}')
except TypeError as errb:
    print(f'Deu TypeError: {errb}')
except:
    print('Deu um erro diferente')



"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except TypeError:
        return None

dic = {"nome": 'Geek'}

print(pega_valor(dic, 8))
