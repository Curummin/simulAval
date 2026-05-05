import numpy as np
from scipy.stats import chi2

# Geracao dos dados
np.random.seed(42)
dados = np.random.exponential(scale=2, size=1000)

n = len(dados)
alpha = 0.05

# Estimativa de lambda
media = np.mean(dados)
lambda_estimado = 1 / media

print("Media:", round(media, 3))
print("Lambda estimado:", round(lambda_estimado, 3))

# Intervalos equiprovaveis (aprox. 20%)
intervalos = [0, 0.45, 1.02, 1.83, 3.22, np.inf]

k = 5
frequencias = [0] * k

# Contagem das frequencias observadas
for v in dados:
    for i in range(k):
        if intervalos[i] <= v < intervalos[i+1]:
            frequencias[i] += 1
            break

print("Frequencias observadas:", frequencias)

# Frequencias esperadas (equiprovaveis)
E = [n / k] * k

# Calculo do qui-quadrado
chi2_calculado = sum((f - e)**2 / e for f, e in zip(frequencias, E))

# Graus de liberdade
gl = k - 2

# Valor critico
chi2_critico = chi2.ppf(1 - alpha, gl)

print("Qui-quadrado:", round(chi2_calculado, 2))
print("Valor critico:", round(chi2_critico, 2))

if chi2_calculado <= chi2_critico:
    print("Nao se rejeita H0 (distribuicao exponencial)")
else:
    print("Rejeita-se H0")

