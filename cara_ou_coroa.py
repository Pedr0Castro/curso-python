




from random import random


def joga_moeda():
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())






