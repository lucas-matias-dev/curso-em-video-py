"""
DESCRIÇÃO: função para saber a area de um retangulo.
AUTOR: Lucas Matias Fontoura
DATA: 10/04/2025
VERSÃO: 1.0
"""
def area(base,altura):
    print(f'a area do terreno é {base}x{altura} é de {base*altura} metros quadrados')

print('-'*20,'CONTROLE DE TERRENO','-'*20)
num = float(input('digite a largura(M) '))
num2 = float(input('digite o comprimento(M) '))

area(num,num2)