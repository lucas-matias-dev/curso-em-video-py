"""
DESCRIÇÃO: Script para mostrar os 10 primeiros termos mais uma quantidade desejada.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
num = int (input('digite o primeiro termo'))
raz = int (input('digite a razão do sua PA'))
laco2 = 10
laco1 = 1
num1 = 0

while laco1 != 0:
    saidalaco = laco2
    while num1 != laco2 :
        result = num+num1*raz
        print(result)
        num1 += 1
    laco1 = int (input('digite quantos termos deseja ver'))
    if laco1 > 0:
        laco2 = laco1 + saidalaco
    else:
        laco1 == 0
print('a quantidade de termos total foi {}'.format(laco2))