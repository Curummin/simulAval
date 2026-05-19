import numpy as np
from scipy.stats import chi2, poisson

dados = np.concatenate ([
        np.random.poisson(lam =2,size =500) ,   #lambda = 2
        np.random.poisson(lam =10,size =500)    #lambda = 10
])

n = len(dados)
alpha = 0.05  # Nivel de significancia
 
# Estimativa de lambda 
lambda_estimado = np.mean(dados)
 
# Classes: 0, 1, 2, ..., 14, >=15
k = 16           

frequencias = [0] * k
for v in dados:
    if v >= 15:
        frequencias[15] += 1
    else:
        frequencias[v] += 1
 
 
# Frequencias esperadas 
E = []
for i in range(k-1):
    prob = poisson.pmf(i, lambda_estimado)
    E.append(n * prob)
 
# Classe >=15
prob_tail = 1 - sum(poisson.pmf(i, lambda_estimado) for i in range(k-1))
E.append(n * prob_tail)
 
# Calculo do qui-quadrado
chi2_calculado = sum((f-e)**2 / e for f, e in zip(frequencias, E))

# Graus de liberdade: k - 1 - 1
gl = k - 2
# 8. Valor critico
chi2_critico = chi2.ppf(1 - alpha, gl)

# Saidas

print("\nTabela de frequencias observadas:")
print(f"{'Classe':<10} {'Obs':>6}")
for i in range(k - 1):
    print(f"  {i:<8} {frequencias[i]:>6}")
print(f"  >=15     {frequencias[k-1]:>6}")
 
print("\nFrequencias esperadas (Poisson):")
print(f"{'Classe':<10} {'Esp':>10}")
for i in range(k - 1):
    print(f"  {i:<8} {E[i]:>10.4f}")
print(f"  >=15     {E[k-1]:>10.4f}")

# 9. Conclusao
print(f"\n--- Resultado do Teste ---")
print(f"Lambda estimado (media): {lambda_estimado:.4f}")
print(f"Qui-quadrado calculado : {chi2_calculado:.4f}")
print(f"Graus de liberdade     : {gl}")
print(f"Valor critico (alpha={alpha}): {chi2_critico:.4f}")
 
if chi2_calculado > chi2_critico:
    print("Conclusao: Rejeita-se H0.")
    print("  Os dados NAO seguem uma distribuicao de Poisson com lambda estimado.")
else:
    print("Conclusao: Nao se rejeita H0.")
    print("  Os dados sao compativeis com uma distribuicao de Poisson com lambda estimado.")

'''
Tabela de frequencias observadas:
Classe        Obs
  0            75
  1           129
  2           128
  3            81
  4            63
  5            56
  6            28
  7            49
  8            47
  9            57
  10           84
  11           63
  12           49
  13           32
  14           24
  >=15         35

Frequencias esperadas (Poisson):
Classe            Esp
  0            2.4812
  1           14.8849
  2           44.6473
  3           89.2797
  4          133.8972
  5          160.6499
  6          160.6231
  7          137.6540
  8          103.2233
  9           68.8041
  10          41.2756
  11          22.5102
  12          11.2532
  13           5.1929
  14           2.2252
  >=15         1.3981

--- Resultado do Teste ---
Lambda estimado (media): 5.9990
Qui-quadrado calculado : 4858.4071
Graus de liberdade     : 14
Valor critico (alpha=0.05): 23.6848
Conclusao: Rejeita-se H0.
  Os dados NAO seguem uma distribuicao de Poisson com lambda estimado.


Como chi2_calculado foi maior do que o chi2_critico, temos que a hipotese de Poisson não é valida para distribuição dos dados. Provavelmente pela distribuição ser bimodal.
'''