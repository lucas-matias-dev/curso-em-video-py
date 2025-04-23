"""
DESCRIÇÃO: Script para obter algumas informações do brasileirão.
AUTOR: Lucas Matias Fontoura
DATA: 26/03/2025
VERSÃO: 1.0
"""
brasileiro = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama','Vitória','Atlético Mineiro',
'Fluminense','Grêmio','Juventude','Bragantino','Athletico Paranaense','Criciúma','Goianiense','Cuiabá','Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional',
'São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama','Vitória','Atlético Mineiro','Fluminense','Grêmio','Juventude','Bragantino','Athletico Paranaense',
'Criciúma','Goianiense','Cuiabá')

print(f"os 5 primeiros colocados são {brasileiro[:5]}\n")
print(f"os 4 ultimos  colocados são {brasileiro[-4:]}\n")
print(f"os times em ordem alfabetica é {sorted(brasileiro)}\n")
print(f"o internacional está na posição {brasileiro.index("Internacional")+1}\n")
