"""
Custo Carro para o consumidor
"""

custo_fabrica = float(input('Digite o valor de fábrica: '))
comissao = 0
impostos = 0
valor_final = 0

if custo_fabrica <= 12000:
    comissao = custo_fabrica * 5 / 100
    impostos = None
    valor_final = custo_fabrica + comissao
    print(f'O seu carro custará R${valor_final: .2f}')
elif 12000 < custo_fabrica <= 25000:
    comissao = custo_fabrica * 10 / 100
    impostos = custo_fabrica * 15 / 100
    valor_final = custo_fabrica + comissao + impostos
    print(f'O seu carro custará R${valor_final: .2f}')
else:
    comissao = custo_fabrica * 15 / 100
    impostos = custo_fabrica * 20 / 100
    valor_final = custo_fabrica + comissao + impostos
    print(f'O seu carro custará R${valor_final: .2f}')
