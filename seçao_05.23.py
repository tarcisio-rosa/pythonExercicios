"""
Determine se um ano lido é bissexto
"""

ano = int(input('Digite o ano para saber se ele é bissexto: '))

resto1 = int(ano % 400)

resto2 = int(ano % 4)

resto3 = int(ano % 100)

if resto1 == 0:
    print('Ano bissexto.')
elif resto2 == 0 and resto3 > 0:
    print('Ano bissexto.')
else:
    print('Esse ano não é bissexto.')
