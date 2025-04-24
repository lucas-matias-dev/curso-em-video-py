"""
DESCRIÇÃO: Script para colocar varios valores numericos em uma lista sem repetir valores.
AUTOR: Lucas Matias Fontoura
DATA: 28/03/2025
VERSÃO: 
(28/03/2025)1.0 -> código sem correção da descrição
(23/04/2025)1.1 -> código com descrição corrigida 

"""
lista = list()
while True:
    num = int(input('digite um valor para adicionar a lista'))
    if num not in lista:
        lista.append(num)
    else:
        print('esse valor já foi digitado')
    desejo = str(input('deseja continuar ou parar [S/N]')).strip().upper()[0]
    if desejo == 'N':
        break
    elif desejo not in 'SN':
        print('vc não digitou corretamente se deseja parar ou continuar, portanto, programa encerrado')
        break
lista.sort()
print(f'sua lista ficou dessa forma {lista}')