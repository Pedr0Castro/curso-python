"""
**Kwargs

Poderiamos chamar este parametro de **xix, mas chamamos de **Kwargs

este é so mais um parametro, mas diferente do *args que coloca os valores extras
em uma tupla, o **Kwargs exige que utilizemos parametros nomeados, e transforma esses
parametros extras em um dicionário.

# Exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')


# OBS: os parametros *args e **Kwargs não são obrigatorios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo

def cumprimento_especial(**Kwargs):
    if 'Geek' in Kwargs and Kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pyhtonico Geek!'
    elif 'geek' in Kwargs:
        return f"{Kwargs['geek']} Geek!"
    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter:

- Parametros obrigatórios;
- *args;
- Parametros default(não obrigatórios);
- **Kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **Kwargs):
    print(f'{nome}, tem {idade}, anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(Kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
def mostra_info(a, b, *args, instrutor='Geek', **Kwargs):
    return [a, b, args, instrutor, Kwargs]

a = 1
b = 2
args = (3,)
instutor = 'Geek'
Kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}



print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **Kwargs

def mostra_nomes(**Kwargs):
    return f"{Kwargs['nome']} {Kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nomes(**nomes))
"""

# Desempacotar com **Kwargs

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
soma_multiplos_numeros(*lista)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS: os nomes da chave em um dicionário deve ser os mesmos dos parâmetros da função
