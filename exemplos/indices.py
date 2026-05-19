import numpy as np

# Dados de exemplo
dados = np . array ([10 , 12 , 15 , 20 , 22 , 24 , 30])

# Medidas de tendência central
media   =     np.mean(dados)
mediana =   np.median(dados)
ponto_medio = (np.max(dados)+ np.min(dados))/2

# Medidas de dispersão

variancia = np . var ( dados , ddof =1)             # ddof =1 para amostral
desvio_padrao = np . std ( dados , ddof =1)
coef_var = desvio_padrao / media
amplitude = np . ptp ( dados )                      # Diferença entre max e min

# Exibindo resultados
print (f"Média : {media:.2f}" )
print (f"Mediana : {mediana:.2f}")
print (f"Ponto Médio : {ponto_medio :.2f}")
print (f"Variância : {variancia:.2f}")
print(f"Desvio Padrão : {desvio_padrao:.2f}")
print(f"Coeficiente de Variação : {coef_var:.2f}")
print(f"Amplitude : {amplitude:.2f}")
