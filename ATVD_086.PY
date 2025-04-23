"""
DESCRIÇÃO: Algoritmo para fazer uma matriz.
AUTOR: Lucas Matias Fontoura
DATA: 06/04/2025
VERSÃO: 1.0
"""
matriz = [[],[],[]]

for cont1 in range (0,3):
    for cont2 in range(0,3):
        matriz[cont1].append(int(input(f'digite um valor para compor a posição [{cont1},{cont2}]')))
matriz.sort()
print('a sua matriz está da seguinte forma:')
print(matriz[0])
print(matriz[1])
print(matriz[2])