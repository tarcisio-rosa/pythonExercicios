"""
Números inteiros de 1 a 99 aleatoriamente com função de soma entre dois números.
"""

import random

a = random.randint(1, 99)

b = random.randrange(1, 99)

resposta = int(input(f"Qual é a soma de {a} + {b}, digite sua resposta: "))

soma = a + b

if resposta == soma:
    print("Sua resposta está correta.")
else:
    print('Resposta errada, treine mais.')

