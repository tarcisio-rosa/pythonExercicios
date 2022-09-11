"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números
naturais pares de 0 até N em ordem decrescente
"""

num = int(input('Digite um número par: '))
x = 0

if num % 2 == 0:
    while num >= x:
        print(num)
        num -= 2
else:
    print('Este número não é par, tente novamente!')
