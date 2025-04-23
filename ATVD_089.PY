"""
DESCRIÇÃO: Algoritmo para mostrar boletim de alunos usando uma lista .
AUTOR: Lucas Matias Fontoura
DATA: 07/04/2025
VERSÃO: 1.0
"""
resposta = 'S'
cont = 0 
lista = list()
lista_final = list()
resposta2 = None

while resposta != 'N':
    nome =  str(input('digite o seu nome:'))
    nota1 = float(input('digite a sua nota1:'))
    nota2 = float(input('digite a sua nota2:'))
    lista.append(nome)
    lista.append([nota1,nota2])
    lista_final.append(lista.copy())
    lista.clear()
    resposta = str(input('digte se deseja continuar[S/N]')).strip().upper()[0]
    cont += 1
for cont2 in range (0,cont):
    num1 = lista_final[cont2][1][0]
    num2 = lista_final[cont2][1][1]
    media = (num1+num2)/2
    print(f'o numero do aluno é {cont2} nome do aluno é {lista_final[cont2][0]} e sua media foi {media}')
while resposta2 != 999:
    resposta2 = int(input('digite o numero do aluno que deseja ver (999 interrompe)'))
    if resposta2 < cont:
        print(f'o nome do aluno é {lista_final[resposta2][0]} e suas notas são {lista_final[resposta2][1]}')
    elif resposta2 == 999:
        break
    else:
        print('digite corretamente o numero do aluno')