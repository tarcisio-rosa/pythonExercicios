"""
Dois números, qual é o maior, se forem iguais imprima 'Números Iguais'
"""

numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(f"O maior número é o {numero1}.")
elif numero1 == numero2:
    print(f"Números iguais.")
else:
    print(f"O maior número é o {numero2}.")
