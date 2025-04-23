"""
DESCRIÇÃO: Script para ler varios valores e atribuir em uma lista, mostrar o tamanho,
ordenar a lista na decrescente e mostrar se o valor 5 foi digitado na lista.
AUTOR: Lucas Matias Fontoura
DATA: 01/04/2025
VERSÃO: 1.0
"""
lista = list()
resposta = 'S'
while resposta != 'N':
    if resposta == 'N':
        print('atribuições de numeros a lista encerrado')
        break
    elif resposta == 'S':
        valor = int(input('digite um valor que deseja colocar na lista'))
        lista.append(valor)
    else:
        print('digite corretamente se deseja colocar mais numeros [S/N]')
    resposta = input('digite se deseja colocar mais valores ou não [S/N]').upper().strip()[0]
        
print(f'sua lista é: {lista}')
print(f'sua lista possui um total de {len(lista)} valores')
lista.sort(reverse = True)
print(f'sua lista ordenada na decrescente é {lista}')
if 5 in lista:
    print('sua lista possui o numero 5')
else:
    print('sua lista não possui o numero 5')

    