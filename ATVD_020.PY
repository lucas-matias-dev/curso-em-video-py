"""
DESCRIÇÃO: Script para obter uma ordem de apresentação de 4 alunos
AUTOR: Lucas Matias Fontoura
DATA: 06/03/2025
VERSÃO: 1.0
"""
from random import shuffle

n1 = input('Digite o nome do aluno 1: ')
n2 = input('Digite o nome do aluno 2: ')
n3 = input('Digite o nome do aluno 3: ')
n4 = input('Digite o nome do aluno 4: ')

l1 = [n1, n2, n3, n4]

shuffle(l1)  # Embaralha a lista no lugar

print('A ordem de apresentação é:', l1)
