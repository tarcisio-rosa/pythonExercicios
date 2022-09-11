"""
Dois números qual é o maior entre eles e a diferença entre tais.
"""

numero1 = int(input("Digite o primeiro número: "))

numero2 = int(input("Digite o segundo número: "))

diferenca = 0

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(f"O {numero1} é o maior número e a diferença entre eles é {diferenca}.")
else:
    diferenca = numero2 - numero1
    print(f"O {numero2} é o maior número e a diferença entre eles é {diferenca}.")
