"""
Cálculo de Horas trabalhadas no mês
"""

horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mês: "))

valor_horas = float(input("Digite o valor em R$ da hora trabalhada: "))

bonus = 110/100

salario = horas_trabalhadas * valor_horas * bonus

print(f"Seu salário será R${salario: .2f}, baseado na quantidade de horas trabalhadas.")
