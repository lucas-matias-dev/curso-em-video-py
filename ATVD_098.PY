"""
DESCRIÇÃO: função contador, de um em um, de dois em dois e personalizado.
AUTOR: Lucas Matias Fontoura
DATA: 10/04/2025
VERSÃO: 1.0
"""
def contador (inicio,fim,passo):
    if fim < 0:
        fim -=1
        passo2 = -1
        passo *= -1
    else:
        fim +=1 
        passo2 = 1
    for cont1 in range(inicio,fim,passo2):
        print(cont1,end=', ')
    print('FIM')
    for cont2 in range(inicio,fim,passo2*2):
        print(f'{cont2}',end=', ')
    print('FIM')
    for cont3 in range (inicio,fim,passo):
        print(f'{cont3}',end=', ')
    print('FIM')
   
    
num1 = int(input('digite o incio'))
num2 = int(input('digite o fim'))
num3 = int(input('digite o numero de passo'))

contador(inicio = num1, fim = num2, passo = num3)