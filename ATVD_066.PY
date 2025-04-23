"""
DESCRIÇÃO: Script para somar uma quantidade indeterminada de termos (utilizando brake).
AUTOR: Lucas Matias Fontoura
DATA: 22/03/2025
VERSÃO: 1.0
"""
num = cont = soma = 0
while num != 999:
    num = int(input('digite um número: '))
    if num == 999:
        break
    cont += 1
    soma = num+soma
print(f'foram digitados {cont} e a soma foi {soma}')