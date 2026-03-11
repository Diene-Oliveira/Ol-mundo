import random
usuario = imput("Digite pedra, papel ou tesoura: ")
opcoes = ["pedra", "papel", "tesoura"]
Computador = randon.choice(opcoes)

print("computador escolheu:", computador)

if usuario == computador:
    print("empate")

elif usuario == "pedra":
    if Computador == "tesoura":
        porint("você ganhou")
    else:
        print("computador")
