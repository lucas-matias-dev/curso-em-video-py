"""
DESCRIÇÃO: Script para somar todos os numeros multiplos de 3 entre 1 e 500.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
soma = 0
soma2 = 0

for cont in range(3,500,3):
    if cont%2 == 0:
        soma = soma + cont
    else:
        soma2 = soma2 + cont
print(soma2)

#versão 1.1 (corrigida)
soma3 = 0
num = 0
for cont in range (1,501,2):
    if cont%3 == 0:
        soma3 = soma3+cont
        num = num + 1
print(' a soma entre todos os numeros impares de 1 a 500 que são {} resulta em {}'.format(num,soma3))