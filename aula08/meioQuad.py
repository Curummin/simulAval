def meio_quadrado_ciclo(semente, n_digitos=3):
    posicao = {}
    atual = semente
    passo = 0

    while atual not in posicao:
        posicao[atual] = passo
        quadrado = str(atual ** 2).zfill(2 * n_digitos)
        total_digitos = len(quadrado)
        meio = total_digitos // 2
        inicio = max(0, meio - n_digitos // 2)
        fim = inicio + n_digitos
        trecho = quadrado[inicio:fim].zfill(n_digitos)
        atual = int(trecho)
        passo += 1

    s0 = semente
    p = posicao[atual]       # passos até o início do ciclo
    x = atual                # primeiro valor que se repetiu
    t = passo - posicao[atual]  # tamanho do período

    return ((s0, p), (x, t))


# Analisar todas as sementes de 000 a 999
melhor = None

for semente in range(1000):
    resultado = meio_quadrado_ciclo(semente, n_digitos=3)
    (s0, p), (x, t) = resultado

    if melhor is None:
        melhor = resultado
    else:
        (_, p_melhor), (_, t_melhor) = melhor
        # Maior período; em empate, maior sequência antes do ciclo
        if t > t_melhor or (t == t_melhor and p > p_melhor):
            melhor = resultado

(s0_melhor, p_melhor), (x_melhor, t_melhor) = melhor
print(f"Melhor semente: {s0_melhor:03d}")
print(f"  Passos até o ciclo (p): {p_melhor}")
print(f"  Início do ciclo (x):    {x_melhor:03d}")
print(f"  Tamanho do período (t): {t_melhor}")
print(f"  Resultado: (({s0_melhor:03d}, {p_melhor}), ({x_melhor:03d}, {t_melhor}))")

'''
Melhor semente: 514
  Passos até o ciclo (p): 21
  Início do ciclo (x):    160
  Tamanho do período (t): 4
  Resultado: ((514, 21), (160, 4))
'''