"""
DESCRIÇÃO: Script para determinar qual é o maior entre 3 números
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
n1 = int(input('digite um número: ')) 
n2 = int(input('digite um número: ')) 
n3 = int(input('digite um número: ')) 
    
if n1>n2 and n1>n3:
    print('o numero {} é o maior número entre os citados'.format(n1))
elif n2>n1 and n2>n3:
    print('o número {} é o maior numero entre os citados'.format(n2))    
else:
    print('o número {} é o maior número entre os citados'.format(n3))

