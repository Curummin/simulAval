import numpy as np
from scipy.stats import trim_mean

with open("./lab01/dados.txt", "r") as arq:
    dados = np.array([int(linha.strip()) for linha in arq])

media = np.mean(dados)
valores_k = [2, 4, 6, 8, 10]

print(f"{'Media':>10}", end="")
for k in valores_k:
    print(f"{f'k={k}':>10}", end="")
print()

print(f"{media:10.2f}", end="")
for k in valores_k:
    media_aparada = trim_mean(dados, proportiontocut=k/100)
    print(f"{media_aparada:10.2f}", end="")

print()