"""
DESCRIÇÃO: Script para analise de pessoas.
AUTOR: Lucas Matias Fontoura
DATA: 20/03/2025
VERSÃO: 1.0
"""
num_idade = 0
maior_idade = 0
num_f = 0
nome2 = str('')

for cont in range (1,5):
    print('---------{}°pessoa---------'.format(cont))
    nome = str (input('nome: '))
    idade = int (input('idade: '))
    sexo = (input('sexo[M/F]')).upper()
    num_idade = num_idade + idade
    if sexo == 'F' and idade <20:
        num_f += 1
    if maior_idade < idade and sexo == 'M':
        maior_idade = idade
        nome2 = nome
        
print('{} mulheres possuem menos de 20 anos'.format(num_f))
print('o homem mais velho é {}'.format(nome2))
print('a media de idade das 4 pessoas é {}'.format(num_idade/4))
