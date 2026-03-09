def calculo_peso(peso):
    agua = peso*15
    copo = int(agua/250)
    return copo
peso = int(input("Qual o peso de Lucas(kg):"))
print("copos nescessarios:", calculo_peso(peso))
