"""
DESCRIÇÃO: Script para jogar impar ou par com o computador (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 1.1 -> havia errado a codificação, pois achei que o que era pedido era para fazer 
um jogo de escolher o mesmo valor esqcolhido pela maquina (maquina impar, para ganhar, tenho que selecionar impar)
"""
from random import randint

cont = 0
result = 0

while True:
    valornum = int(input('digite um numero desejado de 0 a 10: '))
    valornumm = randint(0,10)
    valor = str(input('digite impar ou par: ')).upper().strip() [0]
    if valor == 'I':
        valorm = 'P'
    elif valor == 'P':
        valorm = 'I'
    else:
        ('valor digitado incorreto')
        break
    result = valornum+valornumm
    if result%2 == 0 and valor == 'P':
        cont += 1
        print(f'{result} é P, portando uma vitoria')
    if result%2 != 0 and valor == 'I':
        cont += 1
        print(f'{result} é I-, portando uma vitoria')
    else:
        print(f'{result} é {valorm}, portando vc perdeu')
        break
print(f'vc teve uma sequencia de {cont} numeros')