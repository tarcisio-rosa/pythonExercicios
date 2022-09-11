"""
Aumento tabela funcionário
"""

salario = float(input('Digite o seu salário atual: '))

tempo_de_servico = int(input('Digite a quantidade de tempo de serviço em anos: '))

novo_salario = 0

if salario <= 500:
    if tempo_de_servico < 1:
        novo_salario = salario * 125 / 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 3 >= tempo_de_servico >= 1:
        novo_salario = salario * 125 / 100 + 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 6 >= tempo_de_servico >= 4:
        novo_salario = salario * 125 / 100 + 200
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 10 >= tempo_de_servico >= 7:
        novo_salario = salario * 125 / 100 + 300
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif tempo_de_servico > 10:
        novo_salario = salario * 125 / 100 + 500
        print(f'Seu novo salário é {novo_salario: .2f}')
elif 1000 >= salario > 500:
    if tempo_de_servico < 1:
        novo_salario = salario * 120 / 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 3 >= tempo_de_servico >= 1:
        novo_salario = salario * 120 / 100 + 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 6 >= tempo_de_servico >= 4:
        novo_salario = salario * 120 / 100 + 200
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 10 >= tempo_de_servico >= 7:
        novo_salario = salario * 120 / 100 + 300
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif tempo_de_servico > 10:
        novo_salario = salario * 120 / 100 + 500
        print(f'Seu novo salário é {novo_salario: .2f}')
elif 1500 >= salario > 1000:
    if tempo_de_servico < 1:
        novo_salario = salario * 115 / 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 3 >= tempo_de_servico >= 1:
        novo_salario = salario * 115 / 100 + 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 6 >= tempo_de_servico >= 4:
        novo_salario = salario * 115 / 100 + 200
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 10 >= tempo_de_servico >= 7:
        novo_salario = salario * 115 / 100 + 300
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif tempo_de_servico > 10:
        novo_salario = salario * 115 / 100 + 500
        print(f'Seu novo salário é {novo_salario: .2f}')
elif 2000 >= salario > 1500:
    if tempo_de_servico < 1:
        novo_salario = salario * 110 / 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 3 >= tempo_de_servico >= 1:
        novo_salario = salario * 110 / 100 + 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 6 >= tempo_de_servico >= 4:
        novo_salario = salario * 110 / 100 + 200
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 10 >= tempo_de_servico >= 7:
        novo_salario = salario * 110 / 100 + 300
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif tempo_de_servico > 10:
        novo_salario = salario * 110 / 100 + 500
        print(f'Seu novo salário é {novo_salario: .2f}')
else:
    if tempo_de_servico < 1:
        print('Você não tem direito a reajuste ou bônus este ano.')
    elif 3 >= tempo_de_servico >= 1:
        novo_salario = salario + 100
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 6 >= tempo_de_servico >= 4:
        novo_salario = salario + 200
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif 10 >= tempo_de_servico >= 7:
        novo_salario = salario + 300
        print(f'Seu novo salário é {novo_salario: .2f}')
    elif tempo_de_servico > 10:
        novo_salario = salario + 500
        print(f'Seu novo salário é {novo_salario: .2f}')
