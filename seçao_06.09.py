"""
Faça um programa que leia um número natural N e depois imprima os N primeiros números naturais ímpares
"""

numero = int(input('Digite o número: '))

for numero in range(1, numero, 2):
    print(numero)
