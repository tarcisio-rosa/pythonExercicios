"""
Leia o tempo de serviço de um trabalhador e veja se ele já pode se aposentar
"""

idade = int(input('Digite a sua idade: '))

tempo_servico = int(input('Digite seu tempo de contribuição: '))

if idade > 64:
    print('Você já pode se aposentar.')
elif tempo_servico >= 30:
    print('Você já pode se aposentar.')
elif idade > 59 and tempo_servico > 24:
    print('Você já pode se aposentar.')
else:
    print('Você não pode se aposentar ainda.')
