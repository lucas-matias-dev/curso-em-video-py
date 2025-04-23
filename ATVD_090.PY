"""
DESCRIÇÃO: Algoritmo para obter nome, media e situação do aluno e guardar no dicionario.
AUTOR: Lucas Matias Fontoura
DATA: 09/04/2025
VERSÃO: 1.0
"""
dicio = {}
dicio ['nome'] = str(input('Digite o seu nome: '))
dicio ['media'] = float(input(f'Media de {dicio['nome']}: '))

if dicio['media'] < 6:
    dicio['situacao'] = 'reprovado'
elif dicio['media'] >= 6 and dicio['media'] < 7:
    dicio['situacao'] = 'recuperação'
elif dicio['media'] >= 7:
    dicio['situacao'] = 'aprovado'

print('-'*10,'RESULTADO','-'*10)
for keys, valores in dicio.items():
    print(f'{keys} é igual á {valores}')
    