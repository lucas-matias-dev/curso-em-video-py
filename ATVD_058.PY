"""
DESCRIÇÃO: Script para um jogo de advinhação.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
from random import randint
from time import sleep

cont = 0
num3 = 0
while cont !=1:
    num = int (input('digite um valor para tentar adivinhação'))
    num3 += 1
    num2 = randint(0,10)
    print('aguarde, maquina pensando',end='')
    for time in range (0,3):
        if time < 2:
            print('.', end='')
            sleep(2)
        else:
            print('.')
            sleep(2)
    if num2 == num:
        print('parabens, vc acertou, maquina digitou {} e vc digitou {} com um total de {} tentativas'.format(num2, num, num3))
        cont = 1
    else:
        print('vc errou, maquina digitou {} e vc digitou {}, ate o momento foram {} tentativas.'.format(num2, num, num3))

#obs: for na linha 15 serve apenas de caracter estetico