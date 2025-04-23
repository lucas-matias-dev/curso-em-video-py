"""
DESCRIÇÃO: Script para calculo de passagem.
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
n1 = int(input('digite a distancia da sua cidade em km: '))
if n1 <= 200:
    print('o preço cobrado para sua passagem é de 0,50$ por km, preço cobrado:',n1*0.50)
else: 
    print(' o preço cobrado para sua passagem é de 0,45 por km, preço cobrado: ', n1*0.45)