"""
Algoritmo para cálculo de IMC
"""

print('Veja a sua CLASSIFICAÇÃO DO IMC')
altura = float(input('Digite a sua altura (em m): '))
peso = float(input('Digite o seu peso (em Kg): '))

# Cálculo IMC

calculo_imc = peso / altura ** 2
classificacao = ['Abaixo do Peso', 'Saudável', 'Peso em excesso', 'Obesidade Grau I', 'Obesidade Grau II(severa)',
                 'Obesidade Grau II(mórbida)']

if calculo_imc <= 18.5:
    print(classificacao[0])
elif 18.5 < calculo_imc < 25:
    print(classificacao[1])
elif 25 <= calculo_imc < 30:
    print(classificacao[2])
elif 30 <= calculo_imc < 35:
    print(classificacao[3])
elif 35 <= calculo_imc < 40:
    print(classificacao[4])
else:
    print(classificacao[5])
