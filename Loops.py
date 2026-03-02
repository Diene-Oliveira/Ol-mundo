largest_number = -999999999
number = int(input("diegite um número ou digite -1 para parar"))

# Se o númro não for igual a -1, continue.
while number != -1:
    # número é maior que o maior_númro?
    if number > largest_number:
        #Sim, atualize o maior_número.
        largest_number = number
    # Insira o próximo número.
    number = int(input("Digite um número ou digite -1 para parar"))
# Imprima o maior número.
print(" O maior número é:", largest_number)
