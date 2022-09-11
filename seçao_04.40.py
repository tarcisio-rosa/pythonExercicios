"""
Salário Encanador
"""

dias_trabalhado = int(input("Digite a quantidade de dias trabalhados: "))

imposto_renda = 0.92

salario = 30 * dias_trabalhado * imposto_renda

print(f"O seu salário baseado nos dias trabalhados será R${salario: .2f}")
