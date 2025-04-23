"""
DESCRIÇÃO: Algoritmo para 4 jogadores jogarem um dado.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""
from random import randint
from time import sleep
from operator import itemgetter

dicio = {} 
dicio_org = {}

dicio['jogador1'] = randint(1,6)
dicio['jogador2'] = randint(1,6)
dicio['jogador3'] = randint(1,6)
dicio['jogador4'] = randint(1,6)
print(dicio)

for keys, valor in dicio.items():
    print(f'o {keys} tirou o numero: {valor}')
    sleep(1)
    
dicio_org = sorted(dicio.items(), key = itemgetter(1), reverse = True)

for keys, valor in enumerate(dicio_org):
    print(f'o {keys+1}° colocado é {valor[0]} e tirou {valor[1]}')
    sleep(1)