"""
DESCRIÇÃO: Script para jogar impar ou par com o computador (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 1.0
"""
pergunta = 'S'
sexoh = 0
maiorf = 0
maior = 0
cont3 = 0
while True:
    cont = 0
    cont2 = 0
    while cont != 1:
        if cont3 > 0:
            pergunta = str (input('digite se quer continuar')).upper().strip() [0]
        if pergunta == 'N': 
            break
        elif pergunta == 'S':
            cont = 1
        else:
            print('digite corretamente,S para continuar ou N parar')
    if pergunta =='N':
        break
    while cont2 != 1:
        sexo = str (input('digite seu sexo [M/F]: ')).upper().strip() [0]
        if sexo == 'M' or sexo == 'F':
            cont2 = 1
        else:
            print('digite corretamente M para maculino e F para feminino')
    idade = int (input('digite a sua idade: '))
    if idade > 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        maiorf += 1
    if sexo == 'M':
        sexoh += 1
    cont3 = 1
print(f'foram cadastradas {maior} pessoas maior de 18 anos')
print(f'foram cadastradas {maior} pessoas do sexo feminino com menos de 20 anos')
print(f'foram cadastradas {sexoh} do sexo masculino')