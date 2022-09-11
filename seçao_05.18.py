"""
4 operações básicas
"""
operacao_matematica = int(input("Escolha uma das opções 1 - Soma, 2 - Subtração, 3 - Multiplicação, "
                                "4 - Divisão: "))
resultado = 0

numero1 = float(input("Digite o primeiro número: "))

numero2 = float(input("Digite o segundo número: "))

if operacao_matematica == 1:
    resultado = numero1 + numero2

elif operacao_matematica == 2:
    resultado = numero1 - numero2

elif operacao_matematica == 3:
    resultado = numero1 * numero2

elif operacao_matematica == 4:
    resultado = numero1 / numero2

else:
    print('Digite uma operação válida.')

print(f'O resultado da operção matemática é {resultado: .2f}.')
