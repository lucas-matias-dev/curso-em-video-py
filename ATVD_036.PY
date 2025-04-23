"""
DESCRIÇÃO: Script para aprovar um emprestimo bancario.
AUTOR: Lucas Matias Fontoura
DATA: 18/03/2025
VERSÃO: 1.0
"""
valcasa = float(input('digite o valor da sua casa: '))
valsalario = float(input('digite o valor do seu salario: '))
anos = int (input('digite quantos anos pretende pagar: '))

meses = int (anos*12)
valsalario = valsalario*0.3
valcasa = (valcasa/meses)

if valcasa > valsalario:
    print('emprestimo negado')
else:
    print('emprestimo aceito, suas prestações estão fixadas em {:.2f} por mes e serão {} parcelas por mes'.format(valcasa, meses))