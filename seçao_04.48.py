"""
Segundos para horas, minutos e segundos.
"""

segundos = int(input("Digite a quantidade de tempo em segundos: "))

horas = int(segundos / 3600)

minutos = int((segundos % 3600) / 60)

segundos = (segundos % 3600) % 60

print(f"A quantidade de tempo em horas, minutos e segundos é {horas}h {minutos}m {segundos}s.")
