"""
DESCRIÇÃO: Script para obter uma listagem ordenada com os respectivos preços.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
listagem = 'pão', 11.40, 'arroz', 13.50, 'feijão', 15.90, 'tempero', 0.90, 'manteiga', 20.00
'''
#recebendo valores com for:
for cont in range (0,10):
    if cont%2 == 0:
        nome = input("digite o nome do produto")
        listagem += (nome,)
    else:
        valor = input("digite o preço do produto")
        listagem += (valor,)
    print(listagem)
'''
for cont in range (0,10):
    if cont%2 == 0:
        print("{:15}".format(listagem[cont]),end="")
    else:
        print("R$ = {:>6.2f}".format(listagem[cont]),)
    
