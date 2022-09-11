"""
Conceito notas
"""

nota = float(input("Digite a sua nota: "))

faltas = int(input("Digite a quantidade de faltas que você possui: "))

if 9 <= nota <= 10:
    if faltas > 20:
        conceito = "B"
        print(f"O seu conceito é {conceito}")
    else:
        conceito = "A"
        print(f"O seu conceito é {conceito}")
elif 7.5 <= nota < 9:
    if faltas > 20:
        conceito = "C"
        print(f"O seu conceito é {conceito}")
    else:
        conceito = "B"
        print(f"O seu conceito é {conceito}")
elif 5 <= nota < 7.5:
    if faltas > 20:
        conceito = "D"
        print(f"O seu conceito é {conceito}")
    else:
        conceito = "C"
        print(f"O seu conceito é {conceito}")
elif 4 <= nota < 5:
    if faltas > 20:
        conceito = "E"
        print(f"O seu conceito é {conceito}")
    else:
        conceito = "D"
        print(f"O seu conceito é {conceito}")
elif 0 <= nota < 4:
    if faltas > 20:
        conceito = "E"
        print(f"O seu conceito é {conceito}")
    else:
        conceito = "E"
        print(f"O seu conceito é {conceito}")
else:
    print("Digite uma nota válida!")