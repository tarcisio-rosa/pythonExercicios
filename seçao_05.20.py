"""
Verificar se triângulo é escaleno, equilátero ou isósceles
"""

lado1 = int(input('Digite o primeiro valor: '))

lado2 = int(input('Digite o segundo valor: '))

lado3 = int(input('Digite o terceiro valor: '))

if (lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1:
    print('Os três lados formam um triângulo!')
    if lado1 == lado2 and lado1 == lado3:
        print('Equilátero')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Isósceles')
    else:
        print('Escaleno')
else:
    print('Os três lados não formam um triângulo.')
