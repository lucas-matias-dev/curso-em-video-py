"""
DESCRIÇÃO: Script para saber se um numero digitado é primo.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
from math import sqrt

num = int(input('Digite um número para análise: '))

if num < 2:
    print('Esse número não é primo.') 
elif num == 2:
    print('Esse número é primo.')
else:
    num2 = int(sqrt(num)) 
    num3 = 0

    for cont in range(2, num2 + 1):  # Checa divisores até a raiz quadrada
        if num % cont == 0:
            num3 += 1
            break  # Se encontrar um divisor, não precisa continuar

    if num3 == 0:
        print('Esse número é primo.')
    else:
        print('Esse número não é primo.')
