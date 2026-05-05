import matplotlib.pyplot as plt

# Substituir pelos dados do arquivo
dados = [0, 3, 7, 2, 9, 5, 1, 8, 4, 6,
         2, 7, 0, 5, 9, 3, 6, 1, 8, 4]

# Inicializa frequencias de 0 a 9
frequencias = [0] * 10

# Conta ocorrencias
for valor in dados:
    frequencias[valor] += 1


# Exibe tabela de frequencias
for i in range(10):
    print(f"Valor {i}: {frequencias[i]}")

    
# Segunda parte 
    
# Valores possiveis
valores = list(range(10))

# Grafico de barras
plt.bar(valores, frequencias)

plt.xlabel("Valores")
plt.ylabel("Frequencia")
plt.title("Distribuicao dos dados")

plt.show()

