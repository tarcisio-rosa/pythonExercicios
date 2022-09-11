"""
Programa de Ajuda para Vendedores
"""

valor_venda = float(input("Digite o valor da venda: "))

desconto = valor_venda * 0.9

parcelamento = valor_venda / 3

comissao_vendedor1 = desconto * 0.05

comissao_vendedor2 = valor_venda * 0.05

print(f"{desconto: .2f}")

print(f"{parcelamento: .2f}")

print(f"{comissao_vendedor1: .2f}")

print(f"{comissao_vendedor2: .2f}")
