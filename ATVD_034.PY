"""
DESCRIÇÃO: Script para determinar qual é o maior entre 3 números
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
n1 = float(input('digite o valor do seu salario:'))
if n1>1249.99:
    print('seu aumento é de 10% sobre o seu salario então obteve um aumento de {} e seu salario é {}'.format(n1*0.10, n1+(n1*0.10)))
else:
    print('seu aumento é de 15% sobre o seu salario então obteve um aumento de {} e seu salario é {}'.format(n1*0.15, n1+(n1*0.15)))