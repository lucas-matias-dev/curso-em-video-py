"""
DESCRIÇÃO: Script para apresentar uma variavel tipo string de diversas formas
AUTOR: Lucas Matias Fontoura
DATA: 09/03/2025
VERSÃO: 
(09/03/2025)1.0 -> código sem correção
(22//04/205)1.1 -> correção de código
"""
n1 = str(input('digite seu nome aqui: ')).strip()

print ('seu nome em letras maiusculas é: ',n1.upper())
print ('seu nome com toda as letras em minusculo é: ',n1.lower())
print ('a quantidade de digitos do seu nome é {} sem contar os espaços'.format(len(n1) - n1.count(' ')))

n2 = list(n1.split())

print ('seu primeiro nome é',n2[0],'e seu primeiro nome possui',len(n2[0]))


