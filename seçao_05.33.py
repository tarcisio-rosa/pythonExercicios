"""
Ajuste de preços dos produtos
"""

preco_antigo = float(input("Digite o preço antigo: "))

preco_novo = 0

if preco_antigo >= 50:
    preco_novo = preco_antigo * 1.05
    preco_atual = preco_novo
    if preco_atual < 80:
        print("Barato")
    elif 80 < preco_atual <= 120:
        print("Normal")
    elif 120 < preco_atual <= 200:
        print("Caro")
    elif 80 < preco_atual <= 120:
        print("Muito caro")
elif 50 < preco_antigo <= 100:
    preco_novo = preco_antigo * 1.1
    preco_atual = preco_novo
    if preco_atual < 80:
        print("Barato")
    elif 80 < preco_atual <= 120:
        print("Normal")
    elif 120 < preco_atual <= 200:
        print("Caro")
    elif 80 < preco_atual <= 120:
        print("Muito caro")
elif preco_antigo > 100:
    preco_novo = preco_antigo * 1.15
    preco_atual = preco_novo
    if preco_atual < 80:
        print("Barato")
    elif 80 < preco_atual <= 120:
        print("Normal")
    elif 120 < preco_atual <= 200:
        print("Caro")
    elif 80 < preco_atual <= 120:
        print("Muito caro")
