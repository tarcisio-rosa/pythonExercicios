"""
Altura degrau
"""

altura_degrau = int(input("Digite a altura do Degrau em centímetros: "))

altura_desejada = float(input("Digite a altura que deseja subir em metros: "))

conversao = altura_degrau / 100

quantidade_degraus = int(altura_desejada / conversao)

print(f"A quantidade de degraus necessários na escada é {quantidade_degraus} degraus.")
