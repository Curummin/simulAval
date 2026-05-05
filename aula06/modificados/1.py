import matplotlib.pyplot as plt

# Substituir pelos dados do arquivo
dados1 = [0, 3, 7, 2, 9, 5, 1, 8, 4, 6,
         2, 7, 0, 5, 9, 3, 6, 1, 8, 4]

dados2 =[]
dados3 = []

with open('./CodigosPython/dados2.txt', 'r', encoding='utf-8') as arquivo:
    # readlines() cria uma lista onde cada item é uma linha do arquivo
    dados2 = arquivo.readlines()

# Limpando os caracteres de nova linha (\n) que vêm junto com o texto
dados2 = [int(linha.strip()) for linha in dados2]

with open('./CodigosPython/dados3.txt', 'r', encoding='utf-8') as arquivo:
    # readlines() cria uma lista onde cada item é uma linha do arquivo
    dados3 = arquivo.readlines()

# Limpando os caracteres de nova linha (\n) que vêm junto com o texto
dados3 = [int(linha.strip()) for linha in dados3]

print(f"DADOS 1: {dados1} \nDADOS 2 {dados2} \nDADOS 3 {dados3}")
# Inicializa frequencias de 0 a 9
frequencias = [0] * 10

# Conta ocorrencias de todos os dados
for valor in dados1:
    frequencias[valor] += 1
for valor in dados2:
    frequencias[valor] += 1
for valor in dados3:
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

