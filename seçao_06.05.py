"""
Faça um programa que o usuário digite 10 valores e retorne a soma dos valores
"""

soma = 0
x = 1
while x <= 10:
    valores = float(input('Digite o valor: '))
    soma = soma + valores
    x = x + 1
print(f'A soma dos valores é {soma: .2f}')
