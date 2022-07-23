frase = "ninguém educa ninguém, ninguém educa a si mesmo, os homens educam-se entre si, mediatizados pelo mundo"

# letra(a)
print(f"Tamanho: {len(frase)}")

# letra(b)
cont = 0
for i in frase:
    if i == "n":
        cont += 1

print(f"Quant. letra n: {cont}")

# letra(c)
print(f"Tudo maiusculo: {frase.upper()}")

"""
output:

Tamanho: 102
Quant. letra n: 9
Tudo maiusculo: NINGUÉM EDUCA NINGUÉM, NINGUÉM EDUCA A SI MESMO, OS HOMENS EDUCAM-SE ENTRE SI, MEDIATIZADOS PELO MUNDO
"""