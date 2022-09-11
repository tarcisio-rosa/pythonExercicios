"""
Leia um número, se for positivo imprima raiz quadrada, se for negativo imprima ao quadrado.
"""
import math

numero = float(input("Digite um número: "))

if numero >= 0:
    print(f"O valor da raiz quadrada do número digitado é {math.sqrt(numero)}.")
else:
    print(f"O valor do número digitado ao quadrado é {numero ** 2}.")
