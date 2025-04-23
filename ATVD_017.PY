"""
DESCRIÇÃO: Script para obter a hipotenusa atraves dos dois catetos 
AUTOR: Lucas Matias Fontoura
DATA: 06/03/2025
VERSÃO: 1.0
"""
from math import pow, sqrt

n1 = float(input('digite o valor do cateto 1 '))
n2 = float(input('digite o valor do cateto 2 '))
n3 = (pow(n1,2))+(pow(n2,2))
print('o valor do cateto 1 é {}, o valor do cateto 2 é {} e o valor da hipotenusa é {}'.format(n1,n2,sqrt(n3)))
