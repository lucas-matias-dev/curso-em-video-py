"""
DESCRIÇÃO: Script para saber se um jovem já se alistou, se vai, ou se passou.
AUTOR: Lucas Matias Fontoura
DATA: 18/03/2025
VERSÃO: 1.0
"""
from datetime import datetime 

#versão 1.0 utilizando data de modo não automatico
dtnasc = int(input('digite sua data de nascimento: '))
idade = 2025-dtnasc

#versão 2.0, de modo automatico.
idade =  datetime.now().year - dtnasc

if idade > 18:
    print('passou do tempo do alistamento militar, pois vc deve fazer {} nesse ano'.format(idade))
elif idade < 18:
    print('ainda vai alistar, pois vc deve fazer {} nesse ano'.format(idade))
else:
    print('vc deve se alistar esse ano, pois vc faz {} esse ano'.format(idade))

