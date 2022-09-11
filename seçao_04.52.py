"""
Divisão de prémio proporcional
"""

premio = float(input("Digite o valor do prémio: "))

jogador1 = float(input("Digite o valor apostado pelo primeiro jogador: "))

jogador2 = float(input("Digite o valor apostado pelo segundo jogador: "))

jogador3 = float(input("Digite o valor apostado pelo terceiro jogador: "))

soma_valores_apostados = jogador1 + jogador2 + jogador3

porcentagem_1 = (jogador1 / soma_valores_apostados) * premio

porcentagem_2 = (jogador2 / soma_valores_apostados) * premio

porcentagem_3 = premio - (porcentagem_1 + porcentagem_2)

print(f"O prémio do jogador 1 é {porcentagem_1: .2f}.")
print(f"O prémio do jogador 2 é {porcentagem_2: .2f}.")
print(f"O prémio do jogador 2 é {porcentagem_3: .2f}.")
