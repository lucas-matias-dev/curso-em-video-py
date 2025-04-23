"""
DESCRIÇÃO: Script para mostrar os 10 primeiros termos mais uma quantidade desejada.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
n1 = int (input('digite um numero de termos a serem apresentados de uma sequencia de fibonacci'))
n3 = 0
n2 = 0
cont = 0
while cont != n1:
    result = n2 + n3
    n2 = n3
    n3 = result
    print(result,end='->')  
    if n2 == 0 and cont == 0:
        n2 = n2 + 1
    cont = cont + 1 
print('end')