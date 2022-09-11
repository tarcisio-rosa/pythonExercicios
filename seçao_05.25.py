"""
Calculando as raízes de uma equação do 2 grau
"""

elemento_a = int(input('Digite o termo A da equação: '))

elemento_b = int(input('Digite o termo B da equação: '))

elemento_c = int(input('Digite o termo C da equação: '))

delta = elemento_b ** 2 - 4 * elemento_a * elemento_c

print(delta)

if elemento_a == 0:
    print('Não é equação de segundo grau.')
elif delta < 0:
    print('Não existe raiz.')
elif delta == 0:
    raiz1 = (-elemento_b + delta ** (1 / 2)) / (2 * elemento_a)
    print(f'Raíz única. {raiz1: .2f}.')
elif delta > 0:
    raiz1 = (-elemento_b + delta ** (1 / 2)) / (2 * elemento_a)
    raiz2 = (-elemento_b - delta ** (1 / 2)) / (2 * elemento_a)
    print(f'Duas Raízes, que são {raiz1: .2f}, {raiz2: .2f}.')
else:
    print('Nao é equação.')
