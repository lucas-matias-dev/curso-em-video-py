"""
DESCRIÇÃO: Script para fazer a tabuada com laço.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
num = int (input('digite numero que deseja saber a tabuada'))

for cont in range (1,11):
    print('{} x {} = {}'.format(num,cont,num*cont))

