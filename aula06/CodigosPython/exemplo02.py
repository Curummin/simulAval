from scipy.stats import chi2

alfas = [0.10, 0.05, 0.01]
gls = [1, 2, 3, 4, 5]

print(" gl |  alpha=0.10 |  alpha=0.05 |  alpha=0.01")
print("-" * 46)

for gl in gls:
    valores = [chi2.ppf(1 - a, gl) for a in alfas]
    print(f"{gl:>3} | {valores[0]:>11.3f} | "
          f"{valores[1]:>11.3f} | {valores[2]:>11.3f}")
