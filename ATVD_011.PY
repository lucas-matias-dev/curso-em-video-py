"""
DESCRIÇÃO: Script ara calcular a area e valor de tinta necessario em L
AUTOR: Lucas Matias Fontoura
DATA: 05/03/2025
VERSÃO: 1.0
"""
n1 = float(input('digite o valor da altura da parede'))
n2 = float(input('digite o valor da largura'))

print('o a parede possui {} metros quadrados e serão necessarios {} litros de tinta'.format(n1*n2, (n1*n2)/2))
