"""
DESCRIÇÃO: função para realizar um fatorial de um numero, sendo opcional mostrar o resultado
AUTOR: Lucas Matias Fontoura
DATA: 11/04/2025
VERSÃO: 1.0
"""
def ficha (nome = '',gols = 0):
    if nome == '':
        nome = 'desconhecido'
    print(f'o jogador {nome} fez um total de {gols} no campeonato')


nome = str(input('digite o seu nome aqui:')).strip()
gols = int(input('digite a quantidade de gols:'))

ficha(nome,gols)