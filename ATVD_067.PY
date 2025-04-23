"""
DESCRIÇÃO: Script para somar uma quantidade indeterminada de termos (utilizando brake).
AUTOR: Lucas Matias Fontoura
DATA: 22/03/2025
VERSÃO: 1.0
"""
num = cont = 0
while True:
    num = int (input('digite um numero para saber a tabuada desse número'))
    cont = 0
    if num < 0:
        break
    while cont != 11:
        print (f'{num} x {cont} = {num*cont}')
        cont += 1
