"""
DESCRIÇÃO: Algoritmo para cadastro de pessoas utilizando, nome, idade, ctps, salario, ano de contratação, aposentadoria.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""
from datetime import datetime

pessoa = {}
pessoa['nome'] = str(input('digite o seu nome: '))
pessoa['idade'] = datetime.now().year - int(input('digite o seu ano de nascimento: '))
pessoa['carteira de trabalho'] = int(input('digite a sua carteira de trabalho: '))

if pessoa['carteira de trabalho'] != 0:
    pessoa['tempo de contribuição'] = datetime.now().year - int(input('digite o ano de contratação: '))
    pessoa['salario'] = float(input('digite o seu salario'))
    if pessoa['tempo de contribuição'] >= 35:
        pessoa['aposentar'] = 'aposentado'
    elif pessoa['tempo de contribuição'] < 35:
        pessoa['tempo até aposentar'] = 35 - pessoa['tempo de contribuição']
    print()
    
for keys, valor in pessoa.items():
    print(f'o dado: {keys} é {valor}')