"""
Nota final entre três notas de 0 a 10
"""

nota_trabalho = float(input("Digite a sua nota do Trabalho do laboratório: "))
nota_avaliacao = float(input("Digite a sua nota da Avaliação Semestral: "))
nota_exame = float(input("Digite a sua nota do Exame Final: "))
media = (nota_trabalho) + (nota_avaliacao) + (nota_exame) / 3

print(f"{media: .2f}")

if media > 4.9:
    print("Aprovado!")
elif media <= 2.9:
    print("Reprovado.")
else:
    print("Recuperação.")
