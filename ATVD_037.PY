"""
DESCRIÇÃO: Script para conversão de valores em binario, octal e hexadecimal.
AUTOR: Lucas Matias Fontoura
DATA: 18/03/2025
VERSÃO: 1.0
"""

num = int (input('digite um valor desejado: '))
print ('se deseja converter para \n 1 - binário \n 2 - octal \n 3 - hexadeciamal')
num2 = int (input('digite qual operação deseja realizar: '))

if num2 == 1:
    print('binario é {}'.format(bin(num)[2:]))
elif num2 == 2:
    print ('o seu valor em octal é {2:}'.format(oct(num)[2:]))
elif num2 == 3:
    print('o seu valor em hexadecimal é {}'.format(hex(num)))
else:
    print('opção invalida')