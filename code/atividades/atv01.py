# 1) Crie um programa em Python para cada operação aritmética,
# (Onde é necessário o usuário informar os valoresque ele desejar.)

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
