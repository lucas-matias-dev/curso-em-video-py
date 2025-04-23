"""
DESCRIÇÃO: Script para conversão de temperatura de celsius para fahrenheit
AUTOR: Lucas Matias Fontoura
DATA: 05/03/2025
VERSÃO: 1.0
"""

n1 = int(input('digite quantos dias está com o carro '))
n2 = float(input('digite quantos kilometros foi percorrido com o carro '))

print('dias que vc está com o carro é {} e percorreu {} km o valor a se pagar é {}'.format(n1, n2, (n1*60)+(n2*0.15)))