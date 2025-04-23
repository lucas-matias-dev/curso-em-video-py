"""
DESCRIÇÃO: Script para calculadora.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
from time import sleep

n1 = 0
cont = 0
num = 0
num2 = 0

while n1 != 5:
    print('| 1 - soma            |\n| 2 - multiplicação   |\n| 3 - maior           |\n| 4 - novos numeros   |\n| 5 - sair do programa|')
    print('numeros em memoria são {} e {}'.format(num, num2))
    n1 = int(input('digite o que deseja fazer '))
    if cont == 0 or n1 == 4: 
        num = int (input('digite o primeiro numero: '))
        num2 = int (input('digite o segundo numero: '))
    if n1 == 1:
        print ('a soma entre {} e {} resulta em {}'.format(num, num2, num + num2))
    elif n1 == 2:
        print ('a multiplicação entre {} e {} resulta em {}'.format(num, num2, num2 * num))
    elif n1 == 3:
        if num > num2:
            print('{} é maior que {}'.format(num, num2))
        elif num < num2:
            print('{} é maior que {}'.format(num2, num))
        else:
            print('numeros iguais')
    elif n1 > 5 or n1 < 0:
        print ('opção invalida, digite novamente')
    sleep(2)
    cont = cont + 1
    
