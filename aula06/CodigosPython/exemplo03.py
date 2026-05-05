from scipy.stats import chi2

# Leitura dos dados do arquivo
dados = []
with open("./modificados/dados2.txt", "r") as arq:
    for linha in arq:
        linha = linha.strip()
        if linha:
            dados.append(int(linha))

# Parametros do teste
n = len(dados)
k = 5
E = n / k      # Distribuicao uniforme
alpha = 0.05

# Classes: {0,1}, {2,3}, {4,5}, {6,7}, {8,9}
frequencias = [0] * k

for valor in dados:
    indice = valor // 2
    frequencias[indice] += 1

# Calculo do qui-quadrado
chi2_calculado = sum((f - E) ** 2 / E for f in frequencias)

# Graus de liberdade e valor critico
graus_de_liberdade = k - 1
chi2_critico = chi2.ppf(1 - alpha, graus_de_liberdade)

# Exibicao dos resultados
print(f"Quantidade de dados lidos: {n}")
print(f"Frequencias observadas: {frequencias}")
print(f"Frequencia esperada em cada classe: {E:.1f}")
print(f"Estatistica qui-quadrado calculada: {chi2_calculado:.4f}")
print(f"Valor critico (alpha={alpha}): {chi2_critico:.4f}")

if chi2_calculado <= chi2_critico:
    print("\nResultado: Nao se rejeita H0")
else:
    print("\nResultado: Rejeita-se H0")
    
