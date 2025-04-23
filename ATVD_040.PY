"""
DESCRIÇÃO: Script para saber a aprovação.
AUTOR: Lucas Matias Fontoura
DATA: 19/03/2025
VERSÃO: 1.0
"""

nota = float (input('digite sua primeira: '))
nota2 = float (input('digite sua segunda nota: '))
media_nota =  (nota+nota2)/2

if media_nota >= 7.0: 
    print('você foi aprovado, sua media é {}'.format(media_nota))
elif 7 > media_nota >= 5.0:
    print('você está de recuperação, sua nota foi {}'.format(media_nota))
else:
    print('você foi reprovado')
