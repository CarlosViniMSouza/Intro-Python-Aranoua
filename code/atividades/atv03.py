# Primeiro Problema
num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))

if num1 > num2:
    print(f"{num1} eh maior que {num2}")
elif num1 < num2:
    print(f"{num2} eh maior que {num1}")
else:
    print(f"{num1} eh igual a {num2}")

"""
output:
Insira um numero: 5
Insira outro numero: 8
8 eh maior que 5
"""


# Segundo Problema
salario = float(input("\nInsira seu salario: "))
gastos = float(input("Insira seus gastos: "))

if salario >= gastos:
    print("Gastos dentro do orçamento")
else:
    print("Orçamento estourado")

"""
output:

Insira seu salario: 1050.5
Insira seus gastos: 923.35
Gastos dentro do orçamento
"""


# Terceiro Problema
golsTime1 = int(input("\nInsira os gols do time 01: "))
golsTime2 = int(input("Insira os gols do outro time: "))

if golsTime1 > golsTime2:
    print("time1 GANHOU!")
elif golsTime1 < golsTime2:
    print(f"time2 GANHOU!")
else:
    print(f"Partida Empatada!")

"""
output:

Insira os gols do time 01: 1
Insira os gols do outro time: 1
Partida Empatada!
"""

# Quarto Problema
quant = int(input("\nQuant. de Pneus: "))

if quant < 10:
    print(f"Valor final: R${quant * 120}")
elif 10 <= quant < 50:
    custo = quant * 120 - ((quant * 120) * 0.05)
    print(f"Valor final: R${custo}")
elif 50 <= quant < 100:
    custo = quant * 120 - ((quant * 120) * 0.1)
    print(f"Valor final: R${custo}")
elif 100 <= quant:
    custo = quant * 120 - ((quant * 120) * 0.15)
    print(f"Valor final: R${custo}")
    
"""
output:

Quant. de Pneus: 20
Valor final: R$2280.0
"""
