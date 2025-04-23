"""
DESCRIÇÃO: Algoritmo para obter 7 valores e separar em duas listas (par e impar) em ordem crescente.
AUTOR: Lucas Matias Fontoura
DATA: 06/04/2025
VERSÃO: 1.0
"""
lista = [[],[]]

for cont in range (0,7):
    num = int(input('digite um valor para compor a sua lista'))
    if num%2 == 0:
        lista[1].append(num)
    if num%2 == 1:
        lista[0].append(num)  
    lista[0].sort()
    lista[1].sort()
print(f'os valores pares digitados foram {lista[1]}')
print(f'os valores impares digitados foram {lista[0]}')
