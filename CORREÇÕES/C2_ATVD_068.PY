"""
DESCRIÇÃO: Script para jogar impar ou par com o computador (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 2.0 -> agora o mesmo que o codigo anterior, porem melhorado em alguns aspectos
"""
from random import randint

cont = 0
result = 0
valor = ' '
while True:
    valornum = int(input('digite um numero desejado de 0 a 10: '))
    valornumm = randint(0,10)
    valor = ' '
    while valor not in 'IP':
        valor = str(input('digite impar ou par: ')).upper().strip() [0]
    result = valornum+valornumm
    if result%2 == 0 and valor == 'P':
        cont += 1
        print(f'{result} é P, portando uma vitoria')
    elif result%2 != 0 and valor == 'I':
        cont += 1
        print(f'{result} é I, portando uma vitoria')
    else:
        print(f'{result}, pois vc escolheu {valor} vc perdeu')
        break
print(f'vc teve uma sequencia de {cont} numeros')