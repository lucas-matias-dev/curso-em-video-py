"""
DESCRIÇÃO: Script para saber se o nome da cidade digitada começa com santos
AUTOR: Lucas Matias Fontoura
DATA: 09/03/2025
VERSÃO: 1.1
"""

n1 = str(input('digite o nome da sua ciadade:'))
n1 = n1.title()
print(n1)
n1 = n1.split()
print ('sua cidade começa com',n1[0])

#versão 1.1/correção 
print('portanto, sua cidade começa com santos:',"Santos" in n1[0])