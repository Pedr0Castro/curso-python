"""
Documentando funções com Docstrings

OBS: Podemos ter acesso a documentação de uma função em Python utilizando a propriedade especial
__doc__

Podemos ainda fazer acesso a documentação com a função help()
"""

# Exemplos

def diz_oi():
    """Uma função simples que retorna a string 'oi!'"""
    return 'Oi! '

print(diz_oi())

print(help(diz_oi()))

print(diz_oi.__doc__)

def exponencial(numero, potencia=2):
    """
    Função que retorna por padrao o qaudrado de 'numero' ou 'numero' à 'potencia' informada
    :param numero: Numero que desejamos gerar o exponencial.
    :param potencia: Potencia que queremos gerar o exponencial. Por padrão é 2
    :return: Retorna o exponencial de número por 'potencia'.
    """
    return numero ** potencia

