"""
DESCRIÇÃO: Script para calcular o fatorial de um numero.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
#6*5*4*3*2*1
n1 = int (input('digite o numero que deseja obter fatorial'))
c = n1 
fat = 1

while c > 0:
    fat = fat * c
    c = c - 1
    print (fat)