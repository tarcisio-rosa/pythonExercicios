"""
Dividir prémio para três pessoas com porcentagens diferentes
"""

premio = 780_000

primeiro_ganhador = premio * 0.46

segundo_ganhador = premio * 0.32

terceiro_ganhador = premio - primeiro_ganhador - segundo_ganhador

print(primeiro_ganhador)
print(segundo_ganhador)
print(terceiro_ganhador)
