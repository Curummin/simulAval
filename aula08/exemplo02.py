def gerador_congruente_multiplicativo(semente, beta, alpha, iteracoes):
    print(f"{'i':<3} {'s[i-1]':<7} {'β·s[i-1]':<10} {'s[i]':<5} {'r[i]':<6}")
    print("-" * 35)
    s = semente
    for i in range(1, iteracoes + 1):
        produto = beta * s
        s_novo = produto % alpha
        r = s_novo / alpha
        print(f"{i:<3} {s:<7} {produto:<10} {s_novo:<5} {r:<6.4f}")
        s = s_novo

# Parâmetros conforme o exemplo
semente = 7
beta = 5
alpha = 16
iteracoes = 10

gerador_congruente_multiplicativo(semente, beta, alpha, iteracoes)

