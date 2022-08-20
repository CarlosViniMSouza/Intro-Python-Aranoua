"""
-> Dicionários

Q1. Crie um dicionário, onde a fruta é a chave e o preço será o valor:

Q2. Insira ao menos 7 frutas com seus respectivos valores.

Q3. Crie um laço for() junto com um if(), para buscar uma determinada fruta que o usuário digitar.


-> Set

Q4. Crie um set de frutas e peixes, sem seguida faça a união desses 2 sets.
"""

# q01

fruits = {
    "apple": 3.50,
    "banana": 5.60,
    "orange": 6.15,
    "strawberry": 8.35,
}

print("\n", fruits)

# q02

fruits = {
    "apple": 3.50,
    "banana": 5.60,
    "orange": 6.15,
    "strawberry": 8.35,
    "peach": 4.80,
    "grape": 3.40,
    "watermelon": 10.30
}

print("\n", fruits)

# q03

obj = input("\nWrite an fruit: ")
obj.lower()

for i in fruits:
    if obj == i:
        print("\nFruit founded!!")

# q04

fruits = {"apple", "banana", "orange"}
fishes = {"tambaqui", "pirarucu", "tucunare"}

fruits.update(fishes)

print("\n", fruits)
