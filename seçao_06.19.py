"""
Escreva um algoritmo que leia um número entre 100 e 999 e imprima na saída cada um dos algorismos que
compõem o número.
"""

# Recebendo o número a ser lido pelo usuário
num = int(input('Digite um número entre 100 e 999: '))

# Restringindo a lista que servirá como referência para a condição do problema
lista = list(range(100, 1000, 1))

# Condição sendo testada e retornando o resultado
if num in lista:
    # Condição sendo verdadeira: Converter o número em string, pois um número inteiro não é iterável
    # e depois converter em uma string
    new_list = list(str(num))
    # Saída da lista com suas posições
    print(new_list[0])
    print(new_list[1])
    print(new_list[2])
else:
    # Caso a condição não seja atendida.
    print("Número não se encontra no intervalo de 100 a 999, tente novamente.")
