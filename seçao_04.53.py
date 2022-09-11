"""
Tamanho dos lados de um terreno e custo para cercar o mesmo.
"""

lado_a = float(input("Digite o valor da largura: "))

lado_b = float(input("Digite o valor do comprimento: "))

preco_cerca = float(input("Digite o preço R$ do metro da cerca: "))

preco_a_pagar = ((lado_a * 2 + lado_b * 2) * preco_cerca)

print(f"Você pagará R${preco_a_pagar: .2f}, para cercar todo o seu terreno.")
