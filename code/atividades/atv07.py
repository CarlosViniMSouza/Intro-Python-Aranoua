"""
1. Crie um programa onde seja possível realizar as 6 operações matemáticas (adição, subtração, divisão, multiplicação, potenciação e Radiciação), para cada operação terá uma função.

2. Crie um programa de votação, onde terá 4 candidatos a presidente de turma:

° Arlindo - 12, 
° Zezinho - 13, 
° Jefferson - 25, 
° Wallace - 45, 

Leve em consideração apenas o numero do candidato, o sistema de votação só deve acabar quando for digitado o valor de -9 (nove negativo), após finalizar, apresentar a quantidade de votos de cada um e dizer o vencedor. Particione esse código em funções.
"""

# question 01:

def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def product(n1, n2):
    return n1 * n2

def div(n1, n2):
    return round((n1/n2), 2)

def pot(n1, n2):
    return n1 ** n2

def rad(n1, n2):
    rad = n1 ** (1/n2)
    return round(rad, 2)

print(f"The sum is: {sum(10, 5)}")
print(f"The sub is: {sub(10, 5)}")
print(f"The product is: {product(10, 5)}")
print(f"The div is: {div(10, 5)}")
print(f"The pot is: {pot(10, 5)}")
print(f"The rad is: {rad(10, 5)}")

# question 02:

votes = []

def vote():
    number = int(input("\nWrite your number vote: "))

    while(number != -9):
        votes.append(number)
        number = int(input("Write your number vote: "))

def announceWinner():
    print(f"\nTotal votes for number 12: {votes.count(12)}")
    print(f"Total votes for number 13: {votes.count(13)}")
    print(f"Total votes for number 25: {votes.count(25)}")
    print(f"Total votes for number 45: {votes.count(45)}")

    if votes.count(12) > votes.count(13) and votes.count(25) and votes.count(45):
        print("\nCandidate Number 12 winner!")
    elif votes.count(13) > votes.count(12) and votes.count(25) and votes.count(45):
        print("\nCandidate Number 13 winner!")
    elif votes.count(25) > votes.count(12) and votes.count(13) and votes.count(45):
        print("\nCandidate Number 25 winner!")
    elif votes.count(45) > votes.count(12) and votes.count(13) and votes.count(25):
        print("\nCandidate Number 45 winner!")
    else:
        print("\nTie between candidates!")

vote()
announceWinner()
