"""
DESCRIÇÃO: Script de radar, caso acima de 80, multa de 7,00 a cada km acima do limite.
AUTOR: Lucas Matias Fontoura
DATA: 15/03/2025
VERSÃO: 1.0
"""
n1 = int(input('digite a sua velocidade do seu carro: '))
if n1>80:
    print('você foi multado e sua muta é de {} reais'.format((n1-80)*7,00))
else:
    print('tudo correto, você não foi multado')
