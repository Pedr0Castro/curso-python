"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer geralmente temos:

entrada -> processamento -> saída

se  a gente pensar em uma função, ja sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Fefatorando uma função


def quadrado(numero):
    # return numero * numero
    return numero ** 2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

# Fefatorando uma função


def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o(a) {aniversariante}! ')


cantar_parabens('Pedro')

# Funções podem ter n parametros de entrada,ou seja, podemos receber como  entrada em uma função,
# quantos parametros forem necessários, eles são separados por vírgula.

# Exemplo 1


def soma(a,b):
    return a + b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))

print(multiplica(2, 2))
print(multiplica(2, 5))

print(outra(1, 3, 'Oi '))
print(outra(5, 4, 'Python '))


# obs: se informar um número errado de parâmetro ou argumentos, teremos TypeError.

# print(soma(2, 3, 4))  # TypeError argumentos a mais
# print(soma(4))  # TypeError argumentos a menos

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Pedro', 'Castro'))

# A diferença entre parâmetros e argumentos

# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante uma execussão de uma função;

# A ordem dos parâmetro importa!

nome = 'Pedro'
sobrenome = 'Castro'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (KeyWord Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Pedro', sobrenome='Castro'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

"""

# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total



if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7]
    print(soma_impares(lista))

    tupla = (1, 2, 3, 4, 5, 6, 7)
    print(soma_impares(tupla))
