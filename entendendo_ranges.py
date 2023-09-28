"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Forma gerais:

range(valor_de_parada)

OBS: Valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)
# Exemplo Forma 1
for num in range(11):
    print(num)

# Exemplo forma 2

range(valor_de_inicio, valor_de_parada)

OBS: Valor_de_parada não inclusive (inicio especificado pelo usuário, e passo de 1 em 1)

for num in range(4, 11):
    print(num)

# Exemplo forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: Valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuário)

for num in range(5, 55, 5):
    print(num)

forma 4(inversa)

range(valor_inicio, valor_de_parada, passo)

OBS: Valor_de_parada não inclusive (valor_inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo forma 4
for num in range(10, -1, -1):
    print(num)
"""
