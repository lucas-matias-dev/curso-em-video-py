"""
DESCRIÇÃO: Algoritmo para inserir numeros diretamente ordenados.
AUTOR: Lucas Matias Fontoura
DATA: 02/04/2025
VERSÃO: 1.0
"""
lista = list()
cont2 = 0

for cont in range (0,5):
    num = int(input('digite um numero'))
    
# entrar de modo organizado, ou seja diretamente na sua posição
    if cont == 0:
        lista.append(num)
    elif cont == 1:
        if num > lista[cont-1]:
            lista.append(num)
        elif num < lista[cont-1]:
            lista.insert(0,num)
        else:
            lista.append(num)
    else:
        while True:
            if len(lista) == cont2:
                lista.append(num)
                break
            elif num > lista[cont2]:
                cont2 += 1   
            elif num < lista[cont2]:
                lista.insert(cont2,num)
                break
        cont2 = 0
print(lista)
