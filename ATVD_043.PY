"""
DESCRIÇÃO: Script para IMC .
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""
peso = float(input('digite seu peso:'))
altura = float (input('digite a sua altura:'))
imc = peso/(altura*altura)

if 18.5 > imc:
    print('abaixo do peso, seu imc é {:.2f}'.format(imc))
elif 25 >= imc >= 18.5:
    print('peso ideal, seu imc é {:.2f}'.format(imc))
elif 30 >= imc > 25:
    print('sobrepeso, seu imc é {:.2f}'.format(imc))
elif 40 >= imc > 30:
    print('obesidade, seu imc é {:.2f}'.format(imc))
else:
    print('obesidade mórbida, seu imc é {:.2f}'.format(imc))
