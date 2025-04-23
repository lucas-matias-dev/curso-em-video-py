"""
DESCRIÇÃO: Script para jogar impar ou par com o computador (brake).
AUTOR: Lucas Matias Fontoura
DATA: 23/03/2025
VERSÃO: 2.0 mudanças -> utilizei not in antes era um sistema meio "arcaico", utilizava um principio de contagem
e utilizava uma maior quantidade de if (atualmente reduzido) 
"""
maior = sexoh = cont3 = maiorf = 0 

while True:
    sexo = ' '
    pergunta = ' '
    if cont3 > 0:
        while pergunta not in 'SN':
            pergunta = str (input('digite se quer continuar')).upper().strip() [0]
    if pergunta =='N':
        break
    while sexo not in 'MF':
        sexo = str (input('digite seu sexo [M/F]: ')).upper().strip() [0]   
    idade = int (input('digite a sua idade: '))
    if idade > 18:
        maior += 1
    if idade < 20 and sexo == 'F':
        maiorf += 1
    if sexo == 'M':
        sexoh += 1
    cont3 += 1
print(f'foram cadastradas {maior} pessoas maior de 18 anos')
print(f'foram cadastradas {maior} pessoas do sexo feminino com menos de 20 anos')
print(f'foram cadastradas {sexoh} do sexo masculino')