"""
DESCRIÇÃO: Script de caixa de supermercado (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 1.0
"""
cont = 0
pergunta ='S'
valortotal = 0
mil = 0
while True:
    if cont > 0:
        pergunta = str (input('deseja colocar passar mais produtos? ')).upper().strip() [0]
    if pergunta == 'N':
        break
    nomeprod = str (input('digite o nome da sua compra: '))
    valorprod = float (input('digite o valor da sua compra: '))
    valortotal += valorprod
    if cont == 0:
        menorn = nomeprod
        menorv = valorprod
    elif valorprod < menorv:
        menorn = nomeprod
        menorv = valorprod
    if valorprod > 1000:
        mil += 1 
    cont += 1
print(f'o total gasto em compras foi {valortotal} com um total de {cont} produtos')
print(f'{mil} produtos custaram mais de mil reais')
print(f'o produto mais barato é {menorn} custando {menorv}')
    