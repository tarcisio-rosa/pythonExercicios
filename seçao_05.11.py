"""
Leia um número inteiro maior que zero e devolva a soma de todos os seus algarismos.
"""
numeros = int(input("Digite um número: "))

soma = 0

if numeros < 0:
    print("Número Inválido.")

else:
    while (numeros > 0):
        resto = numeros % 10
        numeros = (numeros - resto) // 10
        soma = soma + resto
    print(f"A soma dos números é {soma}")
