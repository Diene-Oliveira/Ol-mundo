#entradas/variaveis
preco_amaciante1 = float(input('digite o preço do 1º amaciante R$'))
preco_amaciante2 = float(input('digite o preço do 2º amaciante R$'))
#processos
if preco_amaciante1<preco_amaciante2:
    mais_caro = "O primeiro amaciante é o mais barato"
elif preco_amaciante2<preco_amaciante1:
    mais_caro = "O segundo amaciante é o mais caro"
else:
    mais_caro = "O 2º amaciante tem o preço mais caro"
    #saídas
    print(mais_caro)
