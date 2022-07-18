num01 = float(input("Digite um numero real: "))
num02 = float(input("Digite outro numero real: "))


def sumNums(num01, num02):
    return num01 + num02

def divIntNums(num01, num02):
    return num01 // num02

def quadNum01(num01):
    return num01 ** 2

def radQuadNum01(num01):
    return round(num01 ** 0.5, 2)

def radCubNum01(num01):
    return round(num01 ** (1/3), 2)


print(f"\nAdicao: {sumNums(num01, num02)}" +
    f"\nSubtracao: {num01 - num02}" +
    f"\nMultiplicação: {num01 * num02}" +
    f"\nDivisão Fracionaria: {round(num01 / num02, 2)}" +
    f"\nDivisão Inteira: {divIntNums(num01, num02)}" +
    f"\nResto da Divisão: {num01 % num02}"
) # Ops basicas

print(
    f"\nQuadrado do numero 1: {quadNum01(num01)}" +
    f"\nQuadrado do numero 2: {num02 ** 2}" +
    f"\nRaiz Quad. do numero 1: {radQuadNum01(num01)}" +
    f"\nRaiz Quad. do numero 2: {round(num02 ** 0.5, 2)}" +
    f"\nRaiz Cub. do numero 1: {radCubNum01(num01)}" +
    f"\nRaiz Cub. do numero 2: {round(num02 ** (1/3), 2)}"
) # Ops Menos basicas
