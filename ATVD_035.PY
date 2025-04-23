"""
DESCRIÇÃO: Script para saber se 3 retas podem formar um trianguo.
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""

n1 = float(input('digite o valor da sua reta 1'))
n2 = float(input('digite o valor da sua reta 2'))
n3 = float(input('digite o valor da sua reta 3'))

if (n1+n2)>n3 and (n1+n3)>n2 and (n3+n2)>n1:
    print('forma um triângulo')    
else:
    print('não é possivel formar um triângulo')
    