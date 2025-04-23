"""
DESCRIÇÃO: Script gerar 5 numeros aleatorios e colocar em uma tupla.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
from random import randint

tupla2 = tuple()
for cont in range (0,5):
    var = randint(0,20)
    tupla = (var,)
    tupla2 = tupla + tupla2
    del(tupla)
print (tupla2)

for cont in range (0,5):
    if cont == 0:
        maior = tupla2[cont]
        menor = tupla2[cont]
    elif maior < tupla2[cont]:
        maior =tupla2[cont]
    elif menor > tupla2[cont]:
        menor = tupla2[cont]
print(f"o maior numero é {maior} e o menor numero é {menor}")
