"""
DESCRIÇÃO: Script para mostrar os 10 primeiros termos mais uma quantidade desejada.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""

num = int(0)
soma = 0
num2 = 0

while num != 999:
    num = int(input('digite um numero'))
    if num != 999:
        soma = num+soma
        num2 = num2+1
print('foram digitados {} e a soma dos numeros é {}'.format(num2,soma))

#versão alternativa (melhorado, pois não há uma verificação dentro do while)
while num != 999:
    num = int(input('digite um numero'))
    soma = num+soma
    num2 = num2+1
print('foram digitados {} e a soma dos numeros é {}'.format(num2 - 1,soma - 999))

#versão alternativa (mais clean)
num = int(input('digite um numero'))
while num != 999:
    soma = num+soma
    num2 = num2+1
    num = int(input('digite um numero'))
print('foram digitados {} e a soma dos numeros é {}'.format(num2 - 1,soma - 999))
