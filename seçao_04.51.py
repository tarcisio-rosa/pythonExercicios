"""
Coordenadas x e y no R².
"""

ponto_x = int(input("Digite a coordenada do ponto x: "))

ponto_y = int(input("Digite a coordenada do ponto y: "))

distancia = float(ponto_x ** 2 + ponto_y ** 2) ** (1 / 2)

print(f"{distancia: .2f}")
