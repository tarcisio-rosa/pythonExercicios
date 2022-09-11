"""
Escrever um programa que leia o código do produto escolhido e a quantidade.
"""

codigo = int(input("Escolha um dos códigos abaixo:"
                   "\nCódigo - Especificação - Preço"
                   "\n100 - Cachorro Quente - R$ 1.20"
                   "\n101 - Bauru Simples - R$ 1.30"
                   "\n102 - Bauru com Ovo - R$ 1.50"
                   "\n103 - Hamburguer - R$ 1.20"
                   "\n104 - Cheeseburguer - R$ 1.70"
                   "\n105 - Suco - R$ 2.20"
                   "\n106 - Refrigerante - R$ 1.00"
                   "\nDigite aqui seu código: "))
quantidade = int(input("Agora digite a quantidade: "))

valor = 0

if codigo == 100:
    valor = 1.2 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 101:
    valor = 1.3 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 102:
    valor = 1.5 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 103:
    valor = 1.2 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 104:
    valor = 1.7 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 105:
    valor = 2.2 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
elif codigo == 101:
    valor = 1 * quantidade
    print(f"Valor total R$ {valor: .2f}.")
else:
    print("Código errado, por favor digite um código correto.")
