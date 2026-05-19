espaco_amostral = []

# 0 = cara
# 1 = coroa
for i in range(0,2):
  for j in range(0,2):
    for k in range(0,2):
      for l in range(0,2):
        for m in range(0,2):
          espaco_amostral.append((i,j,k,l,m))
print(f"Espaço amostral: {espaco_amostral}")

valores_X = []  #soma

for i,j,k,l,m in espaco_amostral:
    valores_X.append(i+j+k+l+m)

total_eventos = len(espaco_amostral)  

# (a) P(X > 3) = P(X = 4) + P(X = 5)
contagem_X4 = valores_X.count(4)
contagem_X5 = valores_X.count(5)
P_X_maior_3 = (contagem_X4 + contagem_X5) / total_eventos

# (b) P(X = 2)
contagem_X2 = valores_X.count(2)
P_X_igual_2 = contagem_X2 / total_eventos

# (c) E(X) = valor esperado
E_X = sum(valores_X) / total_eventos

# Resultados
print(f"Total de eventos: {total_eventos}")
print(f"\n(a) P(X > 3) = {P_X_maior_3}")
print(f"    ({contagem_X4} eventos com X=4 + {contagem_X5} eventos com X=5) / {total_eventos}")
print(f"    = {P_X_maior_3:.4f} ou {P_X_maior_3 * 100:.1f}%")

print(f"\n(b) P(X = 2) = {P_X_igual_2}")
print(f"    ({contagem_X2} eventos) / {total_eventos}")
print(f"    = {P_X_igual_2:.4f} ou {P_X_igual_2 * 100:.1f}%")

print(f"\n(c) E(X) = {E_X}")
print(f"    Soma total de caras: {sum(valores_X)} / {total_eventos}")
print(f"    = {E_X:.2f} caras em média")

