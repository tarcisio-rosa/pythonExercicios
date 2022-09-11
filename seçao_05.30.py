"""
Três números em ordem crescente
"""

a = int(input("Digite o primeiro número: "))

b = int(input("Digite o segundo número: "))

c = int(input("Digite o terceiro número: "))

if a < b < c:
    print(f"A ordem crescente dos números digitados é {a}, {b}, {c}.")
elif a < c < b:
    print(f"A ordem crescente dos números digitados é {a}, {c}, {b}.")
elif b < a < c:
    print(f"A ordem crescente dos números digitados é {b}, {a}, {c}.")
elif b < c < a:
    print(f"A ordem crescente dos números digitados é {b}, {c}, {a}.")
elif c < a < b:
    print(f"A ordem crescente dos números digitados é {c}, {a}, {b}.")
elif c < b < a:
    print(f"A ordem crescente dos números digitados é {c}, {b}, {a}.")
else:
    print("Valores digitados iguais em uma das opções, por favor digite valores diferentes.")
