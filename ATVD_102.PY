"""
DESCRIÇÃO: função para realizar um fatorial de um numero, sendo opcional mostrar o resultado
AUTOR: Lucas Matias Fontoura
DATA: 11/04/2025
VERSÃO: 1.0
"""
def fatorial(numero, show = None):
    fator = 1
    for cont in range (numero, 0, -1):
        fator *= cont
    if show == True: 
        print(fator)
        
        
n1 =  int(input('digite um numero para realizar o fatorial'))
n2 = str(input('deseja mostrar o resultado [S/N]: ')).strip().upper()[0]

if n2 == 'S':
    n2 = True
else:
    n2 = False
    
fatorial(n1,n2)