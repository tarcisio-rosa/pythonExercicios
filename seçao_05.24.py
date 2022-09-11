"""
Valor e estado
"""

valor = float(input('Digite o valor do produto em R$: '))

estado = input('Digite o estado de destino: MG - Minas Gerais, SP - São Paulo, RJ - Rio de Janeiro,'
               'MS - Mato Grosso do Sul: ')
imposto = 0

if estado == 'MG':
    imposto = valor * 1.07
    print(f'O preço do produto com imposto é R$ {imposto: .2f}.')
elif estado == 'SP':
    imposto = valor * 1.12
    print(f'O preço do produto com imposto é R$ {imposto: .2f}.')
elif estado == 'RJ':
    imposto = valor * 1.15
    print(f'O preço do produto com imposto é R$ {imposto: .2f}.')
elif estado == 'MS':
    imposto = valor * 1.08
    print(f'O preço do produto com imposto é R$ {imposto: .2f}.')
else:
    print('Estado inválido.')
