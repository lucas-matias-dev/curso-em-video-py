"""
DESCRIÇÃO: Script para jogar impar ou par com o computador (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 1.0
"""
from random import choice, randint

cont = 0

while True:
    valor = str (input('digite impar ou par: ')).upper().strip() [0]
    valorm = str(choice(['I','P']))
    if valor != valorm:
        print('vc perdeu, infelizmente')
        break
    else:
        cont+=1
    print('parabens, vc acertou')
print(f'vc teve umas sequencia de {cont} vitorias')
    
#versão 2.0, melhorando o codigo.
cont = 0
result = 0
valor = 0
while True:
    valornum = int(input('digite um numero desejado de 0 a 10: '))
    valornumm = randint(0,10)
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
        print(f'{result} é, portando vc perdeu')
        break
print(f'vc teve uma sequencia de {cont} numeros')
