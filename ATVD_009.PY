"""
DESCRIÇÃO: Script para obter a tabuada de um número qualquer 
AUTOR: Lucas Matias Fontoura
DATA: 05/03/2025
VERSÃO: 1.0
"""

n1=int(input('digite um número para saber a tabuada desse número'))
print(''' 1 x {1} = {2}\n 2 x {1} = {3} \n 3 x {1} = {4} \n 4 x {1} = {5} \n 5 x {1} = {6}
 6 x {1} = {7} \n 7 x {1} = {8} \n 8 x {1} = {9} \n 9 x {1} = {10} \n 10 x {1} = {11} \n'''
.format(n1, n1, n1*1, n1*2, n1*3, n1*4, n1*5, n1*6, n1*7, n1*8, n1*9, n1*10 )) 
