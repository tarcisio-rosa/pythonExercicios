"""
Número digitado positivo calcular ao quadrado e a raiz quadrada
"""

import math

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O número digitado elevado ao quadrado é {numero ** 2}.")
    print(f"O a raiz quadrada do número digitado é {math.sqrt(numero)}.")

else:
    print("Esse número não é válido.")