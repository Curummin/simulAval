import math
import numpy as np

espaco_amostral = []

#0  =   cara
#1  =   coroa
 
for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            for l in range(0,2):
                espaco_amostral.append((i,j,k,l))

print("Espaco amostral:")
print(espaco_amostral)

valores_X = []   # soma
valores_Y = []   # maximo

for i, j, k ,l in espaco_amostral:
    valores_X.append(i + j + k + l)
    valores_Y.append(max(i, j, k, l))

print("\nValores de X = soma:")
print(valores_X)

print("\nValores de Y = maximo:")
print(valores_Y)


valores_possiveis_X = sorted(set(valores_X))
valores_possiveis_Y = sorted(set(valores_Y))

print("\nValores possiveis de X = soma:")
print(valores_possiveis_X)

print("\nValores possiveis de Y = maximo:")
print(valores_possiveis_Y)

frequencias = {}

for valor in valores_X:
    if valor in frequencias:
        frequencias[valor] += 1
    else:
        frequencias[valor] = 1

print("\nFrequencias observadas:")
print(frequencias)


# Conversao para vetores NumPy
x = np.array(sorted(frequencias.keys()))
prob = np.array([frequencias[valor] / 36 for valor in x])

# Calculo da esperanca matematica
esperanca = np.average(x, weights=prob)
print(f"\nEsperanca: {esperanca:.2f}")

# Calculo da variancia
variancia = np.average((x - esperanca)**2, weights=prob)
print(f"Variancia: {variancia:.4f}")

# Calculo do desvio padrao
desvio_padrao = math.sqrt(variancia)
print(f"Desvio padrao: {desvio_padrao:.4f}")

'''
Espaco amostral:
[(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 0, 1, 1), (0, 1, 0, 0), (0, 1, 0, 1), (0, 1, 1, 0), (0, 1, 1, 1), (1, 0, 0, 0), (1, 0, 0, 1), (1, 0, 1, 0), (1, 0, 1, 1), (1, 1, 0, 0), (1, 1, 0, 1), (1, 1, 1, 0), (1, 1, 1, 1)]

Valores de X = soma:
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

Valores de Y = maximo:
[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

Valores possiveis de X = soma:
[0, 1, 2, 3, 4]

Valores possiveis de Y = maximo:
[0, 1]

Frequencias observadas:
{0: 1, 1: 4, 2: 6, 3: 4, 4: 1}

Esperanca: 2.00
Variancia: 1.0000
Desvio padrao: 1.0000
'''