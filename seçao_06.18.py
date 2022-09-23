"""
Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes
o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.
"""

maior = 0
continuar = None
qtd = 0

while continuar != 'Não':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num == maior:
            qtd += 1
    continuar = input('Deseja continuar? ')
print(f'O maior número digitado foi {maior}, ele foi digitado {qtd} vezes.')
