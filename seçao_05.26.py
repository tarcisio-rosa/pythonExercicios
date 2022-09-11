"""
Quantidade de litros de gasolina consumido por um carro
"""

distancia = int(input('Digite a distância em Km: '))

litros = int(input('Digite a quantidade em litros da gasolina consumida: '))

km_l = distancia / litros

if km_l < 8:
    print('Venda o carro!')
elif km_l > 12:
    print('Super econômico!')
else:
    print('Econômico!')
