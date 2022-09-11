"""
Faça um programa que leia 10 inteiros e imprima sua média
"""

soma = 0
x = 1

while x <= 10:
    valores = int(input('Digite o valor: '))
    soma += valores
    x += 1
print(f'A média dos valores é {soma / x: .2f}')
