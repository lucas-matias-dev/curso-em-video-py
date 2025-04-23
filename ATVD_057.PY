"""
DESCRIÇÃO: Script para analise de pessoas.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
sexo = 'sexo'

while sexo != 'F' and sexo != 'M':
    sexo = str(input('SEXO [M/F]: ')).upper().strip()[0]
    if sexo not in 'FM':
        print('digite corretamente o sexo')