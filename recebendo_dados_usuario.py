"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- aspas simples;
- aspas duplas;
- asps simples triplas;
- aspas duplas triplas;
Exemplos:
- aspas simples -> 'Pedro Castro'
-  aspas duplas -> "Pedro Castro"
- aspas simples triplas -> '''Pedro Castro'''
"""
# aspas duplas triplas -> """Pedro Castro"""
# Entrada de dados
# print("qual seu nome? ")
# nome = input() # input -> Entrada
nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}' )

# print("Qual sua idade? ")
# idade = input()
idade = int(input('Qual a sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('O(A) %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# Print ('A {0} tem {1} anos'.format(nome, idade))
# Exemplo de print 'mais atual' 3.7
print(f'O(A) {nome} tem {idade} anos')

"""
# int(idade) -> cast
cast é a 'conversão' de um tipo de dado para outro.
"""

print(f'O(A) {nome} nasceu em {2023 - idade}')

