"""
DESCRIÇÃO: Script para adivinhar um numero inteiro dado pelo computador de forma aleatoria.
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
from random import randint
n1 = int(input('digite  um numero de 0 a 5'))
n2 = int(randint(0,5))

if n1==n2:
    print('parabens, você ganhou')
else:
    print('infelizmente você perdeu')
