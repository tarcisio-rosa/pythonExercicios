"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem crescente
"""

# Recebendo o número através de uma variável
num = int(input('Digite um número inteiro ímpar: '))

# Variável acumuladora
x = 1

# Estrutura condicional para validar se a variável é um número ímpar
if num % 2 != 0:
    "Loop para gerar os números de 1 até a variável num"
    while x <= num:
        print(x)
        x += 2
else:
    print('Este número não é ímpar, reniciei o programa!')
