def meio_quadrado_tabela(semente, n_digitos=4, iteracoes=10):
    resultados = [semente]

    for _ in range(iteracoes):
        quadrado = str(resultados[-1] ** 2).zfill(2 * n_digitos)
        total_digitos = len(quadrado)
        meio = total_digitos // 2
        inicio = max(0, meio - n_digitos // 2)
        fim = inicio + n_digitos
        trecho = quadrado[inicio:fim]
        # Ajustar caso o trecho seja menor que n_digitos
        trecho = trecho.zfill(n_digitos)
        resultados.append(int(trecho))

    return resultados

# Exemplo de uso
sequencia = meio_quadrado_tabela(5731, n_digitos=4, iteracoes=10)
for i, num in enumerate(sequencia):
    print(f"{i}: {num:04d}")

