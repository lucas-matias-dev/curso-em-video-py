"""
DESCRIÇÃO: Script para identificar se uma string é polidromo.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
frase = str (input('digite sua string para saber se é um polidromo: '))

if ' ' in frase:
    frase = frase.replace(' ','')
    
frase2 = frase
frase = frase[::-1]

if frase == frase2:
    print('A frase digitada é um polidromo')
else:
    print('a frase digitada não é um polidromo')
