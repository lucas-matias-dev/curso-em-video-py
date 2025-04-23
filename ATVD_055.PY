"""
DESCRIÇÃO: Script para saber qual é o maior peso e o menor peso entre 5 pessoas.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
num = 0
num2 = 0
num3 = 0

for cont in range (0,5):
    num = float(input('digite o seu peso:'))
    if cont == 0:
        num2 = num
        num3 = num
    else:
        if num > num2:
            num2 = num
        if num < num3:
            num3 = num

print ('o maior peso é {} e o menor peso é {}'.format(num2,num3))
