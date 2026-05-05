import numpy as np
from scipy.stats import chi2, poisson

# Geracao dos dados
dados = np.random.poisson(lam=5, size=1000)

n = len(dados)
alpha = 0.05

# Estimativa de lambda
lambda_estimado = np.mean(dados)

# Classes: 0,1,2,3,4,5,6,7, >=8
k = 9
frequencias = [0] * k

for v in dados:
    if v >= 8:
        frequencias[8] += 1
    else:
        frequencias[v] += 1
        
# Frequencias esperadas
E = []
for i in range(8):
    prob = poisson.pmf(i, lambda_estimado)
    E.append(n * prob)

# Classe >=8
prob_tail = 1 - sum(poisson.pmf(i, lambda_estimado) for i in range(8))
E.append(n * prob_tail)

# Qui-quadrado
chi2_calculado = sum((f - e)**2 / e for f, e in zip(frequencias, E))

# Graus de liberdade
gl = k - 2

# Valor critico
chi2_critico = chi2.ppf(1 - alpha, gl)

# Saidas
print("Lambda estimado:", lambda_estimado)
print("Frequencias observadas:", frequencias)
print("Frequencias esperadas:", [round(e,2) for e in E])
print("Qui-quadrado:", chi2_calculado)
print("Valor critico:", chi2_critico)

if chi2_calculado <= chi2_critico:
    print("Nao se rejeita H0 (Poisson)")
else:
    print("Rejeita-se H0")

