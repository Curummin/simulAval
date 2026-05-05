from scipy.stats import chi2
import matplotlib.pyplot as plt


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

alpha = [0.10, 0.05, 0.01]

# Classes: {0,1}, {2,3}, {4,5}, {6,7}, {8,9}
frequencias = [0] * k

for valor in dados:
    indice = valor // 2
    frequencias[indice] += 1

# Calculo do qui-quadrado
chi2_calculado = sum((f - E) ** 2 / E for f in frequencias)

# Graus de liberdade e valor critico
graus_de_liberdade = k - 1

chi2_critico_alpha = []
for i in range (len(alpha)): 
    chi2_critico_alpha.append(chi2.ppf(1 - alpha[i], graus_de_liberdade))


# Exibicao dos resultados
print(f"Quantidade de dados lidos: {n}")
print(f"Frequencias observadas: {frequencias}")
print(f"Frequencia esperada em cada classe: {E:.1f}")
print(f"Estatistica qui-quadrado calculada: {chi2_calculado:.4f}")

for i in range (len(alpha)):
    print(f"Valor critico (alpha{i+1} ={alpha[i]}): {chi2_critico_alpha[i]:.4f}")


for i in range (len(alpha)):
    if chi2_calculado <= chi2_critico_alpha[i]:
        print(f"\nResultado (alpha{i+1} = {alpha[i]}): Nao se rejeita H0")
    else :
        print(f"\nResultado: (alpha{i+1} = {alpha[i]}): Rejeita-se H0")

# =========================
# TABELA DE FREQUÊNCIAS
# =========================
print("\n===== TABELA DE FREQUÊNCIAS =====")
print(f"{'Classe':<10}{'Fo':<10}{'Fe':<10}")

classes = ["0-1", "2-3", "4-5", "6-7", "8-9"]

for i in range(k):
    print(f"{classes[i]:<10}{frequencias[i]:<10}{E:<10.2f}")

# =========================
# RESUMO GERAL
# =========================
print("\n===== RESUMO =====")
print(f"Quantidade total de dados2.txt: {n}")
print(f"Qui-quadrado calculado: {chi2_calculado:.4f}")
print(f"Graus de liberdade: {4}")

# =========================
# TABELA DO TESTE (α)
# =========================
print("\n===== TESTE QUI-QUADRADO =====")
print(f"{'Alpha':<10}{'Chi2 Critico':<20}{'Decisão'}")

for i in range(len(alpha)):
    decisao = "Não rejeita H0" if chi2_calculado <= chi2_critico_alpha[i] else "Rejeita H0"
    print(f"{alpha[i]:<10}{chi2_critico_alpha[i]:<20.4f}{decisao}")
'''
Quantidade de dados lidos: 1000
Frequencias observadas: [361, 270, 185, 122, 62]
Frequencia esperada em cada classe: 200.0
Estatistica qui-quadrado calculada: 280.8700
Valor critico (alpha1 =0.1): 7.7794
Valor critico (alpha2 =0.05): 9.4877
Valor critico (alpha3 =0.01): 13.2767

Resultado: (alpha1 = 0.1): Rejeita-se H0

Resultado: (alpha2 = 0.05): Rejeita-se H0

Resultado: (alpha3 = 0.01): Rejeita-se H0

===== TABELA DE FREQUÊNCIAS =====
Classe    Fo        Fe        
0-1       361       200.00    
2-3       270       200.00    
4-5       185       200.00    
6-7       122       200.00    
8-9       62        200.00    

===== RESUMO =====
Quantidade total de dados2.txt: 1000
Qui-quadrado calculado: 280.8700
Graus de liberdade: 4

===== TESTE QUI-QUADRADO =====
Alpha     Chi2 Critico        Decisão
0.1       7.7794              Rejeita H0
0.05      9.4877              Rejeita H0
0.01      13.2767             Rejeita H0

1. Para todos alphas h0 foi rejeitado
2. Após executar para ambos conjuntos, temos que dados2.txt tem maior chi2
3.Os dados não são compativeis com a distribuição uniforme
4.O valor calculado é muito maior que o esperado
'''