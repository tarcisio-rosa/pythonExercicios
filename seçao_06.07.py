"""
Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média
"""

soma_positivos = 0
contador_positivos = 0
x = 1

while x <= 10:
    valores = int(input('Digite o valor: '))
    if valores > 0:
        soma_positivos += valores
        contador_positivos += 1
    x += 1
print(f'A média dos números positivos é {soma_positivos / contador_positivos: .2f}')
