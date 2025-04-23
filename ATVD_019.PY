"""
DESCRIÇÃO: Script para fazer um sorteio entre 4 alunos
AUTOR: Lucas Matias Fontoura
DATA: 06/03/2025
VERSÃO: 1.0
"""
from random import randint

n1 = str (input ('digite o nome do aluno 1') )
n2 = str (input ('digite o nome do aluno 2') )
n3 = str (input ('digite o nome do aluno 3') )
n4 = str (input ('digite o nome do aluno 4') )
 
l1 = list((n1,n2,n3,n4))
r1 = randint(1,4)
print('o aluno sorteado é {}'.format(l1[r1]))

#pode ser realizado de varias formas, por if e else, case e entre outros.