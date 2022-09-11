"""
Tarifas de estacionamento
"""

hora_entrada = int(input('Digite a hora de entrada: '))
minutos_entrada = int(input('Digite o minuto de entrada: '))

hora_saida = int(input('Digite a hora de saída: '))
minutos_saida = int(input('Digite o minuto da saida: '))

tempo_minutos_entrada = hora_entrada * 60 + minutos_entrada
tempo_minutos_saida = hora_saida * 60 + minutos_saida

tempo_total = 0

valor_a_pagar = 0

if tempo_minutos_entrada > tempo_minutos_saida:
    tempo_total = (1440 - tempo_minutos_entrada) + tempo_minutos_saida
    if tempo_total <= 60:
        valor_a_pagar = 1
        print(f'Sua tarifa é R$ {valor_a_pagar}.')
    elif 60 < tempo_total <= 120:
        valor_a_pagar = 2
        print(f'Sua tarifa é R$ {valor_a_pagar}.')
    elif 120 < tempo_total <= 180:
        valor_a_pagar = 2 + 1.4
        print(f'Sua tarifa é R$ {valor_a_pagar}')
    elif 180 < tempo_total <= 240:
        valor_a_pagar = 2 + 2 * 1.4
        print(f'Sua tarifa é R$ {valor_a_pagar}')
    elif tempo_total > 240:
        valor_a_pagar = 2 + 2.8 + ((tempo_total - 300) // 60) * 2
        print(f'Sua tarifa é R$ {valor_a_pagar}')
else:
    tempo_total = tempo_minutos_saida - tempo_minutos_entrada
    if tempo_total <= 60:
        valor_a_pagar = 1
        print(f'Sua tarifa é R$ {valor_a_pagar}.')
    elif 60 < tempo_total <= 120:
        valor_a_pagar = 2
        print(f'Sua tarifa é R$ {valor_a_pagar}.')
    elif 120 < tempo_total <= 180:
        valor_a_pagar = 2 + 1.4
        print(f'Sua tarifa é R$ {valor_a_pagar}')
    elif 180 < tempo_total <= 240:
        valor_a_pagar = 2 + 2 * 1.4
        print(f'Sua tarifa é R$ {valor_a_pagar}')
    elif tempo_total > 240:
        valor_a_pagar = 2 + 2.8 + ((tempo_total - 300) // 60) * 2
        print(f'Sua tarifa é R$ {valor_a_pagar}')
