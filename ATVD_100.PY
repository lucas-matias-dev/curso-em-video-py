"""
DESCRIÇÃO: função para sortear 5 numeros e mostrar a soma dos numeros pares.
AUTOR: Lucas Matias Fontoura
DATA: 10/04/2025
VERSÃO: 1.0
"""

#OBS EXERCIO 100, FINALMENTE, apos 35 dias
from random import randint

def sorte (lista):
    for cont in range(0,6):
        lista.append(randint(0,10))
    print(f'a lista com numeros sorteados é {lista}')
    
def soma_pares(lista):
    soma = 0
    for cont in lista:
        if cont%2 == 0:
            soma += cont
    print(f'a soma dos pares é {soma}')
    
numeros = list()
sorte(numeros)
soma_pares(numeros)

