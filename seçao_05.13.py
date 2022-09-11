"""
Média ponderada de um aluno
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / (1 + 1 + 2)

print(f'{media_ponderada: .2f}')

if media_ponderada > 60:
    print("Aprovado!")
else:
    print("Reprovado, tente novamente.")
