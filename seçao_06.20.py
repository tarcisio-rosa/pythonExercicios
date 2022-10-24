"""
Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de
dados lidos e números de valores pares. O processo termina quando for digitado o número 1000.
"""

# Contandor geral dos números lidos, que é a soma dos contadores dos números pares e ímpares.
cont_geral = 0
cont_par = 0
cont_impar = 0

# Criação da lista que restringirá os dados lidos até o número 1000.
lista = list(range(1000))

# Loop que fará a leitura dos dados inseridos
while True:
    num = int(input('Digite um número inteiro: '))
    if num in lista:
        if num % 2 == 0:
            cont_par += 1
        else:
            cont_impar += 1
    else:
        break
cont_geral = cont_par + cont_impar
print(f"Foram digitados {cont_geral + 1} números e {cont_par + 1} são pares.")
