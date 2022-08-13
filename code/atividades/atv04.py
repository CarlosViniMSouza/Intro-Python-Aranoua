"""
1. Utilizando o loop While, crie um programa que mostrar na tela os valores ímpares entre 0 e 100.

2. Utilizando o loop While, crie um programa que mostrar na tela os valores pares entre 100 e 0. Mostre do maior para o menor.

3. Crie uma lista dos peixes que você conhece, em seguida percorra a essa lista usando o loop for, até encontrar um peixe qualquer digitado pelo usuário.

4. Crie um programa usando a função range(), para gerar valores 3 a 214, incrementando 5 valores por vez.

5. Sabendo que a copa do mundo começou em 1930 e que ela se repete a cada 4 anos, mostre os anos que houve copa. (Faça duas respostas, uma usando while, outra usando o for)
"""

import os

# questao 01
for i in range(1, 100, 2):
    print("Numero: ", i)

os.system('clear')

# questao 02
for j in range(100, 0, -2):
    print("Numero: ", j)

os.system('clear')

# questão 03

peixes = ["tambaqui", "piranha", "bodo", "matrinxan"]

obj = input("Digite um peixe ai: ")
obj.lower()

for i in peixes:
    if obj == i:
        print("peixe encontrado!")

os.system('clear')

# questao 04
for k in range(3, 214, 5):
    print("Numero: ", k)

os.system('clear')

# questao 05

## usando for:
for i in range(1930, 2022, 4):
    print("Ano da copa: ", i)

os.system('clear')

## usando while:
cont = 1930

while cont < 2022:
    print("Ano de copa: ", cont)
    cont += 4