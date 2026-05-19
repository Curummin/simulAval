import random

# Simulação de lançamentos
num_experimentos = 100000  # Número grande de experimentos para estimar probabilidades
eventos_A = 0  # Número de vezes que ocorre um número par no dado
eventos_B = 0  # Número de vezes que ocorre cara na moeda
eventos_AeB = 0  # Número de vezes que ambos ocorrem juntos

for _ in range(num_experimentos):
    dado = random.randint(1, 6)  # Lança um dado (1 a 6)
    moeda = random.choice(["C", "K"])  # Lança uma moeda (C = Cara, K = Coroa)
    
    A = dado in {2, 4, 6}  # Evento A: número par no dado
    B = moeda == "C"       # Evento B: cara na moeda
    
    if A:
        eventos_A += 1
    if B:
        eventos_B += 1
    if A and B:
        eventos_AeB += 1

# Cálculo das probabilidades experimentais
P_A = eventos_A / num_experimentos
P_B = eventos_B / num_experimentos
P_AeB = eventos_AeB / num_experimentos
P_A_P_B = P_A * P_B  # Produto das probabilidades individuais

# Exibição dos resultados
print(f"P(A) = {P_A:.4f} (Probabilidade de número par no dado)")
print(f"P(B) = {P_B:.4f} (Probabilidade de cara na moeda)")
print(f"P(A ∩ B) = {P_AeB:.4f} (Probabilidade conjunta)")
print(f"P(A) * P(B) = {P_A_P_B:.4f} (Produto das probabilidades individuais)")

# Verificação da independência
if abs(P_AeB - P_A_P_B) < 0.01:  # Pequena margem de erro devido à simulação
    print("Os eventos A e B são aproximadamente independentes.")
else:
    print("Os eventos A e B não parecem ser independentes.")