"""
DESCRIÇÃO: Script para determinar se o ano é bissexto
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
n1 = int(input('digite um ano desejado: ')) 
    
if n1%100==0 and n1%400==0:
    print('seu ano é bissexto')
elif n1%4==0:
    print('seu ano é bisstexto')    
else:
    print('seu ano não é bissexto')
