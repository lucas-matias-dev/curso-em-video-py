"""
DESCRIÇÃO: Script para obter 5 valores em uma lista.
AUTOR: Lucas Matias Fontoura
DATA: 28/03/2025
VERSÃO: 1.0
"""
lista = list()
pos_maior = list()
pos_menor = list()

for cont in range (0,5):
    lista.append(int(input(f'digite 5 valores, vc ja digitou {cont} valores: ')))
    
for cont in range (0,len(lista)):
    if lista[cont] == max(lista):
        pos_maior.append(cont)
    if lista[cont] == min(lista):
        pos_menor.append(cont)

print(f'o maior valor é {max(lista)} o indice do maior numero é {pos_maior}')
print(f'o menor valor é {min(lista)} o indice do menor numero é {pos_menor}')
        
#versão aternativa sem usar lista para dizer os indices 
del lista
lista = list()

for cont in range (0,5):
    lista.append(int(input(f'digite 5 valores, vc ja digitou {cont} valores:')))

print(f'o maior numero é {max(lista)} nos indices ', end='') 
for cont in range (0,len(lista)):
    if lista[cont] == max(lista):
        print(cont)
print(f'o menor valor é {min(lista)} nos indices ', end='')
for cont in range (0,len(lista)):
    if lista[cont] == min(lista):
        print(cont)
        
#versão aternativa sem usar max e min