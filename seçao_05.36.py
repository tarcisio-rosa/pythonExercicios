"""
Valor fixo + Comissão
"""

venda = float(input("Digite a sua venda mensal: "))

comissao = 0

if venda >= 100000:
    comissao = 700 + (venda * 16 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
elif 100000 > venda >= 80000:
    comissao = 650 + (venda * 14 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
elif 80000 > venda >= 60000:
    comissao = 600 + (venda * 14 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
elif 60000 > venda >= 40000:
    comissao = 550 + (venda * 14 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
elif 40000 > venda >= 20000:
    comissao = 500 + (venda * 14 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
else:
    comissao = 400 + (venda * 14 / 100)
    print(f'Sua comissão será de R${comissao: .2f}')
