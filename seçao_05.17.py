"""
Área de um trapézio
"""

base1 = float(input("Digite o valor da base maior: "))

base2 = float(input("Digite o valor da base menor: "))

altura = float(input("Digite o valor da altura: "))

if base1 and base2 > 0:
    area = ((base1 + base2) * altura) / 2
    print(f"A área do trapézio é {area: .2f}.")
else:
    print("Digite um valor maior de zero.")
