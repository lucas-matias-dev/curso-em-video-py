"""
DESCRIÇÃO: fução para saber um maior valor entre varios.
AUTOR: Lucas Matias Fontoura
DATA: 10/04/2025
VERSÃO: 1.0
"""

def maior (lista):
    maior = 0
    for cont in lista:
        if maior == 0:
            maior = cont
        elif cont > maior:
            maior = cont
    print(f'a lista é {lista} foram informados {len(lista)} valores')
    print(f'o maior numero dessa lista foi {maior}')
        

lista1 = list()
resposta = 'S'

while resposta != 'N':
    lista1.append(int(input('digite um valor para compor a lista')))
    resposta = str(input('deseja colocar mais valores?[S/N]')).upper().strip()[0]
maior(lista1)