"""
DESCRIÇÃO: Script para "rodar" um audio mp3
AUTOR: Lucas Matias Fontoura
DATA: 07/03/2025
VERSÃO: 
(07/03/2025) 1.0 -> erá atribuido o caminho do diretorio, sem o os.path.join (boas praticas)
(23/04/2025) 1.1 -> utiliza os.path.join e um pequeno tratamento em caso de diretorio errado
"""
from playsound3 import playsound
import os

diretorio = os.path.join("CURSO_EM_VIDEO","midias","firstblood.mp3")

if os.path.exists(diretorio):
    playsound(diretorio)
else:
    print('audio, não encontrado')
