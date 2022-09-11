"""
Programa que recebe altura e peso de uma pessoa e mostra a classificação
"""

altura = float(input("Digite a sua altura: "))

peso = float(input("Digite o seu peso: "))

if altura < 1.2 and peso <= 60:
    print("A")
elif altura < 1.2 and 60 < peso <= 90:
    print("D")
elif altura < 1.2 and peso > 90:
    print("G")
elif 1.2 < altura <= 1.7 and peso <= 60:
    print("B")
elif 1.2 < altura <= 1.7 and 60 < peso <= 90:
    print("E")
elif 1.2 < altura <= 1.7 and peso > 90:
    print("H")
elif altura > 1.7 and peso <= 60:
    print("C")
elif altura > 1.7 and 60 < peso <= 90:
    print("F")
elif altura > 1.7 and peso > 90:
    print("I")
