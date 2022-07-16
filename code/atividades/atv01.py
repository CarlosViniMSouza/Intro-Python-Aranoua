# 1) Crie um programa em Python para cada operação aritmética,
# (Onde é necessário o usuário informar os valoresque ele desejar.)

"""
num1 = float(input("Digite um numero 01 real: "))
num2 = float(input("Digite um numero 02 real: "))

print("\nAdicao:", num1 + num2)
print("Subtracao:", num1 - num2)
print("Multiplicacao:", num1 * num2)
print("Divisao Fracionaria:", round(num1 / num2, 2))
print("Divisao Inteira:", round(num1 // num2, 2))
print("Resto da Divisao:", num1 % num2)

print("\nQuadrado do numero 1:", num1 ** 2)
print("Quadrado do numero 2:", num2 ** 2)

print("\nRaiz Quad. do numero 1:", round(num1 ** 0.5, 2))
print("Raiz Quad. do numero 2:", round(num2 ** 0.5, 2))
"""

"""
Aquele era o jeito facil, bora deixar mais elaborado:
"""

nums = list()

recep = float(input("Digite um numero real: "))
nums.append(recep)

recep = float(input("Digite outro numero real: "))
nums.append(recep)

del recep # removendo variavel desnecessaria

print(f"\nAdicao: {nums[0] + nums[1]}" +
    f"\nSubtracao: {nums[0] - nums[1]}" +
    f"\nMultiplicação: {nums[0] * nums[1]}" +
    f"\nDivisão Fracionaria: {round(nums[0] / nums[1], 2)}" +
    f"\nDivisão Inteira: {nums[0] // nums[1]}" +
    f"\nResto da Divisão: {nums[0] % nums[1]}"
) # Ops basicas

print(
    f"\nQuadrado do numero 1: {nums[0] ** 2}" +
    f"\nQuadrado do numero 2: {nums[1] ** 2}" +
    f"\nRaiz Quad. do numero 1: {round(nums[0] ** 0.5, 2)}" +
    f"\nRaiz Quad. do numero 2: {round(nums[1] ** 0.5, 2)}" +
    f"\nRaiz Cub. do numero 1: {round(nums[0] ** (1/3), 2)}" +
    f"\nRaiz Cub. do numero 2: {round(nums[1] ** (1/3), 2)}"
) # Ops Menos basicas
