"""
DESCRIÇÃO: função para mensagem com tamanho adaptavel.
AUTOR: Lucas Matias Fontoura
DATA: 10/04/2025
VERSÃO: 1.0
"""
def escreva(txt):
    print('-'*len(txt))
    print(txt)
    print('-'*len(txt))
    
    
texto = str(input('digite um texto '))
escreva(texto)