"""
DESCRIÇÃO: função voto, função para saber se o voto de uma pessoa é negado, opcional ou obrigatorio.
AUTOR: Lucas Matias Fontoura
DATA: 11/04/2025
VERSÃO: 1.0
"""

def voto (ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade <= 15:
        resposta = str('negado')
    elif idade < 18 and idade > 15:
        resposta = str('opcional')
    elif idade >= 18:
        resposta = str('obrigatorio')
    return resposta
    
    
data_nascimento = int (input('digite seu ano de nascimento'))
print(f'vc pode votar: {voto(data_nascimento)}')
