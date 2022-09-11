"""
Leia duas notas de um aluno válidas de 0 a 10 e imprima a média
"""

nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = float(nota1 + nota2) / 2

if nota1 and nota2 < 0:
    print("Nota inválida, digite uma nota de 0 a 10.")
elif nota1 and nota2 > 10:
    print("Nota inválida, digite uma nota de 0 a 10.")
else:
    print(f"A sua média é {media: .2f}.")
