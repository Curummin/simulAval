def bayes_theorem(prior_D, sensitivity, false_positive):
    """
    Calcula a probabilidade de estar doente dado um teste positivo
    usando o Teorema de Bayes.

    Parâmetros:
    - prior_D: Probabilidade de ter a doença, P(D)
    - sensitivity: Sensibilidade do teste (probabilidade de testar
    positivo dado que tem a doença), P(T+|D)
    - false_positive: Taxa de falso positivo (probabilidade de testar
    positivo sem ter a doença), P(T+|D^c)

    Retorna:
    - P(D|T+): Probabilidade de estar doente dado que o teste foi
    positivo
    """
    prior_not_D = 1 - prior_D # P(D^c)

    # --- Teorema de Bayes
    numerator = sensitivity * prior_D
    denominator = (sensitivity * prior_D) + (false_positive * prior_not_D)

    posterior_D_given_T = numerator / denominator
    return posterior_D_given_T

# Definição dos valores do problema
prior_D = 0.01    # 1% da população tem a doença
sensitivity = 0.95   # O teste identifica corretamente 95% dos doentes
false_positive = 0.10 # O teste dá falso positivo em 10% dos casos

# Cálculo da probabilidade condicional
prob_D_given_T = bayes_theorem(prior_D, sensitivity, false_positive)

# Exibir resultado
print(f"A probabilidade de estar doente dado um teste positivo é {prob_D_given_T:.4f} ({prob_D_given_T * 100:.2f}%).")