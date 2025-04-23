"""
DESCRIÇÃO: Algoritmo para mega sena.
AUTOR: Lucas Matias Fontoura
DATA: 07/04/2025
VERSÃO: 1.0
"""
from random import randint

cont2 = 0
lista1 = list()
lista2 = list()
jogos = int(input('digite a quantidade de palpites que deseja'))


for cont in range (0,jogos):
    while cont2 != 6:
        num = randint(0,60)
        if num not in lista1:
            lista1.append(num)
            cont2 += 1
    lista2.append(lista1.copy())
    lista2.sort()
    lista1.clear()
    cont2 = 0
    print(f' o jogo de numero {cont}: {lista2[cont]}')
        