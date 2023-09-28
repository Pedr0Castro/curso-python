"""
Escopo de Variáveis

Dois casos de Escopo:

1- Variáveis Globais;
  - são reconhecidas, ou seja, seu escopo compreende , todo o programa

2- Variáveis Locais;
  - São reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está limitado
  ao bloco onde foi declarada.

Para declarar variável em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declararmos uma variável nós não colocamos
o tipo de dado dela, este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em JAVA;
int numero =42;
"""

numero = 42  # Exemplo de variável Global
print(numero)
print(type(numero))

numero = 'Gekk'
print(numero)
print(type(numero))


nao_existo = 'Oi'
print(nao_existo)

numero = 42
novo = 0

if numero > 10:
    novo = numero + 10  # A variável 'novo' está declarada  localmente dentro do bloco if. Portanto é global.
    print(novo)

print(novo)