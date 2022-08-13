"""
1. Crie uma lista de 50 valores de numero aleatórios.
2. Remova todas os elementos cujo índice seja par.
3. Insira no inicio dessa lista 8 valores aleatórios
4. Ordene essa lista
"""

# question 01
from numpy import random

listNum = []

for i in range(1, 51):
    numRandom = random.randint(200)
    listNum.append(numRandom)

print(f"\nYour random list: {listNum}")
print(f"Size: {len(listNum)}")

# question 02
del listNum[::2]

print(f"\nNew List: {listNum}")
print(f"Size: {len(listNum)}")

# question 03
for x in range(0, 8):
    numRandom = random.randint(100)
    listNum.insert(x, numRandom)

print(f"\nList with 8 new elements: {listNum}")
print(f"Size: {len(listNum)}")

# question 04:
listNum.sort()
print(f"Sort list: {listNum}")