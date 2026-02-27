#Variáveis/Entradas 
valor_hora = 60.20
horas_trabalhadas = int(input("Quantas horas foram trabalhadas?"))
#Processos
if horas_trabalhadas<=20:
    salario = valor_hora*horas_trabalhadas
else:
    adicional = valor_hora*0.3
    salario = valor_hora*horas_trabalhadas+adicional
#saidas
print(f'o funcionário receberá {salario}de salário')

#ternário python
