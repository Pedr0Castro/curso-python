"""
Estruturas lógicas: and, or, not, is

operadores unários:
        -not;
operadores binários:
     -and, or, is


Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, ser for True vira False, ser for False vira True.
Para o 'is', o valor é comparado com um segundo valor.
"""
ativo = False
logado = False

# Se não tiver ativo
if ativo:
    print('Bem vindo usuário')
else:
   print('Você precisa ativar sua conta. Por favor, cheque seu e-mail')

# Ativo é Falso?
print(ativo is False)





