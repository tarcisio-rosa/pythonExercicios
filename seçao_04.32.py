"""
Soma do triplo do sucessor de um número com o dobro do se antecessor
"""

numero = int(input("Digite um número: "))

sucessor = (numero + 1) * 3
antecessor = (numero - 1) * 2

soma = sucessor + antecessor

print(f"O resultado da soma do triplo do sucessor do número digitado com o dobro do seu antecessor é {soma}.")
