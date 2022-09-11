"""
Altura e sexo de uma pessoa e o programa mostra o peso ideal do indivíduo.
"""

altura = float(input("Digite a sua altura: "))

sexo = str(input("Qual é o seu sexo? (M) - Masculino ou (F) - Feminino "))

if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f"Seu peso ideal é {peso_ideal: .2f}.")

elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f"Seu peso ideal é {peso_ideal: .2f}.")

else:
    print("Carctere Inválido.")
