"""
DESCRIÇÃO: Script para mostrar os 10 primeiros termos
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
num = int (input('digite o primeiro termo da sua PA'))
raz = int (input('digite a razão da sua PA'))
cont=0

while cont != 10:
    cont = cont+1
    res = num + (cont-1)*raz
    print('o termo de numero {} é {}'.format(cont,res))
    