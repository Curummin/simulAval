import numpy as np
# Definição da população (1000 pessoas )

np.random.seed (42) # Para reprodutibilidade
n_pessoas = 1000

# Definição dos eventos A e B

usa_oculos = np . random . choice ([ True , False ] , size = n_pessoas , p =[0.3 ,0.7]) # 30% usam óculos
canhoto = np . random . choice ([ True , False ] , size = n_pessoas , p =[0.1 , 0.9])   #10% são canhotos

# Cálculo das probabilidades
P_A = np . mean ( usa_oculos ) # Probabilidade de usar óculos P ( A )
P_B = np . mean ( canhoto ) # Probabilidade de ser canhoto P ( B )

P_A_intersec_B = np . mean ( usa_oculos & canhoto ) # Probabilidade de usar óculos e ser canhoto P ( A e B )
P_B_dado_A = P_A_intersec_B / P_A # Probabilidade condicional P ( B | A )
# Exibição dos resultados
print (f"P ( A ) - Probabilidade de usar óculos : { P_A :.3 f } " )
print (f" P ( B ) - Probabilidade de ser canhoto : { P_B :.3 f } " )
print (f" P ( A e B ) - Probabilidade de usar óculos e ser canhoto : {P_A_intersec_B :.3 f } " )
print (f" P ( B | A ) - Probabilidade de ser canhoto dado que usa óculos : {P_B_dado_A :.3 f } " )

# Verificando a regra do produto

produto = P_A * P_B_dado_A
print (f" P ( A ) * P ( B | A ) = { produto :.3 f } ( deve ser igual a P ( A e B ) )")