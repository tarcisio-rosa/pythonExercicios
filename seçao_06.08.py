"""
Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido
"""

x = 1
lista = []
while x <= 10:
    valores = int(input('Digite o valor: '))
    lista.append(valores)
    x += 1
print(f'O valor mínimo é {min(lista)}')
print(f'O valor máximo é {max(lista)}')
