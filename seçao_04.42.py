"""
Salário Base Funcionário
"""

salario_base = float(input("Digite o seu slário base: "))

gratificacao = salario_base * 5/100

imposto = salario_base * 7/100

salario_final = salario_base + gratificacao - imposto

print(f"O seu salário esse mês será de R${salario_final: .2f}.")
