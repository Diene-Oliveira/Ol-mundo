def soma(number1, number2):
    return number1+number2
def subtração(number1, number2):
    return number1-number2
def multiplicação(number1, number2):
    return number1*number2
def divisão(number1, number2):
    return number1/number2
def exponenciação(number1, number2):
    return number1**number2
number1= int(input("digite o primeiro número:"))
number2= int(input("digite o segundo número:"))
operacao= str(input("digite a operacao (soma/ subtração/ divisão/ multiplicação/ exponenciação):"))
if operacao == "soma":
    print("O valor da soma é:",soma(number1, number2))
elif operacao == "sutração":
    print("O valor da subtração é:",subtração(number1, number2))
elif operacao == "multiplicação":
    print("O valor da multiplicação é:",multiplicação(number1, number2))
elif operacao == "divisão":
    print("O valor da divisão é:",divisão(number1, number2))
elif operacao == "exponenciação":
    print("O valor da exponenciação é:",exponenciação(number1, number2))
else: 
    print("oprecao invalida")
