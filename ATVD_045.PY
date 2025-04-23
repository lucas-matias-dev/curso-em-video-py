"""
DESCRIÇÃO: Script para jogar jokenpô.
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""
from random import randint
from time import sleep

num = int(input('2 - pedra \n1 - tesoura \n0 - papel \ndigite valor do escolhido: '))
nummachine = randint(0,2)
opc = list (["papel","tesoura","pedra"])


print('JO')
sleep(1)
print('KE')
sleep(1)
print('PO')

if num == nummachine:
    print('empate oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 2 and nummachine == 1:
    print('vc ganhou, parabens. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 2 and nummachine == 0:
    print ('vc perdeu, infelizmente. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 1 and nummachine == 0:
    print('você ganhou, parabens. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 1 and nummachine == 2:
    print('vc perdeu, infelizmente. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 0 and nummachine == 2:
    print('vc ganhou, parabens. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
elif num == 0  and nummachine == 1:
    print('vc perdeu, infelizmente. Oponente jogou {} e vc jogou {}'.format(opc[nummachine],opc[num]))
else:
    print('você jogou um numero invalido {}'.format(num))