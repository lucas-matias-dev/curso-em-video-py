"""
DESCRIÇÃO: Script para mostrar os 10 primeiros termos mais uma quantidade desejada.
AUTOR: Lucas Matias Fontoura
DATA: 21/03/2025
VERSÃO: 1.0
"""
num2 = 0
maior = 0
menor = 0
text = 'S'
soma = 0

while text != 'N':
    num = int (input('digite um numero'))
    if num > maior: 
        maior = num 
    if num < menor or num2 == 0:
        menor = num
    num2 = num2 + 1
    soma += num
    div = soma/num2
    text = str (input('deseja continuar a colocar valores?')).upper().strip()
print('a soma dos numeros é {} a media dos numeros é {} e  o maior numero é {} e o menor numero é{}'.format(soma,div,maior,menor))