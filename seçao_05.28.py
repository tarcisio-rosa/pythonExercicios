"""
Leia três números inteiros positivos e efetue o calcúlo de umas das seguintes médias
"""

numero1 = int(input('Digite o primeiro número: '))

numero2 = int(input('Digite o segundo número: '))

numero3 = int(input('Digite o terceiro número: '))

opcao = int(input('Digite a média para o cálculo: 1 - Média Geométrica, 2 - Média Ponderada,'
                  '3 - Média Harmônica, 4 - Média Artimética: '))

if opcao == 1:
    media = (numero1 * numero2 * numero3) ** (1/3)
    print(f'{media: .2f}')
elif opcao == 2:
    media = ((numero1 + 2) * (numero2 + 3) * numero3) / 6
    print(f'{media: .2f}')
elif opcao == 3:
    media = 1 / ((1 / numero1) + (1 / numero2) + (1 / numero3))
    print(f'{media: .2f}')
elif opcao == 4:
    media = (numero1 + numero2 + numero3) / 3
    print(f'{media: .2f}')
else:
    print('Digite uma opção válida.')