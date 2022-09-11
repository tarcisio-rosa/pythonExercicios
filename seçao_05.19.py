"""
Número divisível
"""

numero = int(input("Digite um número: "))

divisao1 = numero % 3

divisao2 = numero % 5

if divisao1 == 0:
    print('Número é divisível por 3')

elif divisao2 == 0:
    print('Número é divisível por 5')
