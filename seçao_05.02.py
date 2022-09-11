"""
Número positivo calcular raiz quadrada, negativo número inválido
"""
import math

numero = float(input("Digite um número: "))

if numero > 0:
    print(f"O valor da raiz quadrada do número digitado é {math.sqrt(numero)}.")
else:
    print("Esse número não é válido.")
