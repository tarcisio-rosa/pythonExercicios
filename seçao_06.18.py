"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes
o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

maior_numero: 0

while True:
    num = input('Digite um número: ')
    if num >= maior_numero:
        maior_numero = num
