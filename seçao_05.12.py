"""
Ler um número inteiro, se for negativo escreva número inválido, positivo calcular o logartimo.
"""
import math

numero = int(input("Digite um número: "))

if numero < 0:
    print("Número inválido.")
else:
    print(math.log(numero))
