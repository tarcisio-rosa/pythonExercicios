"""
Faça um programa que leia um número inteiro positivo N e calcule a soma dos N primeiros
números naurais
"""

# Recebendo a variável como parâmetro de entrada
num = int(input('Digite um número inteiro positivo: '))

# Variável contadora
x = 1

# Variável acumuladora
soma = 0
# Validando se a variável 'n' é um tipo inteiro positivo
if num > -1:
    while x <= num:
        soma += x
        x += 1
    print(soma)
else:
    print('Este número não é um inteiro positivo, reniciei o programa!')
