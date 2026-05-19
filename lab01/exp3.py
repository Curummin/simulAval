#João Gabriel Miguêz da Silva - 2023008890

P_S = 0.20                  # emails que são spam
P_M_dado_S = 0.90           # filtro marca como spam dado que é spam
P_M_dado_nao_S = 0.10       # femail legitimo que não é spam


P_nao_S = 1 - P_S

P_S_dado_M_bayes = (P_M_dado_S * P_S) / (P_M_dado_S * P_S + P_M_dado_nao_S * P_nao_S)

print(f"P(S|M) pelo Teorema de Bayes: {P_S_dado_M_bayes * 100:.2f}%")


def calcular_por_contagem(arquivo):
    S_e_M = 0             # S & M (interseção marcados com spam e são spam)
    M = 0       # emails marcados #(S interseção M)

    with open(arquivo, 'r') as f:
        for linha in f:
            partes = linha.strip().split()
            if len(partes) < 3:
                continue  # linha inválida
            _, real_class, filter_class = map(int, partes[:3])

            if filter_class == 1:  # filtro marcou como spam
                M += 1
                if real_class == 1:  # realmente é spam
                    S_e_M += 1

    if M == 0:
        return 0
    return S_e_M / M

P_S_dado_M_direta = calcular_por_contagem('emails.txt')
print(f"P(S|M) por contagem direta: {P_S_dado_M_direta * 100:.2f}%")

