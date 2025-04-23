"""
DESCRIÇÃO: Script gerar 5 numeros aleatorios e colocar em uma tupla.
AUTOR: Lucas Matias Fontoura
DATA: 27/03/2025
VERSÃO: 1.1, retirada dos for's (ocorrendo melhora/simplificação no codigo.)
""" 
from random import randint

numeros = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

print(f"os numeros sorteados são {numeros}")
print(f"o mmaior valor em numeros é {max(numeros)}")
print(f"o menor numero é {min(numeros)}")
