"""
DESCRIÇÃO: Algoritmo para soma dos valores pares de uma matriz, soma da terceira coluna de uma matriz
e o maior valor da segunda linha.
AUTOR: Lucas Matias Fontoura
DATA: 06/04/2025
VERSÃO: 1.0
"""
matriz = [[],[],[]]
maior = None
soma = int()
soma_col3 = int()

for cont1 in range (0,3):
    for cont2 in range(0,3):
        num = int(input(f'digite um numero para compor a posição[{cont1},{cont2}]'))
        if num%2 == 0:
            soma += num
        if cont2 == 2:
            soma_col3 += num
        if cont1 == 2:
            if maior == None:
                maior = num
            elif maior < num:
                maior = num
        matriz[cont1].append(num)
matriz.sort()

print('a sua matriz está da seguinte forma:')
print(matriz[0])
print(matriz[1])
print(matriz[2])
print(f'a soma de todos os valores pares é {soma}')
print(f'a soma dos valores da terceira coluna é {soma_col3}')
print(f'o maior valor da segunda linha é {maior}')