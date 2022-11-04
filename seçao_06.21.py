"""
Faça um programa que receba dois números. Calcule e mostre:

    - a soma dos números pares desse intervalo de números, incluindo os números digitados;

    - a multiplicação dos números ímpares desse intervalo, incluindo os digitados;

"""

# Recebendo os números digitados pelo usuário
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

# Variáveis que receberão os números pares e ímpares
n_par = 0
n_impar = 1

# Variáveis com os totais das somas e multiplicações dos números
total_par = 0
total_impar = 1

# Verificando qual número é maior
if n1 > n2:
    # iterando no intervalo dos números
    for i in range(n2, n1):
        # Verificando se o número é par
        if i % 2 == 0:
            n_par += i
            # Verificando se o primeiro número digitado é par
            if n1 % 2 == 0:
                total_par = n_par + n1
            else:
                total_par = n_par
        else:
            n_impar *= i
            if n1 % 2 == 0:
                total_impar = n_impar
            else:
                total_impar = n_impar * n1
    print(f'A soma dos números pares são {total_par}\n'
          f'A multiplicação dos números ímpares são {total_impar}')

else:
    for i in range(n1, n2):
        if i % 2 == 0:
            n_par += i
            if n2 % 2 == 0:
                total_par = n_par + n2
            else:
                total_par = n_par
        else:
            n_impar *= i
            if n2 % 2 == 0:
                total_impar = n_impar
            else:
                total_impar = n_impar * n2
    print(f'A soma dos números pares são {total_par}\n'
          f'A multiplicação dos números ímpares são {total_impar}')
