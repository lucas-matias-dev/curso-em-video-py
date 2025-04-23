"""
DESCRIÇÃO: Script para saber qual valor é maior ou igual entre dos valores.
AUTOR: Lucas Matias Fontoura
DATA: 18/03/2025
VERSÃO: 1.0
"""

num = int (input('digite o primeiro valor que deseja comparar: '))
num2 = int (input('digite o segundo valor que deseja comparar: '))

if num > num2:
    print('o numero {} é maior que o {}'.format(num, num2))
elif num2 > num:
    print('o numero {} é maior que o {}'.format(num2,num))
else:
    print('os dois numeros são iguais')