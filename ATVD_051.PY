"""
DESCRIÇÃO: Script para calcular os 10 primeiros de termos de uma PA.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
raz = float(input('digite a razão da sua P.A.'))
termo = float(input('digite o primeiro termo da sua P.A.'))
for cont in range(1,10):
    print ('o {}° da sua P.A é {}'.format(cont, termo+raz*cont))

