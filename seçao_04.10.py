""" Velocidade em Km/h para m/s
"""

velocidade_em_km = int(input("Digite a velocidade em km/h: "))

velocidade_em_metro_segundo = velocidade_em_km / 3.6

print(f"A velocidade digitada é {velocidade_em_metro_segundo: .2f}m/s")
