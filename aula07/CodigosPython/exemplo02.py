import math
from scipy.stats import chi2

f = [50, 60, 70, 80, 90, 110, 120, 140, 280]

n = sum(f)
k = len(f)
alpha = 0.05
lambda_estimado = 6

E = []

for i in range(8):
    prob = math.exp(-lambda_estimado) * lambda_estimado**i / math.factorial(i)
    E.append(n * prob)

# Classe >= 8
prob_tail = 1 - sum(E) / n
E.append(n * prob_tail)

chi2_calculado = sum((fo - fe)**2 / fe for fo, fe in zip(f, E))

gl = k - 2
chi2_critico = chi2.ppf(1 - alpha, gl)

print("Frequencias esperadas:", [round(e, 2) for e in E])
print("Qui-quadrado:", round(chi2_calculado, 2))
print("Valor critico:", round(chi2_critico, 2))

if chi2_calculado > chi2_critico:
    print("Rejeita-se H0")
else:
    print("Nao se rejeita H0")
    

