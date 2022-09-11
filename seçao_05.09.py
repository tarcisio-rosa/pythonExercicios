"""
Leia o salário de um trabalhador e o valor da prestação, se maior que 20% então imprima: Empréstimo não
concedido, caso contrário imprima: Empréstimo Concendido.
"""

salario = float(input("Digite o valor do seu salário: "))

prestacao = float(input("Digite o valor de sua prestação: "))

porcentagem = (prestacao * 100) / salario

if porcentagem > 20:
    print("Empréstimo não concedido.")

else:
    print("Empréstimo Concedido.")
