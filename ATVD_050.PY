"""
DESCRIÇÃO: Script para somar apenas numeros pares em um laço for .
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
soma = int(0)
for cont in range (1,6):
    num = int(input('digite um numero'))
    if num%2 == 0:
        soma += num
print('a soma dos números pares é {}'.format(soma))