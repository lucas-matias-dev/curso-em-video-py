"""
DESCRIÇÃO: Script para para ordenação de numeros em uma lista sem usar o sort.
AUTOR: Lucas Matias Fontoura
DATA: 01/04/2025
VERSÃO:
(01/03/2025)1.0 -> código sem correção da descrição
(23/04/2025)1.1 -> código com descrição corrigida 
"""
lista = list()
for cont1 in range (0,5):
    lista.append(int(input('digite um numero')))    
    
for cont2 in range (0,len(lista)):
    for cont in range (0,len(lista)-1):
        if lista[cont] > lista[cont+1]:
            num = lista [cont+1]
            lista[cont+1] = lista [cont]
            lista[cont] = num
print(lista) 

#necessrio correção, pois o metodo usado é o bubble sort
#versão correta: ordenação ao digitar um valor, o valor ja deve entrar de forma ordenada na lista