"""
Hipotenusa de um triângulo.
"""
cateto_a = int(input("Digite o valor do primeiro cateto: "))

cateto_b = int(input("Digite o valor do segundo cateto: "))

hipotenusa = (cateto_a ** 2) + (cateto_b ** 2)

import math
print(f"O valor da hipotenusa é {math.sqrt(hipotenusa)}")
