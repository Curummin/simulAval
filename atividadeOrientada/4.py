# Exercício 4
espaco_amostral = []

for i in range (0,5):
  for j in range (0,5):
      espaco_amostral.append((i,j))

valores_X = []   # soma
valores_Y = []   # maximo

for i, j in espaco_amostral:
    valores_X.append(i + j)
    valores_Y.append(max(i, j))

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

