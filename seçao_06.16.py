"""
Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os
números ímpares de 1 até N em ordem decrescente
"""

# Recebendo o número através de uma variável, nesse caso, que será também a variável acumuladora
num = int(input('Digite um número inteiro ímpar: '))

# Estrutura condicional para validar se a variável é um número ímpar
if num % 2 != 0:
    "Loop para gerar os números da variável num até 1"
    while num >= 1:
        print(num)
        num -= 2
else:
    print('Este número não é ímpar, reniciei o programa!')
