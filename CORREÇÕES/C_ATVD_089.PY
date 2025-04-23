"""
DESCRIÇÃO: Algoritmo para obter um nome, duas notas, media das notas e deixar em uma lista.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.1. apenas algumas mudanças de otimização (incompleto)
"""
lista = list()
lista2 = list()
resposta = 'S'
nota1 = nota2 = media = i = 0.0
while resposta != 'N':
    nome = str(input('digite o seu nome: '))
    nota1 = float(input('digite a sua nota1: '))
    nota2 = float(input('digite a sua nota2: '))
    media = (nota1+nota2)/2
    lista = [nome,media,[nota1,nota2]]
    lista2.append(lista.copy())
    lista.clear()
    resposta = str(input('deseja continuar ou parar [S/N]')).upper().strip()[0]
for cont in lista2:
    i+=1
    print(f'{i}seu nome é {cont[0]} e sua media é {cont[1]}')
while i != 999:
    i = int(input('digite o numero do aluno que deseja ver'))
    if i == 999:
        print('programa finalizado')
        break
    elif i > len(lista2) or i < 0:
        print('digite corretamente o numero')
    else:
        print(lista2[i])
