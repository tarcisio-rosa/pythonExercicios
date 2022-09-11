"""
Segundos adicionados em tempo determinado.
"""
hora_inicial = int(input("Digite a hora inicial: "))

minuto_inicial = int(input("Digite o minuto inicial: "))

segundos_inicial = int(input("Digite o segundo inicial: "))

segundos = int(input("Digite a quantidade de tempo em segundos do experimento: "))

horas = int(segundos / 3600) + hora_inicial

minutos = int((segundos % 3600) / 60) + minuto_inicial

segundos = ((segundos % 3600) % 60) + segundos_inicial

print(f"O experimento terminará às {horas}h {minutos}m {segundos}s.")
