"""
DESCRIÇÃO: Script para saber quantas pessoas atingiram maioridade.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
from datetime import datetime

soma = 0
soma2 = 0

for cont in range (0,7):
    idade = int (input('digite seu ano de nascimento'))
    idade = datetime.now().year - idade 
    if idade >= 18:
        print('vc é de maior') 
        soma += 1
    else:
        print('vc não é maior de idade')
        soma2 += 1
print ('A quantidade de pessoas que é maior de idade é {} e menores de idade é {}'.format (soma,soma2))