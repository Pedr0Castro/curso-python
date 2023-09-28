"""
Bloco With

Passos para se trabalhar com arquivos
# 1 - abrimos
# 2 - manipulamos/trabalhamos
# 3 - fechamos o arquivo

o bloco with é utilizado para criar um contexto de trabalho, onde os recursos utilizados sção fechados
após o bloco with
"""

# o bloco with - Forma Pythonica de manipular arquivos

with open('texto.txt', encoding='utf-8') as arquivo:
    print(arquivo.readlines())
    print(arquivo.closed)


print(arquivo.closed)

