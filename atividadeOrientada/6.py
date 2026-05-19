# Exercício 6
import math
import matplotlib.pyplot as plt
import numpy as np
# cara = p      #probabilidade de sucesso
# coroa = 1-p   #probabilidade de fracasso
# n lançamentos
# X = numero de cara obtidas

def P(k, n, p):
    if k < 0 or k > n:
      return 0

    coefBinomial = math.factorial(n) // (math.factorial(k) * math.factorial(n-k)) 
    probabilidade = coefBinomial * (p ** k) * ((1-p) ** (n-k))
    return probabilidade


def E(p,n):
  return p * n

def V(p,n):
  return n * p * (1-p)

p_sucesso = float(input("Entre com a probabilidade de sucesso (0.0 <= p <= 1.0): "))
n = int(input("Entre com o numero de lances: "))
k = int(input("Entre com o numero de sucessos para se calcular a probabilidade: "))

print(f"Probabilidade de Cara: {P(k, n, p_sucesso)}")
print(f"Esperança E(X): {E(p_sucesso,n)}")
print(f"Variância V(X): {V(p_sucesso, n):.2f}")

# 1. Gerar todos os valores possíveis de k (de 0 até n)
eixo_x = np.arange(0, n + 1)

# 2. Calcular a probabilidade para cada valor de k usando a função P
eixo_y = [P(i, n, p_sucesso) for i in eixo_x]

# 3. Criar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(eixo_x, eixo_y, color='skyblue', edgecolor='navy', alpha=0.7)
plt.title(f'Distribuição Binomial (n={n}, p={p_sucesso})', fontsize=14)
plt.xlabel('Número de Caras (k)', fontsize=12)
plt.ylabel('Probabilidade P(X = k)', fontsize=12)
plt.xticks(eixo_x)  
plt.grid(axis='y', linestyle='--', alpha=0.6)
for i in range(len(eixo_x)):
    plt.text(eixo_x[i], eixo_y[i], f'{eixo_y[i]:.3f}', ha='center', va='bottom', fontsize=9)

plt.show()

