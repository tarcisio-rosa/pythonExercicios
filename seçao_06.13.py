"""
Faça um programa que leia um número inteiro positivo par N e imprima todos os números
naturais pares de 0 até N em ordem crescente
"""

num = int(input('Digite um número par: '))
x = 0

if num % 2 == 0:
    while x <= num:
        print(x)
        x += 2
else:
    print('O número digitado não é par, tente novamente!')
