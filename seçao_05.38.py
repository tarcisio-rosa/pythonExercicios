"""
Data Nascimento Válida
"""

dia = int(input("Digite o dia em número: "))
mes = int(input("Digite o mês em número: "))
ano = int(input("Digite o ano em número: "))


if ano % 4 == 0:
    if mes == 1 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 3 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 5 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 7 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 8 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 10 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 12 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 2 and 29 >= dia > 0:
        print('Data Válida')
    elif mes == 4 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 6 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 9 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 11 and 30 >= dia > 0:
        print('Data Válida')
    else:
        print('Data Inválida')
else:
    if mes == 1 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 3 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 5 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 7 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 8 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 10 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 12 and 31 >= dia > 0:
        print('Data Válida')
    elif mes == 4 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 6 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 9 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 11 and 30 >= dia > 0:
        print('Data Válida')
    elif mes == 2 and 28 >= dia > 0:
        print('Data Válida')
    else:
        print('Data Inválida')