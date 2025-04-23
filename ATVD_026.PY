"""
DESCRIÇÃO: Script para analise de uma string
AUTOR: Lucas Matias Fontoura
DATA: 08/03/2025
VERSÃO: 1.0
"""

n1 = str(input('digite uma frase qualquer'))
print('sua frase possui {} caracteres "a"'.format(n1.count('a')))
print('sua frase aparece pela primeira vez em', n1.find('a'))
print('sua frase aparece pela primeira vez em', n1.rfind('a'))

