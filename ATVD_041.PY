"""
DESCRIÇÃO: Script para saber se é mirin, infantil, junior, sênior, master.
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""
from datetime import datetime
idade = int(input('digite seu ano de nascimento: '))
idade = datetime.now().year - idade

print(idade)
if idade <= 9:
    print('você é um mirin')
elif 14 >= idade > 9:
    print('infantil')
elif 19 >= idade > 14:
    print ('junior')
elif 20 == idade:
    print('sênior')
else:
    print('master')
    