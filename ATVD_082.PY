"""
DESCRIÇÃO: Algoritmo para atribuir valores a uma lista e mostrar uma lista separada de valores pares e impares.
AUTOR: Lucas Matias Fontoura
DATA: 01/04/2025
VERSÃO: 1.0
"""
resposta = 'S'
lista = list()
lista_par = list()
lista_impar = list()

while resposta != 'N':
    if resposta == 'S':
        lista.append(int(input('digite um numero para adicionar a lista')))
    elif resposta == 'N':
        print('programa de atribuições encerrado')
        break
    else:
        print('digite corretamente se deseja continuar ou parar [S/N]')
    resposta = str(input('digite se deseja continuar ou parar [S/N]')).upper().strip()[0]
    
for num in lista:
    if num%2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
print(f'A lista principal é {lista}')
print(f'A lista par é {lista_par}')
print(f'A lista impar é {lista_impar}')