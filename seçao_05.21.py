"""
Menu de opções e execute a operação escolhida
"""

numero1 = int(input('Digite o primeiro valor: '))

numero2 = int(input('Digite o segundo valor: '))

menu_de_opcoes = int(input('Digite uma opção: 1 - Soma de dois números, 2 - Diferença entre dois números;'
                           ' 3 - Produto entre dois números; 4 - Divisão entre dois números: '))

resultado = 0

if menu_de_opcoes == 1:
    resultado = numero1 + numero2
    print(f'O valor da soma é {resultado}')
elif menu_de_opcoes == 2:
    if numero1 > numero2:
        resultado = numero1 - numero2
        print(f'O valor da subtração é {resultado}.')
    else:
        resultado = numero2 - numero1
        print(f'O valor da subtração é {resultado}.')
elif menu_de_opcoes == 3:
    resultado = numero1 * numero2
    print(f'O valor do produto é {resultado}.')
elif menu_de_opcoes == 4:
    if numero1 > 0:
        resultado = numero2 / numero1
        print(f'O valor da divisão é {resultado: .2f}.')
    elif numero2 > 0:
        resultado = numero1 / numero2
        print(f'O valor da divisão é {resultado: .2f}.')
else:
    print('Opção inválida, digite uma opção válida!')
