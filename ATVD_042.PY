"""
DESCRIÇÃO: Script para saber qual é o triangulo .
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""
lado = float(input('digite o valor do lado 1:'))
lado2 = float(input('digite o valor do lado 2:'))
lado3 = float(input('digite o valor do lado 3:'))

if lado == lado2 and lado == lado3 and lado2 == lado3 :
    print('Equilatero')
elif lado != lado2 and lado != lado3 and lado2 != lado3:
    print('escaleno')
else:
    print('isoceles')