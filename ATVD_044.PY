"""
DESCRIÇÃO: Script para valor das compras e formato de pagamento.
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""

val_prod = float(input('digite o valor total dos produtos'))
print('|1 - cheque/dinheiro - 10% de desconto|\n|2 - a vista cartão - 5% de desconto  |\n|3 - 2x no cartão - 0% de desconto    |\n|4 - 3x ou + no cartão - 20% de juros | ')
formapag = float(input('digite a forma desejada de pagamento'))

if formapag == 1: 
    print('o valor das suas compras ficaram no valor de {}'.format(val_prod-(val_prod*0.1)))
elif formapag == 2:
    print('o valor das suas compras ficaram no valor de {}'.format(val_prod-(val_prod*0.05)))
elif formapag == 3:
    print('o valor das suas compras ficaram no valor de {} em duas vezes'.format(val_prod))
elif formapag == 4:
    parc = int(input('deseja pagar em quantas parcelas?'))
    print('o valor das suas compras ficaram no valor de {} em {} parcelas que será pago {} por mes'.format(val_prod+(val_prod*0.2),parc,(val_prod+(val_prod*0.2))/parc))
else:
    print('opa, não temos esse formato de pagamento')