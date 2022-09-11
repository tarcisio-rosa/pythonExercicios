"""
Volume de um cilindro
"""
altura_cilindro = int(input("Digite o valor da altura do cilindro: "))

raio_cilindro = float(input("Digite i valor do raio do cilindro: "))

volume_cilindro = 3.141592 * (raio_cilindro ** 2) * altura_cilindro

print(f"O volume do cilindro é {volume_cilindro: .2f}m³.")
