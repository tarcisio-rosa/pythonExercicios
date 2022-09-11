"""
Categoria do nadador de acordo com a idade
"""

idade = int(input('Digite a sua idade: '))

if 4 < idade < 8:
    print('Categoria Infantil A.')
elif 7 < idade < 11:
    print('Categoria Infantil B')
elif 10 < idade < 14:
    print('Categoria Juvenil A')
elif 13 < idade < 18:
    print('Categoria Juvenil B')
elif idade > 17:
    print('Categoria Sênior')
