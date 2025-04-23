"""
DESCRIÇÃO: Script para obter uma listagem ordenada com os respectivos preços.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
vogais = ('a','e','i','o','u')
palavras = ('pao','arroz','feijão','tempero','manteiga')

for palavra in palavras:
    lista_vogais = list()
    for letra in palavra:
        if letra in vogais:
            lista_vogais += [letra]
    print(f'na palavra {palavra} temos as seguintes vogais: {lista_vogais}')
    
