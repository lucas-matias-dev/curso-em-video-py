"""
DESCRIÇÃO: Script para obter a tangente, cosseno e seno atraves de um angulo
AUTOR: Lucas Matias Fontoura
DATA: 06/03/2025
VERSÃO: 1.0
"""
from math import radians, cos, sin, tan

n1 = float(input('digite o valor do angulo'))
n1 = radians(n1)
print ('tangente do seu angulo é {} o cosseno é {} e o seno é {}'.format(cos(n1),sin(n1),tan(n1)))
